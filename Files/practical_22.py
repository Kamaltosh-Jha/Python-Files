'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - Write a Program to enter multiple values-based data in 
multiple columns/rows and show that data in python using 
DataFrames and pandas.

'''
#***************Code of the Program****************

print("Welcome to the program")
import pandas as pd 

df = pd.DataFrame(
    {
        "Name" : ["Venti", "Zhongli", "Ei", "Nahida", "Furina"],
        "Vision" : ["Anemo", "Geo", "Electro", "Dendro", "Hydro"],
        "Weapon" : ["Bow", "Polearm", "Polearm", "Catalyst", "Sword"],
        "Region" : ["Monstad", "Liyue", "Inazuma", "Sumeru", "Fontaine"]
    }
)

print("The data frame is")
print(df)

'''
********* OUTPUT **********
The data frame is
      Name   Vision    Weapon    Region
0    Venti    Anemo       Bow   Monstad
1  Zhongli      Geo   Polearm     Liyue
2       Ei  Electro   Polearm   Inazuma
3   Nahida   Dendro  Catalyst    Sumeru
4   Furina    Hydro     Sword  Fontaine

'''