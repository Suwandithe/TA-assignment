# Encapsulation: Using classes to bundle data and methods that work on the data
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # To be overridden in subclasses


# Inheritance: Creating a new class by using existing class properties and methods
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# Abstraction: Hiding the implementation details and showing only the necessary features
class Shape:
    def area(self):
        pass  # To be overridden in subclasses


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Polymorphism: Ability to use a single interface for different data types
def animal_speak(animal):
    return animal.speak()


def calculate_area(shape):
    return shape.area()


# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(animal_speak(dog))  # Output: Buddy says Woof!
print(animal_speak(cat))  # Output: Whiskers says Meow!

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(calculate_area(circle))  # Output: 78.5
print(calculate_area(rectangle))  # Output: 24