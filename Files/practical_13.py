'''
Name:- Kamaltosh Jha
Section A, Group-1
Title - WAP to take subjects of 5 marks and based on the percentage print the grades A B C D E 
'''

#***************Code of the Program****************

num_subjects = 5

marks1 = float(input("Enter marks in subject 1 "))
marks2 = float(input("Enter marks in subject 2 "))
marks3 = float(input("Enter marks in subject 3 "))
marks4 = float(input("Enter marks in subject 4 "))
marks5 = float(input("Enter marks in subject 5 "))

max_marks_per_subject = int(input("Enter maximum marks for each subject "))

total_marks_obtained = marks1 + marks2 + marks3 + marks4 + marks5
total_maximum_marks = num_subjects * max_marks_per_subject
percentage_marks = (total_marks_obtained*100)/(total_maximum_marks)

print("")
print("Your percentage is ", str(percentage_marks) + "%")

if(percentage_marks>=91 and percentage_marks<= 100):
    print("Your grade is A")
elif(percentage_marks>=81 and percentage_marks<= 90):
    print("Your grade is B")
elif(percentage_marks>=71 and percentage_marks<= 80):
    print("Your grade is C")
elif(percentage_marks>=61 and percentage_marks<= 70):
    print("Your grade is D")
elif(percentage_marks>=51 and percentage_marks<= 60):
    print("Your grade is E")
else:
    print("Your grade is F")

print("")
print("The Grade System is")
print('''
Marks   Grade
91-100    A
81-90     B
71-80     C
61-70     D
51-60     E
Below 51  F
''')

'''
********* OUTPUT **********
Enter marks in subject 1 83
Enter marks in subject 2 84
Enter marks in subject 3 81
Enter marks in subject 4 85
Enter marks in subject 5 82
Enter maximum marks for each subject 100

Your percentage is  83.0%
Your grade is B

The Grade System is

Marks   Grade
91-100    A
81-90     B
71-80     C
61-70     D
51-60     E
Below 51  F
'''