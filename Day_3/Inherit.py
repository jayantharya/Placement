class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed=breed
    def speak(self):
        print(f"{self.name} says Woof!")
class Cat(Animal):
    def __init__(self, name, color):
        print("Initializing Cat")
        super().__init__(name)

    def speak(self):
        print(f"{self.name} says Meow!")
dog1 = Dog("Buddy", "Golden Retriever")
cat1 = Cat("Whiskers", "Tabby")
dog1.speak()  
cat1.speak()  
