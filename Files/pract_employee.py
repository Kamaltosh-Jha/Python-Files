'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - 

'''
#***************Code of the Program****************

print("Welcome to the program")
class Employee:
    empcount=101
    def __init__(self, name,designation,salary):
        self.name=name
        self.designation=designation
        self.salary=salary
        self.employeeID="E"+str(Employee.empcount)
        Employee.empcount+=1
    def showdetails(self):
        print("The name of the employee is "+str(self.name))
        print("The designation of the employee is "+str(self.designation))
        print("The salary of the employee is "+str(self.salary))
        print("The Employee ID of the employee is "+str(self.employeeID))
        print()
    @classmethod
    def countemp(cls):
        temp=cls.empcount-101
        return(temp)

emp1 = Employee("John Vicks", "Analyst", 100000)
emp2 = Employee("Barry Alien", "Athelete", 50000)
emp3 = Employee("Bruce Insane", "Officer", 60000)

emp1.showdetails()
emp2.showdetails()
emp3.showdetails()
'''
********* OUTPUT **********

Welcome to the program
The name of the employee is John Vicks
The designation of the employee is Analyst
The salary of the employee is 100000
The Employee ID of the employee is E101

The name of the employee is Barry Alien
The designation of the employee is Athelete
The salary of the employee is 50000
The Employee ID of the employee is E102

The name of the employee is Bruce Insane
The designation of the employee is Officer
The salary of the employee is 60000
The Employee ID of the employee is E103
'''