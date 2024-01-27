'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - WAP to find the maximum of 3 entered numbers
'''

#***************Code of the Program****************
#Inputing the numbers
a = int(input("Enter a "))
b = int(input("Enter b "))
c = int(input("Enter c "))

if (a > b and a > c):
    print("Number a is largest")
elif (b > a and b > c):
    print("Number b is largest")
elif (c > a and c > b):
    print("Number c is largest")
elif (a == b and a > c):
    print("Number a and b are equally the largest")
elif (b == c and c > a):
    print("Number b and c are equally the largest")
elif (a == c and a > b):
    print("Number a and c are equally the largest")
else:
    print("They are all equal")
'''
********* OUTPUT **********
1.
Enter a 5
Enter b 6
Enter c 5
b is largest

2.
Enter a 6
Enter b 4
Enter c 6
a and c are equally the largest

3.
Enter a 6
Enter b 6
Enter c 6
They are all equal
'''