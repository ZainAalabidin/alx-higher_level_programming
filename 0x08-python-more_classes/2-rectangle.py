#!/usr/bin/python3
"""1-rectangle, built for project 0x08 task 1.
"""


class Rectangle:
    """At this stage the class creates private instance attributes .

    Args:
        width (int): horizontal dimension of rectangle, defaults to 0.
        height (int): vertical dimension of rectangle, defaults to 0.
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        """__height getter.

        Return:
            __height (int): vertical dimension of rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): vertical dimension of rectangle

        Attributes:
            __height (int): vertical dimension of rectangle.

        Raises:
            TypeError: if value is not an int.
            ValueErroe: if value is less than 0.

        """
        if isinstance(value, int):
            self.__height = value
        else:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """__width getter.

        Return:
            __width (int): horizontal dimension of rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): horizontal dimension of rectangle.

        Attributes:
            __height (int): horizontal dimension of rectangle.

        Raises:
            TypeError: if value is not an int.
            ValueErroe: if value is less than 0.

        """
        if isinstance(value, int):
            self.__width = value
        else:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

    def area(self):
        """Return area of rectangle from the attributes `width` and `height`.

        Attributes:
            __width (int): horizontal dimension of rectangle.
            __height (int): vertical dimension of rectangle.

        Return:
            Area of rectangle self.__width * self.__height

        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter.

        Attributes:
            __width (int): horizontal dimension of rectangle.
            __height (int): vertical dimension of rectangle.

        Returns:
            0 if ether attribute equal to 0.

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
