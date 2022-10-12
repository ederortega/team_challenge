"""
Module for Data capturing and stats generation.

Define DataCapture class to take data inputs and generate Stats.
Define Stats class for query stats information.
"""
from multiprocessing.sharedctypes import Value
from utils import valid_int_input


class Stats():
    """Define the methods to query stats information from data."""
    
    COUNT = 'count'
    CUMULATIVE = 'cumulative'

    def __init__(self, dict_stats: dict, num_elements: int) -> None:
        self.dict_stats = dict_stats
        self.num_elements = num_elements

    def less(self, value: int) -> int:
        """Returns the number of elements less than the actual value.

        Args:
            value (int): value to evaluate

        Returns:
            int: number of elements less than value
        """
        return self.dict_stats[value][self.CUMULATIVE]

    def greater(self, value: int) -> int:
        """Returns the number of elements greater than the actual value.

        Args:
            value (int): value to evaluate

        Returns:
            int: number of elements greater than value
        """
        return self.num_elements - self.dict_stats[value][self.CUMULATIVE] - 1

    def between(self, start: int, end: int) -> int:
        """Rerturns the number of elements between start and end inclusive.

        Args:
            start (int): start value
            end (int): end value

        Returns:
            int: number of elements
        """
        return self.dict_stats[end][self.CUMULATIVE] - self.dict_stats[start][self.CUMULATIVE] + 1


class DataCapture():
    """Class to take data inputs and generate Stats.
    
    Define the dict structure for further stats generation.
    """

    def __init__(self) -> None:
        self.elements = {}

    def add(self, value: int):
        """Add a new element.

        Args:
            value (int): value to add.
        """
        self.elements[value] = self.elements.get(value, 0) + 1

    def build_stats(self) -> Stats:
        """Build the stats from actual data enhancing the dict structure.

        Returns:
            Stats: Stats object with stats information
        """
        stat_structure = {}
        cumulative = 0
        for key in sorted(self.elements.keys()):
            stat_structure[key] = {
                Stats.COUNT: self.elements[key], 
                Stats.CUMULATIVE: cumulative
            }
            cumulative += self.elements[key]
        return Stats(stat_structure, cumulative)

if __name__ == '__main__':
    try:
        
        data_capture = DataCapture()
        number_of_data = valid_int_input(input('Please type the number of data to read: '))
        for index in range(number_of_data):
            data = valid_int_input(input(f'type data {index}: '))
            data_capture.add(int(data))
        
        stats = data_capture.build_stats()
        less = valid_int_input(input('Type value to test less option: '))
        greater = valid_int_input(input('Type value to test greate option: '))
        start = valid_int_input(input('Type start value to test between option: '))
        end = valid_int_input(input('Type end value to test between option: '))
        print(' Stats resume '.center(100, '='))
        print('_' * 100)
        print(f'Less: result ({stats.less(less)}) with input ({less})')
        print(f'Greater: result ({stats.greater(greater)}) with input ({greater})')
        print(f'Between: result ({stats.between(start, end)}) with input ({start}, {end})')
        print('_' * 100)
    except ValueError as e:
        print(e)
