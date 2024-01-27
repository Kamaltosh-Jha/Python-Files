'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - Write a program to compute the roots of the quadratic equation
'''
#***************Code of the Program****************
#Defining Equation
a = float(input("Enter coefficient of x^2 "))
b = float(input("Enter coefficient of x "))
c = float(input("Enter contant coefficient "))

print("Your Equation is: "+ str(a)+"x^2"+"+"+str(b)+"x"+ "+"+str(c))

discriminant = (b**2) - (4*a*c)
root1 = (- b + discriminant**0.5)/(2*a)
root2 = (- b - discriminant**0.5)/(2*a)


if (discriminant == 0):
    print("Both roots are real and equal")
elif (discriminant > 0):
    print("Both roots are real and unequal")
elif (discriminant < 0):
    print("Both roots are complex and unequal")

print("Roots of the equation are ", root1, "and", root2)

'''
********* OUTPUT **********
1.
Enter coefficient of x^2 1
Enter coefficient of x -5
Enter contant coefficient 6
Your Equation is: 1.0x^2+-5.0x+6.0
Both roots are real and unequal
Roots of the equation are  3.0 and 2.0
2.
Enter coefficient of x^2 1
Enter coefficient of x 2
Enter contant coefficient 6
Your Equation is: 1.0x^2+2.0x+6.0
Both roots are complex and unequal
Roots of the equation are  (-0.9999999999999999+2.23606797749979j) and (-1.0000000000000002-2.23606797749979j)
3.
Enter coefficient of x^2 4
Enter coefficient of x -15
Enter contant coefficient 3
Your Equation is: 4.0x^2+-15.0x+3.0
Both roots are real and unequal
Roots of the equation are  3.538016836956259 and 0.2119831630437412
'''