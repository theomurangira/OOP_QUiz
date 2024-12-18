# OOP Quiz in Python

This project demonstrates the use of Object-Oriented Programming (OOP) concepts in Python. The quiz consists of two classes, `Point` and `Circle`, showcasing fundamental principles like encapsulation, abstraction, and inheritance.

## Features

- **`Point` Class:**
  - Represents a 2D point with `x` and `y` coordinates.
  - Methods include:
    - Getting and setting coordinates.
    - Calculating the distance between two points.
    - Equality comparison of two points.
    - String representation of a point in the format `(x, y)`.

- **`Circle` Class:**
  - Represents a circle with a center (a `Point` object) and a radius.
  - Methods include:
    - Getting and setting the center and radius.
    - Calculating the area of the circle.
    - Checking if a point lies inside the circle.
    - Equality comparison of two circles.
    - String representation of the circle in the format `Center: (x, y), Radius: r`.

## Requirements

- Python 3.x
- Math library (standard in Python)

## Usage

1. Clone the repository or copy the code.
2. Run the script in a Python environment.
3. Example usage:

```python
# Creating Point instances
origin = Point(0, 0)
p1 = Point(3, 4)
p2 = Point(2, 3)

# Creating Circle instances
c1 = Circle(origin, 4)
c2 = Circle(p1, 3)

# Using class methods
print(c1)               # Output: Center: (0, 0), Radius: 4
print(p1)               # Output: (3, 4)
print(c1.area())        # Output: 50.26548245743669
print(c1.is_in(p1))     # Output: True
print(c2.is_in(p2))     # Output: True
print(c1 == c2)         # Output: False
```

## How It Works

1. **Encapsulation:**
   - Attributes like `x`, `y`, `center`, and `radius` are accessed and modified through getter and setter methods.

2. **Abstraction:**
   - Complex operations like calculating distance, area, or checking point inclusion are hidden behind simple method calls.

3. **Code Reusability:**
   - `Point` class is reused in the `Circle` class as the center.

4. **Polymorphism:**
   - Methods like `__eq__` and `__str__` behave differently based on the object context.

## Project Structure

- `Point`: A class for representing and manipulating points in 2D space.
- `Circle`: A class for representing and manipulating circles in 2D space.

## OOP Concepts Covered

- Class and Object creation
- Instance methods
- Encapsulation with getters and setters
- Method overriding for string representation (`__str__`) and equality comparison (`__eq__`)


