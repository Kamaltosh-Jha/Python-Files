'''
Name:- Kamaltosh Jha
Section A Group 1
Title :- Write a menu driven Program to determine EOQ using various inventory models.

'''
#****************Program******************
import math

def basic_eoq(lmbda, A, IC):
    eoq = math.sqrt((2 * lmbda * A) / IC)
    return eoq

def epq(lmbda, A, IC, psi):
    eoq = math.sqrt(((2 * lmbda * A)*psi)/ (IC * (psi - lmbda)))
    return eoq

def eoq_with_shortages(lmbda, A, IC, pi):
    eoq = math.sqrt(((2 * lmbda * A)*(IC + pi))/ (IC * pi))
    return eoq

def eoq_with_shortages_and_finite_production(lmbda, A, IC, pi, psi):
    eoq = math.sqrt((2 * lmbda * A * (IC + pi) * psi) / (IC * (psi - lmbda) * pi))
    return eoq
choice = 1
while repeat:
    print("Welcome to Inventory Management - Economic Order Quantity (EOQ) Calculator")
    print("1. Basic EOQ Model")
    print("2. EOQ Model with Quantity Discounts")
    print("3. EOQ Model with Shortages")
    print("4. EOQ Model with Shortages and Finite Production Rate")
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        demand = float(input("Enter annual demand: "))
        ordering_cost = float(input("Enter ordering cost per order: "))
        holding_cost = float(input("Enter holding cost per unit: "))
        result = basic_eoq(demand, ordering_cost, holding_cost)
        print(f"The Economic Order Quantity (EOQ) using Basic EOQ Model is: {result}")

    elif choice == 2:
        demand = float(input("Enter annual demand: "))
        ordering_cost = float(input("Enter ordering cost per order: "))
        holding_cost = float(input("Enter holding cost per unit: "))
        production_rate = float(input("Enter production rate "))
        result = epq(demand, ordering_cost, holding_cost, production_rate)
        print(f"The Economic Production Quantity (EPQ) is: {result}")

    elif choice == 3:
        demand = float(input("Enter annual demand: "))
        ordering_cost = float(input("Enter ordering cost per order: "))
        holding_cost = float(input("Enter holding cost per unit: "))
        shortage_cost = float(input("Enter shortage cost per unit per year: "))
        result = eoq_with_shortages(demand, ordering_cost, holding_cost, shortage_cost)
        print(f"The Economic Order Quantity (EOQ) with Shortages is: {result}")

    elif choice == 4:
        demand = float(input("Enter annual demand: "))
        ordering_cost = float(input("Enter ordering cost per order: "))
        production_rate = float(input("Enter production rate "))
        holding_cost = float(input("Enter holding cost per unit: "))
        shortage_cost = float(input("Enter shortage cost per unit per year: "))
        result = eoq_with_shortages_and_finite_production(demand, ordering_cost, holding_cost, shortage_cost, production_rate)
        print(f"The Economic Order Quantity (EOQ) with Shortages and Finite Production is: {result}")

    else:
        print("Invalid choice. Please enter a valid option.")


    repeat = int(input("Do you want to calculate another model? Enter 1 for yes and 0 for no "))

'''
#********OUTPUT********
Welcome to Inventory Management - Economic Order Quantity (EOQ) Calculator

1. Basic EOQ Model
2. EOQ Model with Quantity Discounts
3. EOQ Model with Shortages
4. EOQ Model with Shortages and Finite Production Rate
Enter your choice (1-4): 1
Enter annual demand: 2940
Enter ordering cost per order: 7.5
Enter holding cost per unit: 2.25
The Economic Order Quantity (EOQ) using Basic EOQ Model is: 140.0
Do you want to calculate another model? Enter 1 for yes and 0 for no 1 


Welcome to Inventory Management - Economic Order Quantity (EOQ) Calculator
1. Basic EOQ Model
2. EOQ Model with Quantity Discounts
3. EOQ Model with Shortages
4. EOQ Model with Shortages and Finite Production Rate
Enter your choice (1-4): 2
Enter annual demand: 2940
Enter ordering cost per order: 7.5
Enter holding cost per unit: 2.25
Enter production rate 9999999
The Economic Production Quantity (EPQ) is: 140.02058454106097
Do you want to calculate another model? Enter 1 for yes and 0 for no 1    


Welcome to Inventory Management - Economic Order Quantity (EOQ) Calculator
1. Basic EOQ Model
2. EOQ Model with Quantity Discounts
3. EOQ Model with Shortages
4. EOQ Model with Shortages and Finite Production Rate
Enter your choice (1-4): 3
Enter annual demand: 2940
Enter ordering cost per order: 7.5
Enter holding cost per unit: 2.25
Enter shortage cost per unit per year: 9999999
The Economic Order Quantity (EOQ) with Shortages is: 140.0000157500007    
Do you want to calculate another model? Enter 1 for yes and 0 for no 1 


Welcome to Inventory Management - Economic Order Quantity (EOQ) Calculator1. Basic EOQ Model
2. EOQ Model with Quantity Discounts
3. EOQ Model with Shortages
4. EOQ Model with Shortages and Finite Production Rate
Enter your choice (1-4): 4
Enter annual demand: 2940
Enter ordering cost per order: 7.5
Enter production rate 9999999
Enter holding cost per unit: 2.25
Enter shortage cost per unit per year: 9999999
The Economic Order Quantity (EOQ) with Shortages and Finite Production is: 140.02060029337744
Do you want to calculate another model? Enter 1 for yes and 0 for no 0

'''