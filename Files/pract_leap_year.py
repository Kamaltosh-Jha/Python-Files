'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - WAP to find whether a year is leap year or not.
'''

#***************Code of the Program****************
print("Welcome the leap year checker!")

year = int(input("Enter the year you want to check "))

if(year%4 == 0):
    if(year%100 == 0):
        if(year%400 == 0):
            print("It's a leap year!")
        else:
            print("It's not a leap year!")
    else:
        print("It's a leap year!")

else:
    print("It's not a leap year!")

'''
********* OUTPUT **********
1.
Welcome the leap year checker!
Enter the year you want to check 1900
It's not a leap year!
2.
Welcome the leap year checker!
Enter the year you want to check 2000
It's a leap year!
3.
Welcome the leap year checker!
Enter the year you want to check 1904
It's a leap year!
'''