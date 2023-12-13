# Inheritance notes

# Base Class
class Animal:
    def __init__(self):
        self.num_eyes = 2  # Attribute: number of eyes (Encapsulation: wrapping data in class)

    def breathe(self):
        print("Inhale, exhale.")  # Base method for breathing (Encapsulation: wrapping methods in class)


# Derived Class
class Fish(Animal):  # Fish inherits from Animal (Inheritance)
    def __init__(self):
        super().__init__()  # Initialize the base class to inherit its attributes
        # Additional attributes specific to Fish can be added here

    def breathe(self):
        super().breathe()  # Call the breathe method from the base class (Animal)
        print("Doing this under water.")  # Extending the breathe method for Fish
        # Demonstrates Polymorphism: Method overriding to change behavior in derived class

    # @staticmethod  # make it into static instead of Instance Method by also removing the "self" from swim method
    def swim(self):
        print("Moving in water.")  # Method specific to Fish


# Creating an instance of Fish
nemo = Fish()
nemo.swim()
nemo.breathe()  # Calls the overridden breathe method in the Fish class
print(nemo.num_eyes)


# This example demonstrates:
# 1. Inheritance: How a derived class (Fish) inherits properties and methods from a base class (Animal).
# 2. Polymorphism: Method 'breathe' behaves differently in Animal (base class) and Fish (derived class).
# 3. Encapsulation: Animal and Fish classes encapsulate their data and methods, defining their behavior.
# 4. Use of super(): To call methods from the base class in the derived class, especially in overriding scenarios.
