'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - Write a menu driven Program to enter the number and print 
whether the number is
a. odd or even
b. prime.

'''
#***************Code of the Program****************
def is_prime(num):
    if num == 2 or num == 3:
        return True
    else:
        for i in range(2, int((num**0.5)+1)):
            if num%i==0:
                return False
        return True

print("Welcome to the program")
choice = 1
while choice:
    print("Enter 1 to check whether number is odd or even")
    print("Enter 2 to check whether number is prime or not")
    n=int(input())
    num=int(input("Enter the number "))
    
    if n==1:
        if (num%2==0):
            print("Number is even")
        else:
            print("Number is odd")

    else:
        if is_prime(num):
            print("Yes it is a prime number")
        else:
            print("No it is not a prime number")
            



    choice = int(input("Do you want to run the program again? Enter 1 for yes and 0 for no: "))

'''
********* OUTPUT **********

Welcome to the program
Enter 1 to check whether number is odd or even
Enter 2 to check whether number is prime or not
1
Enter the number 4567
Number is odd
Do you want to run the program again? Enter 1 for yes and 0 for no: 1
Enter 1 to check whether number is odd or even
Enter 2 to check whether number is prime or not
2
Enter the number 4567
Yes it is a prime number
Do you want to run the program again? Enter 1 for yes and 0 for no: 0

'''