class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} гавкает"
    
dog = Dog("Шарик")
print(dog.speak())