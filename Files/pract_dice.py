
'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - 

'''
#***************Code of the Program****************

print("Welcome to the program")
import random as rn
class Dice:
    def __init__(self,sides):
        self.sides=sides
    def roll_dice(self):
        temp=rn.randint(1,self.sides)
        return temp
s=int(input("Input number of sides "))
d1=Dice(s)
print("Roll of the dice with sides "+str(s)+" is "+str(d1.roll_dice()))
'''
********* OUTPUT **********
Input number of sides 10
Roll of the dice with sides 10 is 4

'''