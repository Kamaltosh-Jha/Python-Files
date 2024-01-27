'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - Write a program to plot a bar chart in python to display the 
result of a school for five consecutive years.

'''
#***************Code of the Program****************
import matplotlib.pyplot as plt

print("Welcome to the program")

year=[2019,2020,2021,2022, 2023]
result=[80,90,95.5,92,50]
plt.bar(year, result)
plt.xlabel("Year")
plt.ylabel("Result")
plt.title("ABC School Five Year Results")
plt.show()
'''
********* OUTPUT **********


'''