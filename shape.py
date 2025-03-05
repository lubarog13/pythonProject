class Shape:
    id = 1


class Rectangle(Shape):
    def __init__(self):
        self.id = Shape.id
        Shape.id+=1
    def __str__(self):
        return str(self.id) + ":" + "Rectangle"


class Square(Shape):
    def __init__(self):
        self.id = Shape.id
        Shape.id += 1

    def __str__(self):
        return str(self.id) + ":" + "Square"


class Ellipse(Shape):
    def __init__(self):
        self.id = Shape.id
        Shape.id += 1

    def __str__(self):
        return str(self.id) + ":" + "Ellipse"

print(Rectangle(), Ellipse())
