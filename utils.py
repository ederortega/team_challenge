"""Utils tools. """


class NumericInputValidatorMixin():
    """Define input validation for numeric types."""

    def valid_int_input(self, value: str) -> int:
        """Validate if an string is an int value.

        Args:
            value (str): value to evaluate

        Raises:
            ValueError: when the input is not a digit

        Returns:
            int: value casted to int
        """
        if isinstance(value, str) and not value.isdigit():
            raise ValueError('Please type a valid int value!')

        return int(value)
