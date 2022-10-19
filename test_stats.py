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

    def test_add_value_to_datacapture_with_wrong_input_value_raise_valueerror(self):
        data_capture = DataCapture()
        with self.assertRaises(ValueError) as context:
            data_capture.add('a')

    def test_data_capture_build_stats_returns_stats(self):
        stats = self.data_capture.build_stats()
        self.assertIsInstance(stats, Stats)

    def test_stats_less_return_right_value(self):
        stats = self.data_capture.build_stats()
        self.assertEqual(stats.less(4), 2)

    def test_stats_less_raise_error_with_wrong_input_value(self):
        stats = self.data_capture.build_stats()
        with self.assertRaises(ValueError) as context:
            self.assertEqual(stats.less('a'), 2)

    def test_stats_between_return_right_value(self):
        stats = self.data_capture.build_stats()
        self.assertEqual(stats.between(3, 6), 4)

    def test_stats_between_raise_error_with_wrong_input_value(self):
        stats = self.data_capture.build_stats()
        with self.assertRaises(ValueError) as context:
            self.assertEqual(stats.between('a', 6), 4)
        with self.assertRaises(ValueError) as context:
            self.assertEqual(stats.between(3, 'a'), 4)

    def test_stats_greater_return_right_value(self):
        stats = self.data_capture.build_stats()
        self.assertEqual(stats.greater(4), 2)

    def test_stats_greater_raise_error_with_wrong_input_value(self):
        stats = self.data_capture.build_stats()
        with self.assertRaises(ValueError) as context:
            self.assertEqual(stats.greater('a'), 2)
