'''
Name:- Kamaltosh Jha
Section A Group 1
Title :- Write a program in python language to display the given pattern:
                5
            4   5
        3   4   5
    2   3   4   5
1   2   3   4   5
                            

'''
#****************Program******************

print('''We are going to print the pattern below
                5
            4   5
        3   4   5
    2   3   4   5
1   2   3   4   5
Here we have printed 5 lines
      ''')

lines = int(input("Enter number of lines you want to print "))

print()

for i in range(lines):
    print("    " * (lines - i - 1), end = "")
    print(lines-i, end = "")
    j = (lines-i)
    while j < lines:
        print("   ", end = "")
        print(j+1, end = "")
        j+=1
    print("")
    

'''
#********OUTPUT********
We are going to print the pattern below
                5
            4   5
        3   4   5
    2   3   4   5
1   2   3   4   5
Here we have printed 5 lines

Enter number of lines you want to print 10

                                    10
                                9   10
                            8   9   10
                        7   8   9   10
                    6   7   8   9   10
                5   6   7   8   9   10
            4   5   6   7   8   9   10
        3   4   5   6   7   8   9   10
    2   3   4   5   6   7   8   9   10
1   2   3   4   5   6   7   8   9   10
'''