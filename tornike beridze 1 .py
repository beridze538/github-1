class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plus(self):
        return self.x + self.y

    def minus(self):
        return self.x - self.y

    def multiple(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y


class Rectangle:
    def __init__(self, width=100, height=150):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def print_info(self):
        return self.width, self.height, self.area(), self.perimeter()

rect = Rectangle()
print(rect.print_info())