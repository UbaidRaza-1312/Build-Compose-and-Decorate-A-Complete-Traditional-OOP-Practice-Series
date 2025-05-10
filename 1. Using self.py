class student :
    def __init__(self , name , marks):
        self.name = name
        self.mark = marks


    def display(self):
        print(f"Student name : {self.name}")
        print(f"Marks : {self.mark}")


student1 = student("ubaid raza" , 99)
student1.display()