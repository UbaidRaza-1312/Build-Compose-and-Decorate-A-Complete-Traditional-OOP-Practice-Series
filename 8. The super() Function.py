class Person:
    def __init__(self, name):
        self.name = name
        print(f"Persom created with the name : {self.name}")


class Teacher(Person):
    def __init__(self, name , subject):
        super().__init__(name)
        self.suject = subject
        print(f"Teacher teacher : {self.suject}")
        

t = Teacher("Ubaid" , "Math")

