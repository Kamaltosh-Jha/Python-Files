'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - Write a Program to implement Inheritance. Create a class Employee inherit two classes Manager and Clerk from Employee.

'''
#***************Code of the Program****************
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_details(self):
        return f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}"


class Clerk(Employee):
    def __init__(self, name, salary, role):
        super().__init__(name, salary)
        self.role = role

    def display_details(self):
        return f"Name: {self.name}, Salary: {self.salary}, Role: {self.role}"



manager = Manager("Finn Ischer", 9999, "HR")
clerk = Clerk("Ben Stokes", 4444, "Attendant")

print(manager.display_details()) 
print(clerk.display_details())   



'''
********* OUTPUT **********
Name: Finn Ischer, Salary: 9999, Department: HR
Name: Ben Stokes, Salary: 4444, Role: Attendant

'''