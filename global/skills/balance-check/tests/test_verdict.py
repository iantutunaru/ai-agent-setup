"""Tests for verdict.py. Expected numbers come from the JavaScript tool it was ported from (run on the same inputs)."""

import math
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import verdict as v  # noqa: E402

BAND = (0.45, 0.55)


class Wilson(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(v.wilson(0, 0), (0.0, 1.0))

    def test_all_wins_stays_in_range(self):
        low, high = v.wilson(20, 20)
        self.assertAlmostEqual(low, 0.8389, places=3)
        self.assertEqual(high, 1.0)

    def test_half(self):
        low, high = v.wilson(50, 100)
        self.assertAlmostEqual(low, 0.4038, places=3)
        self.assertAlmostEqual(high, 0.5962, places=3)


class Verdict(unittest.TestCase):
    def test_fair(self):
        self.assertEqual(v.verdict(v.wilson(2000, 4000), BAND), "fair")

    def test_unbalanced(self):
        self.assertEqual(v.verdict(v.wilson(67, 100), BAND), "unbalanced")

    def test_unclear(self):
        self.assertEqual(v.verdict(v.wilson(50, 100), BAND), "unclear")


class MoreNeeded(unittest.TestCase):
    def test_settled_is_zero(self):
        self.assertEqual(v.more_needed(67, 100, BAND), 0)

    def test_on_the_edge_is_infinite(self):
        self.assertEqual(v.more_needed(55, 100, BAND), math.inf)

    def test_true_half_needs_about_385(self):
        self.assertEqual(v.more_needed(50, 100, BAND) + 100, 385)


class Report(unittest.TestCase):
    def test_lines(self):
        self.assertTrue(v.report(67, 100, BAND).endswith(": unbalanced"))
        self.assertTrue(v.report(50, 100, BAND).endswith(": unclear, run about 285 more"))
        self.assertTrue(v.report(55, 100, BAND).endswith(": borderline"))


if __name__ == "__main__":
    unittest.main()
