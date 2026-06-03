class Dog:
    sepecies = "Canis familiaris"
    def bark(self):
        return "Woof!"
    



dog1 = Dog()
dog2 = Dog()
print(dog1.sepecies)  # Output: Canis familiaris
#print(dog2.sepecies)  # Output: Canis familiaris
print(dog1.bark())  # Output: Woof!
print(dog2.bark())  # Output: Woof!