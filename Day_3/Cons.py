class Constructor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
person1 = Constructor("JKD", 30)
person2 = Constructor("Jai", 25)    
person1.display()  
person2.display() 
