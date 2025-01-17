
# * super() = Function used in a child class to call methods from a parent class (superclass).
# *           Allows you to extend the functionality of the inherited methods


class Shape:
    def __init__(self, color, filled) -> None:
        self.color = color
        self.filled = filled

    def describe(self): 
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)

        self.radius = radius

    def describe(self):
        super().describe()
        print(f"it is a circle with an area of {3.14 * self.radius * self.radius} cm^2")

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width 
        self.height = height


circle = Circle(color="red", filled=True, radius=5)


print(circle.color)
print(circle.filled)
print(f"{circle.radius} cm")


circle.describe()