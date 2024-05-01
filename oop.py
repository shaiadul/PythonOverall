print(":::: OOP In Python ::::")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def getSalary(self):
        print(f"{self.name} salary is {self.salary}")


shaiadul = Employee("shaiadul", 20000)

try:
    shaiadul.getSalary()
except Exception as e:
    print("Error is: \n", e)