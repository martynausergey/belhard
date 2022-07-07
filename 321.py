class Rectangle:
    def __init__(self, x: tuple[int, int], y: tuple[int, int]):
        self.x = x
        self.y = y

    def __lenght(self):
        lenght = abs(self.x[0]) + abs(self.y[0])
        height = abs(self.x[1]) + abs(self.y[1])
        return lenght, height

    def perimeter(self) -> int:
        lenght = self.__lenght()
        return sum(lenght) * 2

    def are(self):
        lenght = self.__lenght()
        return lenght[0] * lenght[1]

rectangle = Rectangle(
    x=(-3, 2),
    y=(5, -4)
)
print(rectangle.area())
print(rectangle.perimeter())
