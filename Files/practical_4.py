'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - Write a menu driven Program to reverse the entered numbers and print the sum of digits entered.

'''
#***************Code of the Program****************

print("Welcome to the program")

choice = 1
while choice:
    num = input("Enter your number: ")
    print(f"Your reversed number is: {num[::-1]}")

    sum_of_digits = 0
    for i in num:
        sum_of_digits += int(i)

    print(f"The sum of digits is number is: {sum_of_digits}")

    choice = int(input("Do you want to run the program again? Enter 1 for yes and 0 for no: "))
        

'''
********* OUTPUT **********

Welcome to the program
Enter your number: 12345
Your reversed number is: 54321
The sum of digits is number is: 15
Do you want to run the program again? Enter 1 for yes and 0 for no: 0

'''