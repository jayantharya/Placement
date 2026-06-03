class Animal:
    def __init__(self,name):
        self.name=name
        
    def eat(self):
        return f"{self.name} is eating"
    
    def speak(self):
        return f"{self.name} is some sound"
    
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def speak(self):
        return f"{self.name} says:woof!"
class cat(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color=color
    def speak(self):
        return f"{self.name} meows:meow!"
Dog =Dog("Tommy","Golden retriever") 
cat=cat("whitey","tobby") 
print(Dog.eat())
print(Dog.speak())   
print(cat.eat()) 
print(cat.speak())