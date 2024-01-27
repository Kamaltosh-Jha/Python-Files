'''
Name:- Kamaltosh Jha
Section A Group 1
Title :- Write a Program to find factorial of the entered number using recursion.
Continue till user wants to find he factorial.

'''
#****************Program******************
def factorial(n : int) -> int:
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Welcome to factorial finder")

while True:
    num = int(input("Enter your number "))

    print(f"The factorial of {num} is {factorial(num)}")

    choice = int(input("Do you want to calculate factorial of another number? Enter 1 for Yes, and 0 for No\n"))
    if (choice == 1):
        continue
    else:
        break

print("Thank you and Good Bye!")

'''
#********OUTPUT********
Welcome to factorial finder
Enter your number 1
The factorial of 1 is 1
Do you want to calculate factorial of another number? Enter 1 for Yes, and 0 for No
1
Enter your number 0
The factorial of 0 is 1
Do you want to calculate factorial of another number? Enter 1 for Yes, and 0 for No
1
Enter your number 7
The factorial of 7 is 5040
Do you want to calculate factorial of another number? Enter 1 for Yes, and 0 for No

'''