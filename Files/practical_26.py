'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - Write a program in python to plot a pie chart on consumption 
of water in daily life.

'''
#***************Code of the Program****************

print("Welcome to the program")
import matplotlib.pyplot as plt

time_slots=["Morning","Afternoon","Evening","Night"]
water_consumption=[50,20,40,30]
plt.pie(water_consumption,labels=time_slots)
plt.show()

'''
********* OUTPUT **********


'''