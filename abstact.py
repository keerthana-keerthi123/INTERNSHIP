from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# Child class Car
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with a key.")

# Child class Bike
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started with a kick.")

# Child class Bus
class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine started with a button.")

# Create objects and call start_engine()
vehicle1 = Car()
vehicle2 = Bike()
vehicle3 = Bus()

vehicle1.start_engine()
vehicle2.start_engine()
vehicle3.start_engine()
