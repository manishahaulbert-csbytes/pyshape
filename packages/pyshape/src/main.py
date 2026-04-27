import __main__
import shapes


def test_triangle_init():
        # failing test example
        b = 4
        h = 10
        t = shapes.Triangle(base=b, height=h)
        print(f"Triangle area: {t.area()}, Expected: {(b*h)/2}")
        expected = (b*h)/2
        if t.area() != expected:
            print(f"Test FAILED: {t.area()} != {expected}")
        else:
            print("Test PASSED")

def test_triangle_init_new():
        # failing test example
        b = 6
        h = 12
        t = shapes.Triangle(base=b, height=h)
        print(f"Triangle area: {t.area()}, Expected: {(b*h)/2}")
        expected = (b*h)/2
        if t.area() != expected:
            print(f"Test FAILED: {t.area()} != {expected}")
        else:
            print("Test PASSED")

def main():
    print("PyShape Demo - Testing Triangle Calculations")
    print("=" * 50)
    test_triangle_init()
    test_triangle_init_new()


if __name__ == "__main__":
    main()