'''
Name:- Kamaltosh Jha
Section A Group 1
Title :-
WAP that inputs the no. of characters for your password,then it asks for the
no of letters,no of numeric digits, no of special characters to be included.
Then the computer will generate a random password(system generated) for the inputs taken 
a. Not shuffled
b. Shuffled
'''
#****************Program******************
# Importing the random module
import random

# Making The Lists from which characters will be taken
alphabetList = []
numberList = ['0','1','2','3','4','5','6','7','8','9']
characterList = ['*','@','#','&','/','%','_','?']
for i in range(65, 91):
	alphabetList.append(chr(i))
for i in range(97, 123):
	alphabetList.append(chr(i))


pass_len = int(input("Enter the length of password "))	
num_alphabet = int(input("Enter number of alphabets "))
num_numDigit = int(input("Enter number of numeric digits "))
num_specChars = int(input("Enter number of special characters "))

if((num_alphabet+num_numDigit+num_specChars) != pass_len):
	print("invalid sum")
	exit()

passwordList= []

for i in range(num_alphabet):
	passwordList.append(random.choice(alphabetList))
	
for i in range(num_numDigit):
	passwordList.append(random.choice(numberList))
	
for i in range(num_specChars):
	passwordList.append(random.choice(characterList))

password = ""
for i in passwordList:
	password += i

	
shuffled_pass = ""
random.shuffle(passwordList)
for i in passwordList:
	shuffled_pass += i
	
print("(a). Your password is : ", password)
print("(b). Your Shuffled password is : ", shuffled_pass)
	
#********OUTPUT********
'''
Enter the length of password 12
Enter number of alphabets 4
Enter number of numeric digits 4
Enter number of special characters 4
(a). Your password is :  VQng0230__?%
(b). Your Shuffled password is :  n0g3?_%_VQ02

'''