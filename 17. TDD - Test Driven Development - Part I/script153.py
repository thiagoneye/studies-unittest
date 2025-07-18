def sum_even_numbers(numbers):
    even_numbers = [n for n in numbers if n % 2 == 0]
    return sum(even_numbers)


def test_sum_even_numbers():
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12, "[1, 2, 3, 4, 5, 6] failed"
    assert sum_even_numbers([0, 1, 2, 3, 4, 5, 6]) == 12, "[0, 1, 2, 3, 4, 5, 6] failed"
    assert sum_even_numbers([2, 4, 6]) == 12, "[2, 4, 6] failed"
    assert sum_even_numbers([1, 3, 5]) == 0, "[1, 3, 5] failed"
    assert sum_even_numbers([]) == 0, "[] failed"
