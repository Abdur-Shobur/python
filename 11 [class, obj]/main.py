class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"hello i m {self.name}")


p1 = Person('Abdur', 132)
del p1.age
# p1.greet()


# Inheritance
class Animal:
    def speak(self):
        print('Animal Sound')


class Dog(Animal):
    def bark(self):
        print('Dog Barks')


d = Dog()
x = d.speak()
