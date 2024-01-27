'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - WAP to imitate treasure hunt game
'''

#***************Code of the Program****************
import time

print("Welcome to the Treasure Hunt Game!")
time.sleep(4)
print('''
Game Instructions
1. This is an adventure game and is based on alphabetic key inputs from the user where the player is in a magical forest and is seeking to find the treasure hidden is the depth of this forest. Your companion Paimon is with you to guide you!! All the best
2. To move right you have to enter r, for left enter l, for going forward enter f, game will exit if anything else is pressed.
3. You will start from a point where you have three ways to go right left and forward.
4. Sometimes some paths are blocked by monsters or wild beasts so the entry their is forbidden and if players enter there Traveller will have to fight and defeat the monster and return home, so no treasure.
5. If you keep moving eventually you will reach to the treasure that was hidden.
6. There will be different maps soon, but for now there is only one.
Enjoy!!!
''')
time.sleep(10)
playername = (input("Enter your nickname to start playing "))
time.sleep(2)

#The illusion of free choice
print("After taking your equipments and with your best friend and companion Paimon you are walking into the magical forest but suddenly you hear something")
print()
time.sleep(4)
print('Strange Voice: "Traveler! .... You are not supposed to be here, this is a very dangerous place. I suggest you to turn back. Otherwise you will meet your fate here"')
print()
time.sleep(3)
print('''Paimon: "Wh...where did that come from??.. I think we need to be careful ahead. Don't loose your guard '''+playername+" !!")
print()
time.sleep(5)
print()
print("You see three ways ahead!")
print()
p_input = input("Where do you want to go? ")
if(p_input=="l"):
    print("You go to left opening of the pathway")
    print()
elif(p_input=="r"):
    print("You go to right opening of the pathway")
    print()
elif(p_input=="f"):
    print("You go to forward opening of the pathway")
    print()
else:
    print("You decide to not go further and return home with no treasure, How sad!. Paimon is very upset")
    print()
    time.sleep(3)
    print("Thank You for Playing, See You~!")
    print()
    time.sleep(10)
    exit()
time.sleep(2)
print("As you walked there, suddenly a huge swarm of bats came from the darkness of the forest and pass across you")
print()
time.sleep(2)
print('''Paimon: "Aaagh!..This place is scary. Paimon was gonna faint out."''')
print()
time.sleep(3)
print('''Strange Voice: "You did not listen traveler!... this isn't a place for picnic, leave now and never come back.''')
print()
time.sleep(2)
print('''Paimon: "The voice is even scary, lets go home please!!. Wait!, but we are here for treasure, lets take that then go home, hehe~"''')
print()
time.sleep(2)
print('''Paimon is really into treasures.''')
print()
time.sleep(2)
print("After walking for a while you see some light at the end of the path and after going through, you again see three pathways")
print()
time.sleep(3)
print('''Paimon: "I think if we keep choosing the correct pathways we can reach to the treasure soon. Let's go traveler!"''')
print()
time.sleep(4)
print("You walk through a brigde that crosses a lake, the water of the lake seems as clean as mirror. You don't see any further pathways to go")
print()
time.sleep(3)
print("While you were trying to look for some hints, Paimon gets an idea!")
time.sleep(3)
print('''Out of curiosity, Paimon loudly says facing towards the brink of the lake, "Mirror! Oh Mirror! answer us away, where should be our next way"''')
time.sleep(4)
print("As Paimon finished, suddenly a tree fell in front of you and cleares the pathway into the forest deeper")
time.sleep(3)
print('''Paimon: "Woah! That was not just any mere coincidence. This place is really something else"''')
time.sleep(3)
print("The pathway takes you to yet another three choices for your next path")
time.sleep(4)
p_input = input("Where do you want to go? ")
time.sleep(4)

# The actual start of the journey
if(p_input == "l"):
    print("You decide to go left")
    print()
    time.sleep(3)
    print("Suddenly a Hilichurl Appears out of the bushes, you defeat it and return home without any treasure. Paimon is very sad")
    print()
    time.sleep(10)
    exit()
elif(p_input == "r"):
    print("You decide to go right")
    print()
    time.sleep(3)
    print("You find a ClockWork MeKa guarding the area, you decide not to get into trouble and return home without any treasure. No Treasure for Paimon.")
    print()
    time.sleep(10)
    exit()
elif(p_input == "f"):
    print("You decide not to change direction and go straight further into the forest")
    print()
    time.sleep(5)  
else:
    print("You decide to not go further and return home with no treasure, How sad!. Paimon is very upset")
    print()
    time.sleep(3)
    print("Thank You for Playing, See You~!")
    print()
    time.sleep(10)
    exit()

# The turning point
print("After walking all through the day you decide to place a campfire and take rest.")
time.sleep(5)
print("You take a good nap after an exhaustive day")
time.sleep(4)
print("The next day...")
time.sleep(3)
print("The sun rises again and you wake up to continue your journey")
time.sleep(3)
print("You notice that Paimon is not there, you hastly look around but she is nowhere to be found.")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(5)
print('Strange Voice: "Traveler, I warned you...You will never see your friend again."')
print()
time.sleep(5)
print("You rush towards the source of the voice....")
print()
time.sleep(4)
print("With all your strength you sprint through the forest and see a strange temple")
print()
time.sleep(4)
print("The doors of the temple are open and some light coming from the inside can be seen")
print()
time.sleep(3)
print("With the strong grip of your sword, you enter the temple....")
print()
time.sleep(4)
print("A mystic beast appears at a distance ahead of you")
print()
time.sleep(3)
print("It is a magical beast with the features resembling that of a lion, with golden fur and blue eyes")
print()
time.sleep(3)
print("You are moving further, The beast stops you and says")
print()
time.sleep(2)
print('''Mystical Beast: Traveller, so you are here. You are really stubborn just like your sibling. I know you are looking for your friend."''')
print()
time.sleep(3)
print('''You say to the lion, "So you are the one who was telling us to go back! Who are you and Where is Paimon, I won't ask again!"''')
print()
time.sleep(3)
print("Mystical Beast: I am Craxon, the last descendent of the Divine Beasts. I have been guarding this forest for centuries. Your friend has been captured by the curse of this forest")
print()
time.sleep(3)
print("The beast explains the situation to you, It shows you two gigantic gates with some spell cast on them. It seems only with the help of magic it can be opened")
print()
time.sleep(5)
print('''Mystical Beast: According to the curse, "Your destiny here awaits, behind the shadow of the cursed gates. You are to choose what you desire, with a sacrifice the treasure you will acquire"''')
print()
time.sleep(5)
print("You have now two choices ahead")
print("Mystical Beast: The door on the left leads you to the treasure. For which you adventured through the forest")
print()
time.sleep(5)
print("Mystical Beast: The door on the right leads you to the success, you will become the greatest adventurer, your life will be spent hearing appraises. A life of a king")
print()
time.sleep(2)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
p_input = input("What is your choice traveller? ")

# The final chapter 
if(p_input == "l"):
    print("You decide to go left")
    print()
    time.sleep(3)
    print("You recieve the treasure. You have all the wealth that would last forever")
    print()
    time.sleep(10)
    exit()
elif(p_input == "r"):
    print("You decide to go right")
    print()
    time.sleep(3)
    print("You are famous now. Every person on the continent praises your strength and your might, you are their hero.")
    print()
    time.sleep(10)
    exit()
elif(p_input == "f"):
    print("You turn your sword towards the beast, ready to fight")
    print()
    time.sleep(5)  
    print('''"Mystic Beast: "I see, come forth traveller, show me how far you will go for your companion"''')
    print()
    time.sleep(5)
    print("You fight the Mystic Lion with all your strength, The beast is barely able to keep up, it fights you but it seems weak to be able to fight")
    print()
    time.sleep(5)
    print("You defeat the beast, it lies on the ground. While fighting the beast you realised the beast was never intended to win")
    print()
    time.sleep(5)
    print("Mystic Beast: You are strong traveller, and with that you truly acknowledge your friendship. All the best for your future journeys.....")
    print()
    time.sleep(5)
    print("The beast fades away out of thin air, a flash appears and suddenly you realised you were dreaming. You wake up and find Paimon still Sleeping in the camp.")
    print("You are not able to tell what actually happened")
    print()
    time.sleep(5)
    print("You wake up Paimon, you come out of your camp site and notice a huge treasure chest with a note on it.")
    print()
    time.sleep(5)
    print('''"The note says, "This is for the mighty, blonde traveller and the best companion"''')
    print()
    time.sleep(3)
    print(''''"Paimon: "Yay!!.. It's a treasure.. And the note also says that the treasure is for us. Let's go traveller, we will buy all the dishes from the city restaurant, Paimon is really hungry."''')
    print()
    time.sleep(5)
    print("You both return to the city to celebrate")
    print()
    time.sleep(5)
    print("That was the end of the story, thank you for playing!")
    end = input("Enter 0 to exit ")
    if (end=='0'):
        exit()
else:
    print("You can only choose out of the given options, try again!")
    print()
    time.sleep(3)
    print("Thank You for Playing, See You~!")
    print()
    time.sleep(10)
    exit()

'''
********* OUTPUT **********
Welcome to the Treasure Hunt Game!

Game Instructions
1. This is an adventure game and is based on alphabetic key inputs from the user where the player is in a magical forest and is seeking to find the treasure hidden is the depth of this forest. Your companion Paimon is with you to guide you!! All the best
2. To move right you have to enter r, for left enter l, for going forward enter f, game will exit if anything else is pressed.
3. You will start from a point where you have three ways to go right left and forward.
4. Sometimes some paths are blocked by monsters or wild beasts so the entry their is forbidden and if players enter there Traveller will have to fight and defeat the monster and return home, so no treasure.
5. If you keep moving eventually you will reach to the treasure that was hidden.
6. There will be different maps soon, but for now there is only one.
Enjoy!!!

Enter your nickname to start playing bennetto
After taking your equipments and with your best friend and companion Paimon you are walking into the magical forest but suddenly you hear something

Strange Voice: "Traveler! .... You are not supposed to be here, this is a very dangerous place. I suggest you to turn back. Otherwise you will meet your fate here"

Paimon: "Wh...where did that come from??.. I think we need to be careful ahead. Don't loose your guard bennetto !!


You see three ways ahead!

Where do you want to go? l
You go to left opening of the pathway

As you walked there, suddenly a huge swarm of bats came from the darkness of the forest and pass across you

Paimon: "Aaagh!..This place is scary. Paimon was gonna faint out."

Strange Voice: "You did not listen traveler!... this isn't a place for picnic, leave now and never come back.

Paimon: "The voice is even scary, lets go home please!!. Wait!, but we are here for treasure, lets take that then go home, hehe~"

Paimon is really into treasures.

After walking for a while you see some light at the end of the path and after going through, you again see three pathways

Paimon: "I think if we keep choosing the correct pathways we can reach to the treasure soon. Let's go traveler!"

You walk through a brigde that crosses a lake, the water of the lake seems as clean as mirror. You don't see any further pathways to go

While you were trying to look for some hints, Paimon gets an idea!
Out of curiosity, Paimon loudly says facing towards the brink of the lake, "Mirror! Oh Mirror! answer us away, where should be our next way"
As Paimon finished, suddenly a tree fell in front of you and cleares the pathway into the forest deeper
Paimon: "Woah! That was not just any mere coincidence. This place is really something else"
The pathway takes you to yet another three choices for your next path
Where do you want to go? f
You decide not to change direction and go straight further into the forest

After walking all through the day you decide to place a campfire and take rest.
You take a good nap after an exhaustive day
The next day...
The sun rises again and you wake up to continue your journey
You notice that Paimon is not there, you hastly look around but she is nowhere to be found.
.
.
.
.
Strange Voice: "Traveler, I warned you...You will never see your friend again."

You rush towards the source of the voice....

With all your strength you sprint through the forest and see a strange temple

The doors of the temple are open and some light coming from the inside can be seen

With the strong grip of your sword, you enter the temple....

A mystic beast appears at a distance ahead of you

It is a magical beast with the features resembling that of a lion, with golden fur and blue eyes

You are moving further, The beast stops you and says

Mystical Beast: Traveller, so you are here. You are really stubborn just like your sibling. I know you are looking for your friend."

You say to the lion, "So you are the one who was telling us to go back! Who are you and Where is Paimon, I won't ask again!"

Mystical Beast: I am Craxon, the last descendent of the Divine Beasts. I have been guarding this forest for centuries. Your friend has been captured by the curse of this forest

The beast explains the situation to you, It shows you two gigantic gates with some spell cast on them. It seems only with the help of magic it can be opened

Mystical Beast: According to the curse, "Your destiny here awaits, behind the shadow of the cursed gates. You are to choose what you desire, with a sacrifice the treasure you will acquire"

You have now two choices ahead
Mystical Beast: The door on the left leads you to the treasure. For which you adventured through the forest

Mystical Beast: The door on the right leads you to the success, you will become the greatest adventurer, your life will be spent hearing appraises. A life of a king

.
.
.
What is your choice traveller? f
You turn your sword towards the beast, ready to fight

"Mystic Beast: "I see, come forth traveller, show me how far you will go for your companion"

You fight the Mystic Lion with all your strength, The beast is barely able to keep up, it fights you but it seems weak to be able to fight

You defeat the beast, it lies on the ground. While fighting the beast you realised the beast was never intended to win

Mystic Beast: You are strong traveller, and with that you truly acknowledge your friendship. All the best for your future journeys.....

The beast fades away out of thin air, a flash appears and suddenly you realised you were dreaming. You wake up and find Paimon still Sleeping in the camp.
You are not able to tell what actually happened

You wake up Paimon, you come out of your camp site and notice a huge treasure chest with a note on it.

"The note says, "This is for the mighty, blonde traveller and the best companion"

'"Paimon: "Yay!!.. It's a treasure.. And the note also says that the treasure is for us. Let's go traveller, we will buy all the dishes from the city restaurant, Paimon is really hungry."        

You both return to the city to celebrate

That was the end of the story, thank you for playing!
Enter 0 to exit 0
'''