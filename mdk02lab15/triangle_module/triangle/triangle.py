import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_valid_triangle(self):

        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return False
        return True

    def classify_by_sides(self):
        if not self.is_valid_triangle():
            return "Неверные данные"
        if self.a == self.b == self.c:
            return "Равносторонний треугольник"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "Равнобедренный треугольник"
        else:
            return "Разносторонний треугольник"

    def classify_by_angles(self):
        if not self.is_valid_triangle():
            return "Неверные данные"

        sides = sorted([self.a, self.b, self.c])
        if sides[0] ** 2 + sides[1] ** 2 > sides[2] ** 2:
            return "Остроугольный треугольник"
        elif sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
            return "Прямоугольный треугольник"
        else:
            return "Тупоугольный треугольник"

    def calculate_area(self):
        if not self.is_valid_triangle():
            return "Невозможно вычислить площадь из-за неверных данных"

        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return round(area, 2)


if __name__ == "__main__":
    try:
        a = float(input("Введите сторону a: "))
        b = float(input("Введите сторону b: "))
        c = float(input("Введите сторону c: "))

        triangle = Triangle(a, b, c)

        if triangle.is_valid_triangle():
            print(f"Тип треугольника по сторонам: {triangle.classify_by_sides()}")
            print(f"Тип треугольника по углам: {triangle.classify_by_angles()}")
            print(f"Площадь треугольника: {triangle.calculate_area()}")
        else:
            print("Введены неверные данные. Убедитесь, что длины сторон корректны.")
    except ValueError:
        print("Ошибка ввода. Введите числовые значения.")
