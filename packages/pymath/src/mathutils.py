# mathutils.py -- mathematical utilities
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
from typing import List, Tuple, Union


class Vector2D:
    """A 2D vector class for mathematical operations."""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def magnitude(self) -> float:
        """Calculate the magnitude of the vector."""
        return math.sqrt(self.x**2 + self.y**2)
    
    def normalize(self) -> 'Vector2D':
        """Return a normalized version of the vector."""
        mag = self.magnitude()
        if mag == 0:
            return Vector2D(0, 0)
        return Vector2D(self.x / mag, self.y / mag)
    
    def dot_product(self, other: 'Vector2D') -> float:
        """Calculate the dot product with another vector."""
        return self.x * other.x + self.y * other.y
    
    def angle_between(self, other: 'Vector2D') -> float:
        """Calculate the angle between this vector and another in radians."""
        dot = self.dot_product(other)
        mag_product = self.magnitude() * other.magnitude()
        if mag_product == 0:
            return 0
        return math.acos(max(-1, min(1, dot / mag_product)))
    
    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: float) -> 'Vector2D':
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"


class Statistics:
    """Statistical utility functions."""
    
    @staticmethod
    def mean(values: List[float]) -> float:
        """Calculate the arithmetic mean of a list of values."""
        if not values:
            raise ValueError("Cannot calculate mean of empty list")
        return sum(values) / len(values)
    
    @staticmethod
    def median(values: List[float]) -> float:
        """Calculate the median of a list of values."""
        if not values:
            raise ValueError("Cannot calculate median of empty list")
        sorted_values = sorted(values)
        n = len(sorted_values)
        if n % 2 == 0:
            return (sorted_values[n//2 - 1] + sorted_values[n//2]) / 2
        else:
            return sorted_values[n//2]
    
    @staticmethod
    def standard_deviation(values: List[float]) -> float:
        """Calculate the standard deviation of a list of values."""
        if len(values) < 2:
            raise ValueError("Cannot calculate standard deviation with less than 2 values")
        mean_val = Statistics.mean(values)
        variance = sum((x - mean_val)**2 for x in values) / (len(values) - 1)
        return math.sqrt(variance)
    
    @staticmethod
    def correlation_coefficient(x_values: List[float], y_values: List[float]) -> float:
        """Calculate the Pearson correlation coefficient between two datasets."""
        if len(x_values) != len(y_values) or len(x_values) < 2:
            raise ValueError("Lists must have equal length and at least 2 elements")
        
        mean_x = Statistics.mean(x_values)
        mean_y = Statistics.mean(y_values)
        
        numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_values, y_values))
        sum_sq_x = sum((x - mean_x)**2 for x in x_values)
        sum_sq_y = sum((y - mean_y)**2 for y in y_values)
        
        denominator = math.sqrt(sum_sq_x * sum_sq_y)
        if denominator == 0:
            return 0
        return numerator / denominator


class GeometryUtils:
    """Geometric utility functions that complement the shapes library."""
    
    @staticmethod
    def distance_between_points(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
        """Calculate the Euclidean distance between two points."""
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    
    @staticmethod
    def point_in_circle(point: Tuple[float, float], center: Tuple[float, float], radius: float) -> bool:
        """Check if a point is inside a circle."""
        distance = GeometryUtils.distance_between_points(point, center)
        return distance <= radius
    
    @staticmethod
    def triangle_area_from_vertices(p1: Tuple[float, float], p2: Tuple[float, float], p3: Tuple[float, float]) -> float:
        """Calculate triangle area from three vertices using the cross product method."""
        # Using the shoelace formula
        return abs((p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2)
    
    @staticmethod
    def polygon_perimeter(vertices: List[Tuple[float, float]]) -> float:
        """Calculate the perimeter of a polygon given its vertices."""
        if len(vertices) < 3:
            raise ValueError("Polygon must have at least 3 vertices")
        
        perimeter = 0
        for i in range(len(vertices)):
            next_i = (i + 1) % len(vertices)
            perimeter += GeometryUtils.distance_between_points(vertices[i], vertices[next_i])
        return perimeter


class NumberTheory:
    """Number theory utility functions."""
    
    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Calculate the greatest common divisor using Euclid's algorithm."""
        while b:
            a, b = b, a % b
        return abs(a)
    
    @staticmethod
    def lcm(a: int, b: int) -> int:
        """Calculate the least common multiple."""
        return abs(a * b) // NumberTheory.gcd(a, b) if a and b else 0
    
    @staticmethod
    def is_prime(n: int) -> bool:
        """Check if a number is prime."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def fibonacci(n: int) -> int:
        """Generate the nth Fibonacci number."""
        if n < 0:
            raise ValueError("n must be non-negative")
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    @staticmethod
    def factorial(n: int) -> int:
        """Calculate the factorial of n."""
        if n < 0:
            raise ValueError("n must be non-negative")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result