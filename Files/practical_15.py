'''
Name:- Kamaltosh Jha
Section A Group 1
Title :- Write a python function sin(x,n) to calculate the value of sin(x) using its Taylor series expansion up to n terms.

'''
#****************Program******************
import math

def sin(x, n):
    sine = 0
    for i in range(n):
        coef = (-1) ** i
        power = 2 * i + 1
        term = (coef * (x ** power) )/ (math.factorial(power))
        sine += term
    return sine

num_of_terms = int(input("Enter number of terms "))
angle = eval((input("Enter angle in radians ")))

result = sin(angle, num_of_terms)

print("The result is", result)

'''
#********OUTPUT********
Enter number of terms 10
Enter angle in radians 3.14/2
The result is 0.9999996829318345
'''