
# shapes.py -- object oriented shapes
#
# Copyright (c) 2010, A. G. Smith
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


class Shape(object):
    
    def __init__(self, *args, **kwargs):
        return


class Polygon(Shape):

    def __init__(self, base=None, height=None, *args, **kwargs):
        super(Polygon, self).__init__(*args, **kwargs)
        self.base = base
        self.height = height


class Triangle(Polygon):
    
    def __init__(self, *args, **kwargs):
        super(Triangle, self).__init__(*args, **kwargs)
        

    def area(self):
        return self.base * self.height # failing test example
    

class Quadrilateral(Polygon):

    def __init__(self, *args, **kwargs):
        super(Quadrilateral, self).__init__(*args, **kwargs)


class Parallelogram(Quadrilateral):

    def __init__(self, *args, **kwargs):
        super(Parallelogram, self).__init__(*args, **kwargs)

    def area(self):
        return self.base * self.height


class Square(Parallelogram):

    def __init__(self, *args, **kwargs):
        super(Square, self).__init__(*args, **kwargs)

class Rectangle(Parallelogram):  # pragma: no cover

    def __init__(self, *args, **kwargs):  # pragma: no cover
        super(Rectangle, self).__init__(*args, **kwargs)


class Circle(Shape):

    def __init__(self, radius=None, *args, **kwargs):
        super(Circle, self).__init__(*args, **kwargs)
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)
    

class Ellipse(Shape):

    def __init__(self, major_axis=None, minor_axis=None, *args, **kwargs):
        super(Ellipse, self).__init__(*args, **kwargs)
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def area(self):
        import math
        return math.pi * self.major_axis * self.minor_axis

class Ellipse1(Shape):

    def __init__(self, major_axis=None, minor_axis=None, *args, **kwargs):
        super(Ellipse, self).__init__(*args, **kwargs)
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def area(self):
        import math
        return math.pi * self.major_axis * self.minor_axis
    
class Rhombus(Parallelogram):

    def __init__(self, *args, **kwargs):
        super(Rhombus, self).__init__(*args, **kwargs)
        self.diagonal1 = kwargs.get('diagonal1', None)
        self.diagonal2 = kwargs.get('diagonal2', None)

    def area(self):
        return (self.diagonal1 * self.diagonal2) / 2
    