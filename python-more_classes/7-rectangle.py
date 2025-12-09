#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0
    print_symbol = "#"  # Public class attribute

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = str(self.print_symbol)
        rect_lines = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(rect_lines)

    def __repr__(self):
        """Return recreate-able string representation."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
