'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - (a) WAP to input name and output as hello name 
        along with it display the number of characters in your name
        (b)Input any two characteristics and generate # combining the two characteristics
'''
#***************Code of the Program****************
# (a)
print("Welcome to the program")

user_name = input("Enter Your Name Here: ") # a variable to store the name string upon input
print("Hello", user_name); # printing the first part
print("The number of characters in your name is: ", len(user_name)) # printing the number of characters

# (b)
char1 = input("Enter your hobby: ") # first characteristics
char2 = input("Enter your favourite genre: ") # second characteristics
print("Your # is ", "#" + char1[0:3] + char2[0:3]) # output

'''
********* OUTPUT **********
Enter Your Name Here: Kamaltosh
Hello Kamaltosh
The number of characters in your name is:  9
Enter your hobby: Gaming
Enter your favourite genre: Adventure
Your # is  #GamAdv

'''