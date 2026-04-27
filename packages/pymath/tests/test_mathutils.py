# test_mathutils.py -- tests for mathutils.py
#
# Copyright (c) 2026, PyMath Contributors
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import math
import unittest
import sys
import os

# Add the src directory to the path so we can import mathutils
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from mathutils import Vector2D, Statistics, GeometryUtils, NumberTheory


class TestVector2D(unittest.TestCase):
    
    def test_vector_creation(self):
        v = Vector2D(3, 4)
        self.assertEqual(v.x, 3)
        self.assertEqual(v.y, 4)
    
    def test_magnitude(self):
        v = Vector2D(3, 4)
        self.assertEqual(v.magnitude(), 5)  # 3-4-5 triangle
    
    def test_normalize(self):
        v = Vector2D(3, 4)
        normalized = v.normalize()
        self.assertAlmostEqual(normalized.magnitude(), 1.0, places=6)
    
    def test_normalize_zero_vector(self):
        v = Vector2D(0, 0)
        normalized = v.normalize()
        self.assertEqual(normalized.x, 0)
        self.assertEqual(normalized.y, 0)
    
    def test_dot_product(self):
        v1 = Vector2D(1, 2)
        v2 = Vector2D(3, 4)
        self.assertEqual(v1.dot_product(v2), 11)  # 1*3 + 2*4 = 11
    
    def test_angle_between(self):
        v1 = Vector2D(1, 0)
        v2 = Vector2D(0, 1)
        angle = v1.angle_between(v2)
        self.assertAlmostEqual(angle, math.pi/2, places=6)  # 90 degrees
    
    def test_vector_addition(self):
        v1 = Vector2D(1, 2)
        v2 = Vector2D(3, 4)
        result = v1 + v2
        self.assertEqual(result.x, 4)
        self.assertEqual(result.y, 6)
    
    def test_vector_subtraction(self):
        v1 = Vector2D(5, 7)
        v2 = Vector2D(3, 4)
        result = v1 - v2
        self.assertEqual(result.x, 2)
        self.assertEqual(result.y, 3)
    
    def test_scalar_multiplication(self):
        v = Vector2D(2, 3)
        result = v * 2.5
        self.assertEqual(result.x, 5)
        self.assertEqual(result.y, 7.5)


class TestStatistics(unittest.TestCase):
    
    def test_mean(self):
        values = [1, 2, 3, 4, 5]
        self.assertEqual(Statistics.mean(values), 3)
    
    def test_mean_empty_list(self):
        with self.assertRaises(ValueError):
            Statistics.mean([])
    
    def test_median_odd_length(self):
        values = [1, 3, 2, 5, 4]
        self.assertEqual(Statistics.median(values), 3)
    
    def test_median_even_length(self):
        values = [1, 2, 3, 4]
        self.assertEqual(Statistics.median(values), 2.5)
    
    def test_median_empty_list(self):
        with self.assertRaises(ValueError):
            Statistics.median([])
    
    def test_standard_deviation(self):
        values = [1, 2, 3, 4, 5]
        std_dev = Statistics.standard_deviation(values)
        self.assertAlmostEqual(std_dev, 1.5811, places=3)
    
    def test_standard_deviation_insufficient_data(self):
        with self.assertRaises(ValueError):
            Statistics.standard_deviation([1])
    
    def test_correlation_coefficient_perfect_positive(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        corr = Statistics.correlation_coefficient(x, y)
        self.assertAlmostEqual(corr, 1.0, places=6)
    
    def test_correlation_coefficient_perfect_negative(self):
        x = [1, 2, 3, 4, 5]
        y = [5, 4, 3, 2, 1]
        corr = Statistics.correlation_coefficient(x, y)
        self.assertAlmostEqual(corr, -1.0, places=6)
    
    def test_correlation_coefficient_unequal_lengths(self):
        x = [1, 2, 3]
        y = [1, 2]
        with self.assertRaises(ValueError):
            Statistics.correlation_coefficient(x, y)


class TestGeometryUtils(unittest.TestCase):
    
    def test_distance_between_points(self):
        p1 = (0, 0)
        p2 = (3, 4)
        distance = GeometryUtils.distance_between_points(p1, p2)
        self.assertEqual(distance, 5)  # 3-4-5 triangle
    
    def test_point_in_circle_inside(self):
        point = (1, 1)
        center = (0, 0)
        radius = 2
        self.assertTrue(GeometryUtils.point_in_circle(point, center, radius))
    
    def test_point_in_circle_outside(self):
        point = (3, 4)
        center = (0, 0)
        radius = 2
        self.assertFalse(GeometryUtils.point_in_circle(point, center, radius))
    
    def test_point_in_circle_on_boundary(self):
        point = (2, 0)
        center = (0, 0)
        radius = 2
        self.assertTrue(GeometryUtils.point_in_circle(point, center, radius))
    
    def test_triangle_area_from_vertices(self):
        p1 = (0, 0)
        p2 = (4, 0)
        p3 = (2, 3)
        area = GeometryUtils.triangle_area_from_vertices(p1, p2, p3)
        self.assertEqual(area, 6)  # base=4, height=3, area=12/2=6
    
    def test_polygon_perimeter_square(self):
        vertices = [(0, 0), (2, 0), (2, 2), (0, 2)]
        perimeter = GeometryUtils.polygon_perimeter(vertices)
        self.assertEqual(perimeter, 8)  # 4 sides of length 2
    
    def test_polygon_perimeter_insufficient_vertices(self):
        vertices = [(0, 0), (1, 1)]
        with self.assertRaises(ValueError):
            GeometryUtils.polygon_perimeter(vertices)


class TestNumberTheory(unittest.TestCase):
    
    def test_gcd_basic(self):
        self.assertEqual(NumberTheory.gcd(48, 18), 6)
        self.assertEqual(NumberTheory.gcd(17, 13), 1)
    
    def test_gcd_with_zero(self):
        self.assertEqual(NumberTheory.gcd(5, 0), 5)
        self.assertEqual(NumberTheory.gcd(0, 7), 7)
    
    def test_gcd_negative_numbers(self):
        self.assertEqual(NumberTheory.gcd(-48, 18), 6)
        self.assertEqual(NumberTheory.gcd(48, -18), 6)
    
    def test_lcm_basic(self):
        self.assertEqual(NumberTheory.lcm(12, 8), 24)
        self.assertEqual(NumberTheory.lcm(5, 7), 35)
    
    def test_lcm_with_zero(self):
        self.assertEqual(NumberTheory.lcm(5, 0), 0)
        self.assertEqual(NumberTheory.lcm(0, 7), 0)
    
    def test_is_prime_small_primes(self):
        self.assertTrue(NumberTheory.is_prime(2))
        self.assertTrue(NumberTheory.is_prime(3))
        self.assertTrue(NumberTheory.is_prime(5))
        self.assertTrue(NumberTheory.is_prime(7))
        self.assertTrue(NumberTheory.is_prime(11))
    
    def test_is_prime_composite_numbers(self):
        self.assertFalse(NumberTheory.is_prime(4))
        self.assertFalse(NumberTheory.is_prime(6))
        self.assertFalse(NumberTheory.is_prime(8))
        self.assertFalse(NumberTheory.is_prime(9))
        self.assertFalse(NumberTheory.is_prime(15))
    
    def test_is_prime_edge_cases(self):
        self.assertFalse(NumberTheory.is_prime(0))
        self.assertFalse(NumberTheory.is_prime(1))
        self.assertFalse(NumberTheory.is_prime(-5))
    
    def test_fibonacci_basic(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, expected_val in enumerate(expected):
            self.assertEqual(NumberTheory.fibonacci(i), expected_val)
    
    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            NumberTheory.fibonacci(-1)
    
    def test_factorial_basic(self):
        self.assertEqual(NumberTheory.factorial(0), 1)
        self.assertEqual(NumberTheory.factorial(1), 1)
        self.assertEqual(NumberTheory.factorial(5), 120)
    
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            NumberTheory.factorial(-1)


if __name__ == '__main__':
    unittest.main()