class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

dog1 = Dog("Lucky" , "Aidi")
dog1.bark()