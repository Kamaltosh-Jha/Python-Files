'''
Name:- Kamaltosh Jha
Section A Group 1
Title :- Write a Program to check if the entered number is Armstrong or not.

'''
#****************Program******************

class NotArmstrongError(Exception):

    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return(repr(self.value))

print('''
Hello, Welcome to Armstrong Number checker!
Definition :- An Armstrong Number is a number in any base with n number of digits and when each digit is raised to the power n and summed up it makes the original number!, it is also known by the name "Narcissistic number" or "Plus Perfect Number"
Named after Michael F. Armstrong not Neil Armstrong
example:- 153, A three digit Armstrong number can be written as, 
    153 = 1^3 + 5^3 + 3^3
    153 = 1   + 125 + 27
    153 = 153
''')
while(True):
    try:
        # number entered by the user
        number = int(input("Enter your number to check! \n")) 

        # number of digits
        n = len(str(number)) 
        
        sum = 0
        for i in str(number):
            sum += int(i)**n

        if sum != number:
            raise NotArmstrongError(number)

    except ValueError as val_err:
        print("Please enter a number!")
        print(val_err)
        continue
    except NotArmstrongError as arm_err:
        print('''Unfortunately, 
              It is not an Armstrong Number''')
        print("Your number was", arm_err)
    else:
        print("Congratulations")
        print(f"{number} is an Armstrong Number")
    finally:
        print("Check Complete!")
       

    choice = int(input("Do you want to test another number? Enter 1 for Yes, and 0 for No\n"))
    if (choice == 1):
        continue
    else:
        break

print("Thank you and Good Bye!")

'''
#********OUTPUT********
Hello, Welcome to Armstrong Number checker!
Definition :- An Armstrong Number is a number in any base with n number of digits and when each digit is raised to the power n and summed up it makes the original number!, it is also known by the name "Narcissistic number" or "Plus Perfect Number"
Named after Michael F. Armstrong not Neil Armstrong
example:- 153, A three digit Armstrong number can be written as,
    153 = 1^3 + 5^3 + 3^3
    153 = 1   + 125 + 27
    153 = 153

Enter your number to check!
370
Congratulations, 370 is an Armstrong Number
Check Complete!
Do you want to test another number? Enter 1 for Yes, and 0 for No
1
Enter your number to check!
360
Unfortunately, the number you entered is not an Armstrong Number
Your number was 360
Check Complete!
Do you want to test another number? Enter 1 for Yes, and 0 for No
1
Enter your number to check!
abc
Please enter a number!
invalid literal for int() with base 10: 'abc'
Check Complete!
Enter your number to check!
9 
Congratulations, 9 is an Armstrong Number
Check Complete!
Do you want to test another number? Enter 1 for Yes, and 0 for No
0
Thank you and Good Bye!
'''