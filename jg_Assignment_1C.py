##Assigment-1C

##Program Name: jg_Assigment_1C.py

##Purpose: The purpose of the program is to prompt user to enter name followed by five test scores. The program should display a letter grade for each score and the average test score.

##Author:

##Course: Introduction to scripting CIS.109

##Created January 27, 2024

##Get five test scores assign them to
##test_1, test_2, test_3, test_4, test_5
def main():
    student_name = input('Enter student name:')
    test_1 = float(input('Enter the first test score:'))
    test_2 = float(input('Enter the second test score:'))
    test_3 = float(input('Enter the third test score:'))
    test_4 = float(input('Enter the fouth test score:'))
    test_5 = float(input('Enter the fifth test score:'))
    
    print("\n\n")
    print("===============================================")
    print("===Welcome to Grade and Average Test Scores===")
    print("================================================")
    print("\n")
    print("-------------------------------------------------")
    print(" Student Name:", student_name)
    print("----------------------------------------------")
    print(" Test\tNumeric Grade\tLetter Grade")
    print(" ----   -------------   ------------")
    
    print('1\t',test_1,'\t\t',determine_grade(test_1))
    print('2\t',test_2,'\t\t',determine_grade(test_2))
    print('3\t',test_3,'\t\t',determine_grade(test_3))
    print('4\t',test_4,'\t\t',determine_grade(test_4))
    print('5\t',test_5,'\t\t',determine_grade(test_5))
    
##Calculate the average of five test        
    average = (test_1 + test_2 + test_3 + test_4 + test_5) / 5.0
    print("-----------------------------------------------")
    print("Student Average:", average)
    
##Determine letter grade based on test score
def determine_grade(test_score):
    if test_score >= 90 and test_score <= 100:
        return("A")
    elif test_score >= 80 and test_score <= 89:
        return("B")
    elif test_score >= 70 and test_score <= 79:
        return("C")
    elif test_score >= 60 and test_score <= 69:
        return("D")
    elif test_score < 60:
        return("F")

main()
