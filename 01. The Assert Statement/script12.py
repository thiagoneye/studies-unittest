"""
Suppose you have the function to find the maximum and minimum numbers in the given list.

This function finds the maximum and minimum numbers in a list by iterating through the list and updating the maximum and minimum variables as necessary.

Implement the test_find_max_min() function that tests the find_max_min() function.

Use assert statements five different inputs:
- [1, 2, 3, 4, 5]
- [10, 5, 7, 3, 8]
- [-1, -2, -3, -4, -5]
- [0]
- []
"""

def find_max_min(numbers: list) -> tuple:
    """
    Finds the maximum and minimum values in the given list.

    :param numbers: The list of numbers.
    :return: A tuple containing the maximum and minimum values.
    :raises ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("List is empty")

    maximum = minimum = numbers[0]

    for number in numbers[1:]:
        if number > maximum:
            maximum = number
        elif number < minimum:
            minimum = number

    return maximum, minimum 

def test_find_max_min():
    assert find_max_min([1, 2, 3, 4, 5]) == (5, 1)
    assert find_max_min([10, 5, 7, 3, 8]) == (10, 3)
    assert find_max_min([-1, -2, -3, -4, -5]) == (-1, -5)
    assert find_max_min([0]) == (0, 0)
    
    try:
        find_max_min([])
        assert False
    except ValueError:
        pass

if __name__ == '__main__':
    test_find_max_min()
