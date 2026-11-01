"""Execute an original learning exercise in fresh globals and temporary fixtures.

Used by Pyodide in a Web Worker and by the repository's Python contract tests.
This is a learning runner, not a security boundary for untrusted hosted code.
"""
import contextlib
import io
import json
import os
import shutil
import tempfile
import traceback


class _LimitedOutput(io.StringIO):
    def write(self, text):
        remaining = max(0, 16000 - self.tell())
        super().write(text[:remaining])
        return len(text)


def execute_lab(payload_json):
    payload = json.loads(payload_json)
    output, errors = _LimitedOutput(), _LimitedOutput()
    namespace = {"__name__": "__main__", "__file__": "practice.py"}
    result = {"stdout": "", "stderr": "", "error": None, "checks": []}
    original_dir = os.getcwd()
    folder = tempfile.mkdtemp(prefix="python-lab-")
    import sys
    original_stdin = sys.stdin
    try:
        os.chdir(folder)
        with open("orders.csv", "w", encoding="utf-8", newline="") as handle:
            handle.write(payload.get("csv", ""))
        sys.stdin = io.StringIO(payload.get("stdin", ""))
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors):
            try:
                exec(compile(payload["code"], "practice.py", "exec"), namespace)
            except BaseException as exc:
                result["error"] = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))[-8000:]
            if result["error"] is None and payload.get("mode") == "check":
                for check in payload.get("checks", []):
                    try:
                        exec(compile(check["code"], "exercise_check.py", "exec"), namespace)
                    except BaseException as exc:
                        detail = str(exc) or type(exc).__name__
                        result["checks"].append({"name": check["name"], "passed": False, "detail": f"{type(exc).__name__}: {detail}"[:1500]})
                    else:
                        result["checks"].append({"name": check["name"], "passed": True, "detail": "Passed"})
    finally:
        sys.stdin = original_stdin
        os.chdir(original_dir)
        shutil.rmtree(folder, ignore_errors=True)
        result["stdout"], result["stderr"] = output.getvalue(), errors.getvalue()
        result["truncated"] = len(result["stdout"]) >= 16000 or len(result["stderr"]) >= 16000
    return json.dumps(result, ensure_ascii=False)
