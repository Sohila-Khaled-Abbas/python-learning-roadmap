"""Exercise outcomes and runner behavior, using the same contracts as the browser."""
import importlib.util
import json
from pathlib import Path
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("lab_runner", ROOT / "web/lab-runner.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)
catalog = json.loads(subprocess.check_output([
    "node", "--input-type=module", "-e",
    "import {challenges,ORDERS_CSV} from './web/lab-curriculum.mjs'; console.log(JSON.stringify({challenges,csv:ORDERS_CSV}));"
], cwd=ROOT, text=True))


def execute(code, **options):
    return json.loads(runner.execute_lab(json.dumps({
        "code": code, "csv": catalog["csv"], "mode": "run", **options
    })))


class LabContracts(unittest.TestCase):
    def test_reference_solutions_and_incomplete_starters(self):
        for challenge in catalog["challenges"]:
            if not challenge["checks"]:
                continue
            if challenge.get("packages") and not importlib.util.find_spec("pandas"):
                # No new dependency for the standard-library CI. pandas is also
                # exercised against the actual WebAssembly runtime in browser QA.
                continue
            with self.subTest(challenge=challenge["id"]):
                result = execute(challenge["solution"], mode="check", checks=challenge["checks"])
                self.assertIsNone(result["error"], result["error"])
                self.assertEqual(len(result["checks"]), len(challenge["checks"]))
                self.assertTrue(all(c["passed"] for c in result["checks"]), result["checks"])
                starter = execute(challenge["starter"], mode="check", checks=challenge["checks"])
                self.assertFalse(all(c["passed"] for c in starter["checks"]), challenge["id"])

    def test_fresh_namespace_and_dataset_on_each_run(self):
        execute('leaked = 42\nopen("orders.csv", "w").write("changed")\nopen("extra.txt", "w").write("temp")')
        result = execute('from pathlib import Path\nprint("leaked" in globals())\nprint(Path("extra.txt").exists())\nprint(open("orders.csv").read())')
        self.assertTrue(result["stdout"].startswith("False\nFalse\norder_id,"), result)

    def test_input_errors_and_unicode_output(self):
        result = execute('import sys\nprint("أهلاً", input())\nprint("diagnostic", file=sys.stderr)', stdin="Sohila\n")
        self.assertEqual(result["stdout"], "أهلاً Sohila\n")
        self.assertEqual(result["stderr"], "diagnostic\n")
        self.assertIn("EOFError", execute('input()')["error"])
        self.assertIn("SyntaxError", execute('def broken(:')["error"])
        self.assertIn("SystemExit", execute('raise SystemExit(2)')["error"])

    def test_output_is_bounded_and_bad_code_does_not_pass(self):
        result = execute('print("x" * 1000000)')
        self.assertEqual(len(result["stdout"]), 16000)
        self.assertTrue(result["truncated"])
        result = execute('raise RuntimeError("try again")', mode="check", checks=[{"name":"must not run","code":"assert True"}])
        self.assertEqual(result["checks"], [])
        self.assertIn("try again", result["error"])


if __name__ == "__main__":
    unittest.main()
