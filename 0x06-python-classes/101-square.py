#!/usr/bin/python3
"""Defines the Square class."""


class Square:
    """Represents a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new instance of the Square class."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Compute the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)

    def __str__(self):
        """Return a string representation of the square."""
        result = ""
        if self.__size == 0:
            result += "\n"
        else:
            for _ in range(self.__position[1]):
                result += "\n"
            for _ in range(self.__size):
                result += ' ' * self.__position[0] + '#' * self.__size + "\n"
        return result[:-1]  # Remove the trailing newline


# Example usage
if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
