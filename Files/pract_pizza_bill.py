'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - WAP to generate bill for pizza shop depending on user preference for S M L one extra topping charge seperately and extra charges for cheese burst edition 
'''
#***************Code of the Program****************
small_pizza_price = 149
medium_pizza_price = 249
large_pizza_price = 299
extra_topping_charges = 30
cheese_burst_charges = 50

bill_name = input("Enter your name please... \n")
bill_amount = 0

print("Welcome to Los Polos Hermanos Pizzas")
print("So, you have selected the cottage cheese pizza. What will be the size? S - small, M - medium, L - large")
pizza_size = input()
if (pizza_size == "s" or pizza_size == "S"):
    bill_amount += small_pizza_price
elif (pizza_size == "m" or pizza_size == "M"):
    bill_amount += medium_pizza_price
elif (pizza_size == "l" or pizza_size == "L"):
    bill_amount += large_pizza_price
else:
    print("Invalid Entry, Please try again!")
print()

print("Alright, Great Choice, do you want extra toppings?, Y - yes, anything else for no")
topping = input()
if (topping == "y" or topping == "Y"):
    bill_amount += extra_topping_charges

print("Very well, do you want a cheese burst condition?, Y - yes, anything else for no")
cheese_burst = input()
if (cheese_burst == "y" or cheese_burst == "Y"):
    bill_amount += cheese_burst_charges

print ("Okay, your final bill amount is", bill_amount, "Rs")
print("Thank You and Have a great day!")

'''
********* OUTPUT **********
Enter your name please... 
kamal
Welcome to Los Polos Hermanos Pizzas
So, you have selected the cottage cheese pizza. What will be the size? S - small, M - medium, L - large
m

Alright, Great Choice, do you want extra toppings?, Y - yes, anything else for no
n
Very well, do you want a cheese burst condition?, Y - yes, anything else for no
y
Okay, your final bill amount is 299 Rs
Thank You and Have a great day!
'''