import pytest
from triangle_module import *


def test_classify_by_sides():
    triangle1 = Triangle(3, 4, 5)
    triangle2 = Triangle(2, 2, 2)
    triangle3 = Triangle(2, 2, 3)
    triangle_invalid = Triangle(1, 2, 3)

    assert triangle1.classify_by_sides() == "Разносторонний треугольник"
    assert triangle2.classify_by_sides() == "Равносторонний треугольник"
    assert triangle3.classify_by_sides() == "Равнобедренный треугольник"
    assert triangle_invalid.classify_by_sides() == "Неверные данные"


def test_classify_by_angles():
    triangle1 = Triangle(3, 4, 5)
    triangle2 = Triangle(5, 5, 5)
    triangle3 = Triangle(6, 6, 10)
    triangle_invalid = Triangle(1, 2, 3)

if __name__ == '__main__':
    pytest.main()

