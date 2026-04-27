#!/usr/bin/env python3
"""
PyMath Demo - Demonstrates the functionality of the pymath library
"""

import sys
import os

# Add the src directory to the path so we can import mathutils
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from mathutils import Vector2D, Statistics, GeometryUtils, NumberTheory


def demo_vectors():
    """Demonstrate vector operations."""
    print("=== Vector2D Demo ===")
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)
    
    print(f"Vector 1: {v1}")
    print(f"Vector 2: {v2}")
    print(f"Magnitude of v1: {v1.magnitude():.2f}")
    print(f"Normalized v1: {v1.normalize()}")
    print(f"Dot product: {v1.dot_product(v2):.2f}")
    print(f"Angle between vectors: {math.degrees(v1.angle_between(v2)):.2f} degrees")
    print(f"Vector addition: {v1 + v2}")
    print()
    print(f"Vector subtraction: {v1 - v2}")
    print(f"Scalar multiplication (v1 * 2): {v1 * 2)}")
    print()
    print("Vector2D demo completed successfully!")
    print()


def demo_statistics():
    """Demonstrate statistical functions."""
    print("=== Statistics Demo ===")
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print(f"Data: {data}")
    print(f"Mean: {Statistics.mean(data):.2f}")
    print(f"Median: {Statistics.median(data):.2f}")
    print(f"Standard deviation: {Statistics.standard_deviation(data):.2f}")
    
    x_data = [1, 2, 3, 4, 5]
    y_data = [2, 4, 6, 8, 10]
    print(f"Correlation coefficient: {Statistics.correlation_coefficient(x_data, y_data):.2f}")
    print()


def demo_geometry():
    """Demonstrate geometry utilities."""
    print("=== Geometry Utilities Demo ===")
    p1 = (0, 0)
    p2 = (3, 4)
    
    print(f"Distance between {p1} and {p2}: {GeometryUtils.distance_between_points(p1, p2):.2f}")
    print(f"Point (2, 2) in circle centered at (0, 0) with radius 3: {GeometryUtils.point_in_circle((2, 2), (0, 0), 3)}")
    
    triangle_vertices = [(0, 0), (4, 0), (2, 3)]
    print(f"Triangle area from vertices {triangle_vertices}: {GeometryUtils.triangle_area_from_vertices(*triangle_vertices):.2f}")
    
    square_vertices = [(0, 0), (2, 0), (2, 2), (0, 2)]
    print(f"Square perimeter: {GeometryUtils.polygon_perimeter(square_vertices):.2f}")
    print()


def demo_number_theory():
    """Demonstrate number theory functions."""
    print("=== Number Theory Demo ===")
    print(f"GCD of 48 and 18: {NumberTheory.gcd(48, 18)}")
    print(f"LCM of 12 and 8: {NumberTheory.lcm(12, 8)}")
    print(f"Is 17 prime? {NumberTheory.is_prime(17)}")
    print(f"Is 15 prime? {NumberTheory.is_prime(15)}")
    print(f"10th Fibonacci number: {NumberTheory.fibonacci(10)}")
    print(f"5! = {NumberTheory.factorial(5)}")
    print()


def main():
    """Main demo function."""
    import math
    globals()['math'] = math  # Make math available for demo_vectors
    
    print("PyMath Library Demo")
    print("=" * 50)
    
    demo_vectors()
    demo_statistics()
    demo_geometry()
    demo_number_theory()
    
    print("Demo completed successfully!")


if __name__ == "__main__":
    main()