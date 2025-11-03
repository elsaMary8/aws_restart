"""
Write a Python program that asks the user to enter the names of three students and their marks 
in three subjects. The program should then display each student’s name, their marks, their 
average score, and whether they have passed or failed based on their average.
"""

student_num = 4
for i in range(1,student_num):
    
    print("\n STUDENT {} MARK DETAILS and RESULT".format(i))

    student_name = input("Enter student name: ")


    subject1 = input("Enter mark of Subject 1:")
    subject2 = input("Enter mark of Subject 2:")
    subject3 = input("Enter mark of Subject 3:")

    subject1 = int(subject1)
    subject2 = int(subject2)
    subject3 = int(subject3)

    averagescore = (subject1 + subject2 + subject3)/3
    
    if averagescore > 50:
        print("{} has an average score of {}. \nPASSED!!!".format(student_name, averagescore))
    else:
         print("{} has an average score of {}. \nFAILED...".format(student_name, averagescore))

   

