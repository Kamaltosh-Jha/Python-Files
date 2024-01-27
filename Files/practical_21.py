'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - Write a program to perform read and write operation with .csv 
file

'''
#***************Code of the Program****************

print("Welcome to the program")
import pandas as pd 
df = pd.read_csv('file_21_read.csv') 
print("The data in the csv file is: ")
print(df)

df_write = pd.DataFrame(
    {
        "Name" : ["Venti", "Zhongli", "Ei", "Nahida", "Furina"],
        "Vision" : ["Anemo", "Geo", "Electro", "Dendro", "Hydro"],
        "Weapon" : ["Bow", "Polearm", "Polearm", "Catalyst", "Sword"],
        "Region" : ["Monstad", "Liyue", "Inazuma", "Sumeru", "Fontaine"]
    }
)
df_write.to_csv("file_21_write.csv")
print("The following data has been written to the file")
print(df_write)

'''
********* OUTPUT **********
Welcome to the program
The data in the csv file is: 
    Name       "Sex"   "Age"   "Height (in)"   "Weight (lbs)"
0   Alex         "M"      41              74              170
1   Bert         "M"      42              68              166
2   Carl         "M"      32              70              155
3   Dave         "M"      39              72              167
4   Elly         "F"      30              66              124
5   Fran         "F"      33              66              115
6   Gwen         "F"      26              64              121
7   Hank         "M"      30              71              158
8   Ivan         "M"      53              72              175
9   Jake         "M"      32              69              143
10  Kate         "F"      47              69              139
11  Luke         "M"      34              72              163
12  Myra         "F"      23              62               98
13  Neil         "M"      36              75              160
14  Omar         "M"      38              70              145
15  Page         "F"      31              67              135
16  Quin         "M"      29              71              176
17  Ruth         "F"      28              65              131
The following data has been written to the file
      Name   Vision    Weapon    Region
0    Venti    Anemo       Bow   Monstad
1  Zhongli      Geo   Polearm     Liyue
2       Ei  Electro   Polearm   Inazuma
3   Nahida   Dendro  Catalyst    Sumeru
4   Furina    Hydro     Sword  Fontaine

'''