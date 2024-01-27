'''
Name:- Kamaltosh Jha
Section A Group 1
Title :-
Write a program to display ASCII code of a character and vice versa.
'''
#****************Program******************
while True:

    print('''Welcome the ASCII Converter!
            Chose your option
            1. Character to ASCII 
            2. ASCII to Character 
            Enter 0 to exit
            ''')
    choice = int(input("Your choice here: "))

    if (choice == 1):
        inp_char = input("Enter your character: ")
        char_to_code = ord(inp_char)
        print(f"The ASCII code for '{inp_char}' is {char_to_code} ")

    elif (choice == 2):
        inp_code = int(input("Enter your ASCII code: "))
        code_to_char = chr(inp_code)
        print(f"The Character for ASCII code {inp_code} is '{code_to_char}' ")

    elif (choice == 0):
        print("Thanks, See ya~")
        exit()
        
    else:
        print("Invalid Input! Please try again")    

'''
#********OUTPUT********
Welcome the ASCII Converter!
            Chose your option
            1. Character to ASCII
            2. ASCII to Character
            Enter 0 to exit

Your choice here: 1
Enter your character: W
The ASCII code for 'W' is 87
Welcome the ASCII Converter!
            Chose your option
            1. Character to ASCII
            2. ASCII to Character
            Enter 0 to exit

Your choice here: 2
Enter your ASCII code: 77
The Character for ASCII code 77 is 'M'
Welcome the ASCII Converter!
            Chose your option
            1. Character to ASCII
            2. ASCII to Character
            Enter 0 to exit

Your choice here: 0
Thanks, See ya~

'''