"""One contract per video chapter. Default checks reference solutions, --practice checks yours."""
import argparse
import importlib
import unittest

TARGET = 'solutions.foundations'


class FoundationContracts(unittest.TestCase):
    def setUp(self):
        self.f = importlib.import_module(TARGET)

    def test_01_message(self):
        self.assertEqual(self.f.pipeline_message('landing', 4), 'landing: 4 rows')

    def test_02_money_precision(self):
        self.assertEqual(self.f.to_piastres('12.50'), 1250)
        self.assertEqual(self.f.to_piastres('-1.05'), -105)
        for bad in ['0.001', '', 'NaN', 'Infinity', '1e2']:
            with self.subTest(value=bad), self.assertRaises(ValueError):
                self.f.to_piastres(bad)

    def test_03_discount(self):
        self.assertEqual(self.f.net_revenue(10000, 1500), 8500)
        with self.assertRaises(ValueError):
            self.f.net_revenue(100, 101)

    def test_04_no_mutation(self):
        original = {'id': 1}
        self.assertEqual(self.f.classify_copy(original, 'Food'), {'id': 1, 'category': 'Food'})
        self.assertEqual(original, {'id': 1})

    def test_05_empty_and_zero(self):
        self.assertIsNone(self.f.mean_or_none([]))
        self.assertEqual(self.f.mean_or_none([0, 10]), 5)

    def test_06_partial_page(self):
        self.assertEqual(self.f.page_count(101, 50), 3)
        self.assertEqual(self.f.page_count(0, 50), 0)
        with self.assertRaises(ValueError):
            self.f.page_count(1, 0)

    def test_07_missing_vs_zero(self):
        self.assertEqual([self.f.amount_status(x) for x in [None, -1, 0, 1]], ['missing', 'invalid', 'zero', 'valid'])

    def test_08_skip_invalid(self):
        self.assertEqual(self.f.valid_total([None, 0, -2, 10]), 10)
        self.assertEqual(self.f.valid_total([]), 0)

    def test_09_slice_boundary(self):
        items = [1, 2, 3]
        self.assertEqual(self.f.latest(items, 2), [2, 3])
        self.assertEqual(self.f.latest(items, 0), [])
        self.assertEqual(items, [1, 2, 3])

    def test_10_group(self):
        rows = [{'category': 'Food', 'amount': 300}, {'category': 'Food', 'amount': 200}]
        self.assertEqual(self.f.totals_by_category(rows), {'Food': 500})

    def test_11_reconcile_keys(self):
        self.assertEqual(self.f.missing_ids([1, 2, 2, 4], [1, 4]), [2])

    def test_12_narrow_parse(self):
        self.assertEqual(self.f.parse_count('12'), 12)
        for bad in ['12.5', '', -1, True]:
            with self.subTest(value=bad), self.assertRaises(ValueError):
                self.f.parse_count(bad)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--practice', action='store_true', help='check exercises/foundations.py; unfinished tasks fail intentionally')
    args = parser.parse_args()
    if args.practice:
        TARGET = 'exercises.foundations'
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(FoundationContracts)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(not result.wasSuccessful())
