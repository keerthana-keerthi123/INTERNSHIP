from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # Force child classes to implement

    def sleep(self):
        print("the animal is Sleeping...")  # Common method

# Child classes
class Dog(Animal):
    def sound(self):
        print("the animal is Barking")

class Cat(Animal):
    def sound(self):
        print("the animal is sounding Meow")

class Cow(Animal):
    def sound(self):
        print("the animal is sounding Moo")

# Test
dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
dog.sleep()

cat.sound()
cat.sleep()

cow.sound()
cow.sleep()
