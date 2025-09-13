import unittest
from library_shapes.library import Circle, Triangle

class MyTests(unittest.TestCase):
    def test_create_circle(self):
        circle = Circle(5)
        self.assertIsInstance(circle, Circle)
        self.assertEqual(circle.radius, 5)

    def test_square(self):
        circle = Circle(5)
        result = circle.area()
        self.assertEqual(result, 78.5)

    def test_create_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertIsInstance(triangle, Triangle)
        self.assertEqual(triangle.size_1, 3)
        self.assertEqual(triangle.size_2, 4)
        self.assertEqual(triangle.size_3, 5)

    def test_square_triangle(self):
        triangle = Triangle(3, 4, 5)
        result = triangle.area()
        self.assertEqual(result, 6)

    def test_checking_pryam(self):
        triangle = Triangle(3, 4, 5)
        result = triangle.checking_pryam()
        self.assertEqual(result, "Прямоугольный треугольник")


if __name__ == "__main__":
    unittest.main()