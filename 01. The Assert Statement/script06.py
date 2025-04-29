"""
The rectangle_area() function is given, which returns the
area of a rectangle with additional argument validation.

Assert the following function call:

    rectangle_area('5', '4')

with a value of 20.
"""

def rectangle_area(width: int, height: int) -> int:
    """
    Calculates the area of a rectangle with given width and height.

    :param width: The width of the rectangle.
    :param height: The height of the rectangle.
    :return: The area of the rectangle.
    :raises TypeError: If the width or height is not an integer.
    :raises ValueError: If the width or height is not a positive integer.
    """
    if not isinstance(width, int) or not isinstance(height, int):
        raise TypeError('The width and height must be integers.')
    if width <= 0 or height <= 0:
        raise ValueError(
            'The width and height must be positive integers.'
        )
    return width * height

assert rectangle_area('5', '4')
