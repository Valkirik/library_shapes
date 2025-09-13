from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = 3.14 * (self.radius ** 2)
        return result


class Triangle(Shape):
    def __init__(self, size_1: int, size_2: int, size_3: int):
        self.size_1 = size_1
        self.size_2 = size_2
        self.size_3 = size_3

    def area(self):
        p = (self.size_1 + self.size_2 + self.size_3) / 2
        result = (p * (p - self.size_1) * (p - self.size_2) * (p - self.size_3)) ** 0.5
        return int(result)

    def checking_pryam(self):
        list_sizes = [self.size_1, self.size_2, self.size_3]
        gipotenuza = max(list_sizes)
        catets = list(filter(lambda x: x != gipotenuza, list_sizes))
        sum_squares_catets = sum(map(lambda x: x ** 2, catets))
        if gipotenuza ** 2 == sum_squares_catets:
            return "Прямоугольный треугольник"
        else:
            return "Не прямоугольный треугольник"
