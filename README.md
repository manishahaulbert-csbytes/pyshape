# PyShape Monorepo

A Python monorepo containing mathematical and geometric libraries for computational tasks.

## 📦 Packages

### `pyshape` - Geometric Shapes Library
A Python library for object-oriented geometric shapes with area calculations.

**Features:**
- Shape hierarchy (Shape → Polygon → Triangle, Quadrilateral, etc.)
- Circle and Ellipse implementations
- Area calculations for various shapes
- Comprehensive test coverage

**Location:** `packages/pyshape/`

**Classes:**
- `Shape` (base class)
- `Polygon`, `Triangle`, `Quadrilateral`, `Parallelogram`
- `Square`, `Rectangle`, `Rhombus`
- `Circle`, `Ellipse`

### `pymath` - Mathematical Utilities Library
A comprehensive mathematical utilities library providing vector operations, statistics, geometry utilities, and number theory functions.

**Features:**
- 2D Vector operations (magnitude, normalization, dot product, angles)
- Statistical functions (mean, median, standard deviation, correlation)
- Geometry utilities (distance, point-in-circle, polygon operations)
- Number theory (GCD, LCM, prime checking, Fibonacci, factorial)

**Location:** `packages/pymath/`

**Modules:**
- `Vector2D` - 2D vector mathematics
- `Statistics` - Statistical analysis functions
- `GeometryUtils` - Geometric utility functions
- `NumberTheory` - Number theory operations

## 🚀 Quick Start

### Installing Dependencies

From the root of the monorepo:

```bash
# Install core dependencies
pip install -e .

# Install development dependencies
pip install -e .[dev]
```

### Running Individual Projects

**PyShape (Shapes Library):**
```bash
cd packages/pyshape
python src/main.py
python -m pytest tests/
```

**PyMath (Math Utilities):**
```bash
cd packages/pymath
python src/main.py
python -m pytest tests/
```

### Running All Tests

From the root directory:
```bash
# Run all tests across packages
python -m pytest

# Run tests with coverage
python -m pytest --cov=packages --cov-report=html

# Generate coverage XML report
coverage run -m pytest packages/*/tests/
coverage xml -o coverage.xml
```

## 📁 Project Structure

```
pyshape-monorepo/
├── packages/
│   ├── pyshape/           # Geometric shapes library
│   │   ├── src/
│   │   │   ├── __init__.py
│   │   │   ├── shapes.py   # Shape classes and area calculations
│   │   │   └── main.py     # Demo and examples
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   ├── conftest.py
│   │   │   └── test_shapes.py
│   │   └── pyproject.toml
│   └── pymath/            # Mathematical utilities library  
│       ├── src/
│       │   ├── __init__.py
│       │   ├── mathutils.py  # Vector, stats, geometry, number theory
│       │   └── main.py       # Demo and examples
│       ├── tests/
│       │   ├── __init__.py
│       │   ├── conftest.py
│       │   └── test_mathutils.py
│       └── pyproject.toml
├── pyproject.toml         # Monorepo configuration
├── pytest.ini            # Pytest configuration
├── README.md
└── coverage.xml           # Test coverage reports
```

## 🧪 Development

### Running Tests

Each package has its own test suite:

```bash
# Run pyshape tests
python -m pytest packages/pyshape/tests/

# Run pymath tests  
python -m pytest packages/pymath/tests/

# Run all tests
python -m pytest
```

### Code Quality

The monorepo is configured with development tools:

```bash
# Format code with black
black packages/

# Lint with flake8
flake8 packages/

# Type checking with mypy
mypy packages/
```

## 📝 Examples

### PyShape Usage

```python
from packages.pyshape.src.shapes import Circle, Triangle, Rectangle

# Create shapes
circle = Circle(radius=5)
triangle = Triangle(base=4, height=3)
rectangle = Rectangle(base=6, height=4)

# Calculate areas
print(f"Circle area: {circle.area()}")           # π × 5² ≈ 78.54
print(f"Triangle area: {triangle.area()}")       # 4 × 3 = 12 (intentional bug)
print(f"Rectangle area: {rectangle.area()}")     # 6 × 4 = 24
```

### PyMath Usage

```python
from packages.pymath.src.mathutils import Vector2D, Statistics, NumberTheory

# Vector operations
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
print(f"Magnitude: {v1.magnitude()}")            # 5.0
print(f"Dot product: {v1.dot_product(v2)}")      # 11.0

# Statistics
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Mean: {Statistics.mean(data)}")          # 5.5
print(f"Std Dev: {Statistics.standard_deviation(data)}")

# Number theory
print(f"Is 17 prime? {NumberTheory.is_prime(17)}")      # True
print(f"GCD(48, 18): {NumberTheory.gcd(48, 18)}")       # 6
```

## 🤝 Contributing

1. Each package should maintain its own tests and documentation
2. Follow the established code style (Black formatting)
3. Add tests for new functionality
4. Update this README for major changes

## 📄 License

Copyright (c) 2010-2026, A. G. Smith and PyMath Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.