'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - Write a menu driven program to enter two numbers and print the arithmetic operations
a. + b. – c. * d. / e. // f. %.
'''

#***************Code of the Program****************

print("Welcome to the most basic calculater out here!")

# Menu
print("Please select and enter the operation you want to be performed")
print('''
1. Adddition
2. Subtraction
3. Multiplication
4. Float Division
5. Integer Division
6. Modulus
7. Exponentiation 
'''
)


#Operators
oper1 = int(input("Enter your first operand: "))
oper2 = int(input("Enter your second operand(dont put zero for division): "))

print('\n')
choice = int(input("Enter your choice here: "))

#Choice Wise Calculation and Result Display
if (choice == 1):
    print("The result of your Addition is", oper1 + oper2)
elif (choice == 2):
    print("The result of your Subtraction is", oper1 - oper2)
elif (choice == 3):
    print("The result of your Multiplication is", oper1 * oper2)
elif (choice == 4):
    if(oper2==0):
        print("Division by zero not allowed")
    else:
        print("The result of your Float Division is", oper1 / oper2)
elif (choice == 5):
    if(oper2==0):
        print("Division by zero not allowed")
    else:
        print("The result of your Float Division is", oper1 // oper2)
elif (choice == 6):
    print("The result of your Modulus is", oper1 % oper2)
elif (choice == 7):
    print("The result of your Exponentiation is", oper1 ** oper2)
else:
    print("Enter a valid choice")

'''
********* OUTPUT **********
Welcome to the most basic calculater out here!
Please select and enter the operation you want to be performed

1. Adddition
2. Subtraction
3. Multiplication
4. Float Division
5. Integer Division
6. Modulus
7. Exponentiation 

Enter your first operand: 5
Enter your second operand(dont put zero for division): 6


Enter your choice here: 7
The result of your Exponentiation is 15625
'''