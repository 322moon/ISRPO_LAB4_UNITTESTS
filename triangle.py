<<<<<<< HEAD
import unittest


class TriangleTestCase(unittest.TestCase):

    def test_zero_area(self):
        res = area(0, 10)
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_triangle_area_1(self):
        res = area(10, 100)
        self.assertEqual(res, 500)

    def test_triangle_area_2(self):
        res = area(7, 5)
        self.assertEqual(res, 17.5)

    def test_triangle_perimeter_1(self):
        res = perimeter(6, 8, 10)
        self.assertEqual(res, 24)

    def test_triangle_perimeter_2(self):
        res = perimeter(45, 54, 90)
        self.assertEqual(res, 189)


def area(a, h):
    return a * h / 2


def perimeter(a, b, c):
    return a + b + c
if __name__ == "__main__":
    unittest.main()
=======
import unittest

class TriangleTestCase(unittest.TestCase):

    def test_zero_area(self):
        res = area(0,10)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0,0,0)
        self.assertEqual(res, 0)

    def test_triangle_area_1(self):
        res = area(10,100)
        self.assertEqual(res, 500)
        
    def test_triangle_area_2(self):
        res = area(7,5)
        self.assertEqual(res, 17.5)

    def test_triangle_perimeter_1(self):
        res = perimeter(6,8,10)
        self.assertEqual(res, 24)
    
    def test_triangle_perimeter_2(self):
        res = perimeter(-45, -54, 90)
        self.assertEqual(res, 189)


def area(a, h):
    return a * h / 2

def perimeter(a, b, c):
    return a + b + c
>>>>>>> b33dd628256fdd0e31053b0d20873b90b2f09b40
