from unittest import TestCase

from stats import DataCapture, Stats


class StatsTestCase(TestCase):

    def setUp(self):
        self.data_capture = DataCapture()
        self.data_capture.add(3)
        self.data_capture.add(9)
        self.data_capture.add(3)
        self.data_capture.add(4)
        self.data_capture.add(6)

    def test_data_capture_build_stats_returns_stats(self):
        stats = self.data_capture.build_stats()
        self.assertIsInstance(stats, Stats)

    def test_stats_less_return_right_value(self):
        stats = self.data_capture.build_stats()
        self.assertEqual(stats.less(4), 2)

    def test_stats_between_return_right_value(self):
        stats = self.data_capture.build_stats()
        self.assertEqual(stats.between(3, 6), 4)

    def test_stats_less_return_right_value(self):
        stats = self.data_capture.build_stats()
        self.assertEqual(stats.greater(4), 2)
