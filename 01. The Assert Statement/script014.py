"""
Suppose you have the median calculation function.

This function takes a list of numbers as input and calculates the median.

It first sorts the list, and then determines whether the length of the list is even or odd.

If the length is even, it returns the average of the middle two numbers.

If the length is odd, it returns the middle number.

Implement the test_calculate_median() function that tests the calculate_median() function.

Use assert statements five different inputs:
- [1, 2, 3] -> 2
- [4, 5, 6, 7] -> 5.5
- [2, 1, 3] -> 2
- [0, 0, 0, 0] -> 0
- [] -> ValueError
"""

def calculate_median(numbers: list) -> float:
    """
    Calculates the median value of the given list of numbers.

    :param numbers: The list of numbers.
    :return: The median value.
    :raises ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("List is empty")
    sorted_nums = sorted(numbers)
    length = len(sorted_nums)

    if length % 2 == 0:
        return (
            sorted_nums[length // 2 - 1] + sorted_nums[length // 2]
        ) / 2
    else:
        return sorted_nums[length // 2]

def test_calculate_median():
    assert calculate_median([1, 2, 3]) == 2
    assert calculate_median([4, 5, 6, 7]) == 5.5
    assert calculate_median([2, 1, 3]) == 2
    assert calculate_median([0, 0, 0, 0]) == 0
    try:
        calculate_median([])
        assert False
    except ValueError:
        pass

if __name__ == '__main__':
    test_calculate_median()
