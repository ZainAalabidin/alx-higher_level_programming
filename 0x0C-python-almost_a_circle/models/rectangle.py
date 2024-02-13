#!/usr/bin/python3
""" Module class Rectangle """

from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer".format(x))
        elif x < 0:
            raise ValueError("x must be >= 0".format(x))

        else:
            self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer".format(y))
        elif y < 0:
            raise ValueError("y must be >= 0".format(y))
        else:
            self.__y = y

    def area(self):
        """return the area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """display the rectangle"""
        if self.__y and self.__x == 0:
            for _ in range(self.__height):
                print("#" * self.__width)
        else:
            for x in range(self.__y):
                print()
            for x in range(self.__height):
                print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """special method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """update method"""
        if len(args) > 0:
            self.id = args[0] if len(args) > 0 else self.id
            self.__width = args[1] if len(args) > 1 else self.__width
            self.__height = args[2] if len(args) > 2 else self.__height
            self.__x = args[3] if len(args) > 3 else self.__x
            self.__y = args[4] if len(args) > 4 else self.__y

        for key, value in kwargs.items():
            self.id = value if key == "id" else self.id
            self.__width = value if key == "width" else self.__width
            self.__height = value if key == "height" else self.__height
            self.__x = value if key == "x" else self.__x
            self.__y = value if key == "y" else self.__y

    def to_dictionary(self):
        """return dictionary with prop"""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width,
        }
