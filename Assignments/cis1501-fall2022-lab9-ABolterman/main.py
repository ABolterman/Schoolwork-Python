# Write a class Rectangle with private attributes for length and width,
#   an init method that accepts length and width
#   functions for getting length, width, perimeter, and area
#
# Write a class Square that inherits from Rectangle, write an init method that accepts an argument for length

class Rectangle:
    def __init__(self, length, width=-5):
        self._length = length
        if width == -5:
            width = length
        self._width = width

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def get_perimeter(self):
        perimeter = 2 * (self._width + self._length)
        return perimeter

    def get_area(self):
        area = self._width * self._length
        return area


class Square(Rectangle):
    def __init__(self, length):
        Rectangle.__init__(self, length)



rect_2x3 = Rectangle(2, 3)
print(rect_2x3.get_area())
print(rect_2x3.get_perimeter())
square_2x2 = Square(2)
print(square_2x2.get_perimeter())
print(square_2x2.get_area())
