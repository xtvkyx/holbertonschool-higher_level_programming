#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not isinstance(value[0], int) or
            not isinstance(value[1], int) or
            value[0] < 0 or
            value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the '#' character."""
        if self.__size == 0:
            print("")
            return

        # Print vertical offset (newlines)
        for _ in range(self.__position[1]):
            print("")

        # Print square rows with leading spaces
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
