from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def fuel_type(self):
        pass
    def drive(self):
        print("driving.")
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")
    def fuel_type(self):
        print("petrol.")
class ElectricCar(Vehicle):
    def start_engine(self):
        print("Electric: slient start.")
    def fuel_type(self):
        print("Electric.")
c=Car()
c.start_engine()
c.drive()
