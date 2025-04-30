"""
You have the greatest common divisor (GCD) function using the Euclidean algorithm.

Use assert statements to test this function with four different inputs:
- 8, 12 -> 4
- 17, 23 -> 1
- 40, 60 -> 20
- 0, 5 -> 5
"""

def gcd(a: int, b: int) -> int:
    """
    Calculates the greatest common divisor of two integers.

    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of the two integers.
    """
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    assert gcd(8, 12) == 4
    assert gcd(17, 23) == 1
    assert gcd(40, 60) == 20
    assert gcd(0, 5) == 5
