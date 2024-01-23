##Jairo Gutierrez Inro to python 115
##Test Average and grade   
def main():
    
    score_1 = get_score('test 1')
    score_2 = get_score('test 2')
    score_3 = get_score('test 3')


    average_score = get_average(score_1,score_2,score_3)
    letter_grade = get_grade(average_score)

    print(f'score 1 : {score_1:.1f}')
    print(f'score 2 : {score_2:.1f}')
    print(f'score 3 : {score_3:.1f}')
    print(f'Average score : {average_score:.1f}')
    print(letter_grade)

def get_score(param):
    score = float(input(f'Enter score for {param} 0-100 :'))
    while(not(score >= 0 and score <= 100)):
        print('Invalid')
        score = float(input(f'Enter score for 0-100 :'))
    return score

def get_average(grade1, grade2, grade3):
    averages = (grade1 + grade2 + grade3) / 3.0
    return averages

def get_grade(the_score):
    student_grade = ""
    if the_score >= 90:
        student_grade = "A"
    elif the_score >= 80:
        student_grade = "B"
    elif the_score >= 70:
        student_grade = "C"
    elif the_score >= 60:
        student_grade = "D"
    elif the_score > 60:
        student_grade = "F"
    return student_grade
        
main()

##Test Output
##Enter score for test 1 0-100 :100
##Enter score for test 2 0-100 :80
##Enter score for test 3 0-100 :60
##score 1 : 100.0
##score 2 : 80.0
##score 3 : 60.0
##Average score : 80.0
##B

