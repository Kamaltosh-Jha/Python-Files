'''
Name:- Kamaltosh Jha
Section A Group 1
Title :- Write a Program to enter the string and to check if it's palindrome or not using loop.

'''
#****************Program******************
def reverseString(input_string : str) -> str:
    i = len(input_string)
    output_string = ""
    while (i):
        output_string += input_string[i-1]
        i-=1
    return output_string

test_string = input("Enter your string ")
if (len(test_string) == 0):
    print("Empty string is always a palindrome")
    exit()
reversed_string = reverseString(test_string)

if reversed_string == test_string:
    print("Yes, It is a palindrome")
else:
    print("No, It is not a palindrome")

'''
#********OUTPUT********
Enter your string racecar
Yes, It is a palindrome

Enter your string racist
No, It is not a palindrome
'''
