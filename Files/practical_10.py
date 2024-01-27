'''
Name:- Kamaltosh Jha
Section A Group 1
Title :- Write a Program to enter the number of terms and to print the Fibonacci Series.
0 1 1  2  3  5 
'''
#****************Program******************
def fibonacciTerms(n : int) -> None:
    first = 0;
    second = 1;
    fib_list = [0, 1]
    if n <= 2:
        print("This is the smallest list of Fibonacci series")
        print(fib_list)
        return
    for i in range(3, n+1):
        sum = first + second 
        fib_list.append(sum)
        first = second
        second = sum
    print("The Fibonacci Series is ")
    print(fib_list)




print("Welcome to Fibonacci Printer")


num = int(input("Enter number of terms "))

fibonacciTerms(num)



print("Thank you and Good Bye!")
'''
#********OUTPUT********
Welcome to Fibonacci Printer
Enter number of terms 10
The Fibonacci Series is
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
Thank you and Good Bye!

Welcome to Fibonacci Printer
Enter number of terms 1
This is the smallest list of Fibonacci series
[0, 1]
Thank you and Good Bye!
'''