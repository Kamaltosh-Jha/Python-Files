'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - Write a program to enter height and weight of user in metres and kg respectively and calculate BMI and according to the BMI slab print the condition
'''

#****************Program****************

print("Welcome to the most basic calculater out here!")

#Inputs
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in Kgs "))

#bmi calculating formula
bmi = weight/((height)**2)
print("Your BMI is:", bmi)

# BMI Division Slab selector
if (bmi<18.5):
    print("Your BMI lies in the slab of Underweight")
elif (bmi>=18.5 and bmi < 25):
    print("Your BMI lies in the slab of Normal")
elif (bmi>=25 and bmi < 30):
    print("Your BMI lies in the slab of Slightly Overweight")
elif (bmi>=30 and bmi < 35):
    print("Your BMI lies in the slab of Obese")
elif (bmi>=35):
    print("Your BMI lies in the slab of Clinically Obese")

# BMI Division Slab
print("Here is the BMI division Slab")
print('''
    BMI               Condition
Below 18.5           Underweight
Between 18.5 and 25  Normal
Between 25 and 30    Slightly Overweight
Between 30 and 35    Obese
Above 35             Clinically Obese
''')

'''
********* OUTPUT **********
1.
Welcome to the most basic calculater out here!
Enter your height in meters: 1.8
Enter your weight in Kgs 76
Your BMI is: 23.456790123456788
Your BMI lies in the slab of Normal
Here is the BMI division Slab

    BMI               Condition
Below 18.5           Underweight
Between 18.5 and 25  Normal
Between 25 and 30    Slightly Overweight
Between 30 and 35    Obese
Above 35             Clinically Obese

2.
Welcome to the most basic calculater out here!
Enter your height in meters: 1.75
Enter your weight in Kgs 70
Your BMI is: 22.857142857142858
Your BMI lies in the slab of Normal
Here is the BMI division Slab

    BMI               Condition
Below 18.5           Underweight
Between 18.5 and 25  Normal
Between 25 and 30    Slightly Overweight
Between 30 and 35    Obese
Above 35             Clinically Obese

'''