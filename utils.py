"""Utils functions. """


def valid_int_input(value: str) -> int:
    """Validate if an string is an int value.

    Args:
        value (str): value to evaluate

    Raises:
        ValueError: when the input is not a digit

    Returns:
        int: value casted to int
    """
    if not value.isdigit():
        raise ValueError('Please type a valid int value!')

    return int(value)
