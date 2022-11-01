from unittest import TestCase
from unittest.mock import patch

from stats import DataCapture, Stats, Program


class DataCaptureTestCase(TestCase):

    def test_add_value_to_datacapture_with_two_values(self):
        data_capture = DataCapture()
        data_capture.add(1)
        data_capture.add(2)
        self.assertIn(1, data_capture.elements)
        self.assertIn(2, data_capture.elements)

    def test_add_value_to_datacapture_with_wrong_input_value_raise_valueerror(self):
        data_capture = DataCapture()
        with self.assertRaises(ValueError) as context:
            data_capture.add('a')

    def test_data_capture_build_stats_returns_stats(self):
        data_capture = DataCapture()
        data_capture.add(3)
        data_capture.add(9)
        stats = data_capture.build_stats()
        self.assertIsInstance(stats, Stats)


class StatsTestCase(TestCase):

    def setUp(self):
        self.data_capture = DataCapture()
        self.data_capture.add(3)
        self.data_capture.add(9)
        self.data_capture.add(3)
        self.data_capture.add(4)
        self.data_capture.add(6)

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

    def test_stats_between_raise_error_with_negative_values(self):
        stats = self.data_capture.build_stats()
        with self.assertRaises(ValueError) as context:
            self.assertEqual(stats.between(-1, 6), 4)
        with self.assertRaises(ValueError) as context:
            self.assertEqual(stats.between(3, -6), 4)

    def test_stats_between_raise_error_with_start_value_greater_than_end_value(self):
        stats = self.data_capture.build_stats()
        with self.assertRaises(ValueError) as context:
            self.assertEqual(stats.between(6, 3), 4)

    def test_stats_greater_return_right_value(self):
        stats = self.data_capture.build_stats()
        self.assertEqual(stats.greater(4), 2)

    def test_stats_greater_raise_error_with_wrong_input_value(self):
        stats = self.data_capture.build_stats()
        with self.assertRaises(ValueError) as context:
            self.assertEqual(stats.greater('a'), 2)


class ProgramTestCase(TestCase):

    @patch('builtins.input')
    def test_program_run_with_all_int_values(self, mock_input):
        input_values = (5, 3, 9, 3, 4, 6, 4, 4, 3, 6)
        mock_input.side_effect = input_values
        program = Program()
        program.run()
        self.assertEqual(mock_input.call_count, len(input_values))

    @patch('builtins.input')
    def test_program_run_with_one_wrong_value_raise_error(self, mock_input):
        input_values = ('a', 3, 9, 3, 4, 6, 4, 4, 3, 6)
        mock_input.side_effect = input_values
        program = Program()
        program.run()
        mock_input.assert_called_once()
