import csv
import json
from pathlib import Path
import tempfile
import unittest
from projects.pipeline import run, parse_row

ROOT = Path(__file__).resolve().parents[1]


class PipelineContracts(unittest.TestCase):
    def test_reconciliation_quarantine_and_rerun(self):
        source = ROOT/'data/fixtures/orders.csv'
        before = source.read_bytes()
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            first = run(source, base/'orders.sqlite', base/'out')
            self.assertEqual((first['input_rows'], first['accepted'], first['rejected']), (7, 4, 3))
            self.assertEqual((first['stored_rows'], first['stored_total_piastres']), (3, 36175))
            self.assertEqual(first['input_rows'], first['accepted']+first['rejected'])
            second = run(source, base/'orders.sqlite', base/'out')
            self.assertEqual(second['inserted'], 0)
            self.assertEqual(second['stored_total_piastres'], 36175)
            with (base/'out/rejects.csv').open(encoding='utf-8') as handle:
                rejects = list(csv.DictReader(handle))
            self.assertEqual(len(rejects), 3)
            self.assertTrue(all(r['reason'] and json.loads(r['raw_json']) for r in rejects))
            self.assertIn('عناية بالبشرة', (base/'out/orders.csv').read_text(encoding='utf-8'))
        self.assertEqual(source.read_bytes(), before)

    def test_conflicting_duplicate_keeps_original(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            source = base/'source.csv'
            source.write_text('order_id,order_date,category,quantity,unit_price_egp\nX,2026-01-01,A,1,10.00\nX,2026-01-01,A,1,99.00\n', encoding='utf-8')
            result = run(source, base/'db.sqlite', base/'out')
            self.assertEqual((result['stored_total_piastres'], result['rejected']), (1000, 1))

    def test_invalid_header_does_not_create_database(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            source = base/'wrong.csv'; source.write_text('id,amount\n1,2\n')
            with self.assertRaises(ValueError):
                run(source, base/'db.sqlite', base/'out')
            self.assertFalse((base/'db.sqlite').exists())

    def test_empty_valid_file(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            source = base/'empty.csv'; source.write_text('order_id,order_date,category,quantity,unit_price_egp\n')
            result = run(source, base/'db.sqlite', base/'out')
            self.assertEqual((result['stored_rows'], result['stored_total_piastres']), (0, 0))

    def test_precision_and_integer_overflow_rejected(self):
        row = dict(order_id='1',order_date='2026-01-01',category='A',quantity='1',unit_price_egp='0.001')
        with self.assertRaises(ValueError):
            parse_row(row)
        row['unit_price_egp']='999999999999999999999999999999999999999999999999999'
        with self.assertRaises(ValueError):
            parse_row(row)

    def test_source_output_collision(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder)/'orders.csv'
            source.write_text('order_id,order_date,category,quantity,unit_price_egp\n')
            with self.assertRaises(ValueError):
                run(source, Path(folder)/'db.sqlite', Path(folder))


if __name__ == '__main__':
    unittest.main()
