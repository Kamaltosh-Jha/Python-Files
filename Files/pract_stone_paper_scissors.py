'''
Name:- Kamaltosh Jha
Section A Group 1
Title :-
1.Wap to play stone, paper, scissors with computer
'''
#****************Program******************
# Importing the random module
import random
items = ('Stone', 'Paper', 'Scissor')
print("Welcome to the original, old school and retro Stone Paper Scissors")
print("Hello Player")
print('''
Choose from the following options 
1. Stone
2. Paper
3. Scissors
''')
comp_choice = random.choice(items)
choice = int(input("What do you chose? : "))
user_choice = items[choice-1]
print("You chose, ", user_choice)	
print("Computer chose, ", comp_choice)

# Winner Decision
if (user_choice == items[0] and comp_choice == items[0]):
	print("Tie, No One Wins")
elif (user_choice == items[0] and comp_choice == items[1]):
	print("Computer Wins")
elif (user_choice == items[0] and comp_choice == items[2]):
	print("Player Wins")


elif (user_choice == items[1] and comp_choice == items[0]):
	print("Player Wins")
elif (user_choice == items[1] and comp_choice == items[1]):
	print("Tie, No One Wins")
elif (user_choice == items[1] and comp_choice == items[2]):
	print("Computer Wins")
	

elif (user_choice == items[2] and comp_choice == items[0]):
	print("Computer Wins")
elif (user_choice == items[2] and comp_choice == items[1]):
	print("Player Wins")
elif (user_choice == items[2] and comp_choice == items[2]):
	print("Tie, No One Wins")




#********OUTPUT********
'''
Welcome to the original, old school and retro Stone Paper Scissors
Hello Player

Choose from the following options
1. Stone
2. Paper
3. Scissors

What do you chose? : 1
You chose,  Stone
Computer chose,  Scissor
Player Wins

'''