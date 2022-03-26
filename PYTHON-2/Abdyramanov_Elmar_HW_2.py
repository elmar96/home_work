import math


class Figure:
    unit = 'см'

    @staticmethod
    def format_number(num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate_area(self):
        raise NotImplementedError('method \'calculate_area\'must be implemented in every child class')

    def info(self):
        raise NotImplementedError('method \'info\'must be implemented in every child class')


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return math.pi * self.__radius ** 2

    def info(self):
        area = self.calculate_area()
        print('Circle radius: {radius}{unit}, area: {area:.2f}{unit}'.format(radius=self.__radius,
                                                                             unit=self.unit,
                                                                             area=area))


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return self.format_number(0.5 * (self.__side_a * self.__side_b))

    def info(self):
        area = self.calculate_area()
        print('RightTriangle side a: {side_a}{unit},side b: {side_b}{side_b},area:{area}{unit}'
              .format(unit=self.unit, side_a=self.__side_a, side_b=self.__side_b, area=area))


list_of_figures = [Circle(6), Circle(10), RightTriangle(6, 3), RightTriangle(9, 5), RightTriangle(8, 7)]
for figure in list_of_figures:
    figure.info()
