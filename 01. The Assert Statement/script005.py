"""
The following rectangle_area() function is given, which 
returns the area of a rectangle (no argument validation).

Assert the following function calls:
- rectangle_area(4, 10)
- rectangle_area(5, 6)

with the appropriate values:
- 40
- 30
"""

def rectangle_area(width: int, height: int) -> int:
    """
    Calculates the area of a rectangle with given width and height.

    :param width: The width of the rectangle.
    :param height: The height of the rectangle.
    :return: The area of the rectangle.
    """
    return width * height

if __name__ == "__main__":
    assert rectangle_area(4, 10) == 40
    assert rectangle_area(5, 6) == 30
