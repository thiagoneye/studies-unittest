"""
The implementation of the max_min_diff() function is given.

Modify the implementation of the max_min_diff() function.
By using the assert statement inside this function, add the ability to
check the length of the numbers argument before returning the result.

If the length of the numbers object is 0 raise the AssertionError with message:
- 'The input list cannot be empty.'

Otherwise, it returns the correct result (the difference between
the highest and lowest value for numbers).

In case the module with the solution is run directly, call the
max_min_diff() function passing an empty list.
"""

def max_min_diff(numbers):
    """
    Calculates the difference between the maximum and minimum number
    in the given list.

    :param numbers: A list of numbers.
    :return: The difference between the maximum and minimum number
    in the list.
    :raises ValueError: If the list is empty.
    """
    # Enter your solution here
    assert len(numbers) != 0, "The input list cannot be empty."
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    max_min_diff([])
