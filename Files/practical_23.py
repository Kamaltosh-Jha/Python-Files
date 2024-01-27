'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - WAP in python to perform various statistical measures using 
pandas.

'''
#***************Code of the Program****************

print("Welcome to the program")
import pandas as pd 

df = pd.DataFrame(
    {
        "Name" : ["Venti", "Zhongli", "Ei", "Nahida", "Furina"],
        "Vision" : ["Anemo", "Geo", "Electro", "Dendro", "Hydro"],
        "Weapon" : ["Bow", "Polearm", "Polearm", "Catalyst", "Sword"],
        "Region" : ["Monstad", "Liyue", "Inazuma", "Sumeru", "Fontaine"], 
        "Power" : [70, 100, 90, 80, 60]
    }
)


print(df["Power"].describe())


'''
********* OUTPUT **********
Welcome to the program
count      5.000000
mean      80.000000
std       15.811388
min       60.000000
25%       70.000000
50%       80.000000
75%       90.000000
max      100.000000
Name: Power, dtype: float64

'''