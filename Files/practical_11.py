'''
Name:- Kamaltosh Jha
Section A Group 1
Title :- Write a Program to enter the numbers and to print greatest number using loop.

'''
#****************Program******************
def returnGreatest(numList: list) -> int:
    max = 0
    for i in numList:
        if i >= max:
            max = i
        else:
            continue
    return max

print("Welcome to greatest number finder ")
size = int(input("How many elements do you have? "))
numbersList = []
for i in range(size):
    num = int(input(f"Enter value no. {i+1} : "))
    numbersList.append(num)
print(f"The greatest number out of {numbersList} is ")
print(returnGreatest(numbersList))

'''
#********OUTPUT********
Welcome to greatest number finder 
How many elements do you have? 10
Enter value no. 1 : 323
Enter value no. 2 : 4356
Enter value no. 3 : 4673
Enter value no. 4 : 986 
Enter value no. 5 : 35463
Enter value no. 6 : 475689
Enter value no. 7 : 45867
Enter value no. 8 : 45678
Enter value no. 9 : 8745
Enter value no. 10 : 346578
The greatest number out of [323, 4356, 4673, 986, 35463, 475689, 45867, 45678, 8745, 346578] is
475689

'''