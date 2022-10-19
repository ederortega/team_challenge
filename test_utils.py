from multiprocessing.sharedctypes import Value
from unittest import TestCase

from utils import NumericInputValidatorMixin


class NumericInputValidatorTestCase(TestCase):
    
    def test_valid_int_input_return_int_with_str_digit_value(self):
        validator = NumericInputValidatorMixin()
        value = validator.valid_int_input('3')
        self.assertIsInstance(value, int)
        self.assertEqual(value, 3)

    def test_valid_int_input_return_int_with_float_value(self):
        validator = NumericInputValidatorMixin()
        value = validator.valid_int_input(3.5)
        self.assertIsInstance(value, int)
        self.assertEqual(value, 3)

    def test_valid_int_input_raise_error_with_wrong_str_value(self):
        validator = NumericInputValidatorMixin()
        with self.assertRaises(ValueError) as context:
            value = validator.valid_int_input('a')
