class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name              
        self._salary = salary        
        self.__ssn = ssn             

    def get_ssn(self):
        return self.__ssn
    
    def set_salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("Salary must be positive in number.")

    def display(self):
        print(f"Name : {self.name}")
        print(f"Salary : {self._salary}")
        print(f"SSN : {self.__ssn}")

class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        super().__init__(name, salary, ssn)
        self.department = department

    def show_manager_info(self):
        print(f"Manager : {self.name}")
        print(f"Department : {self.department}")
        print(f"Protected salary : {self._salary}")
        print(f"Accessing SSN via getter : {self.get_ssn()}")

m = Manager("John", 50000, "1234", "Information Technology")
m.show_manager_info()
m.set_salary(60000)
print("Updated salary (60000):", m._salary)
print("Private SSN via getter:", m.get_ssn())
