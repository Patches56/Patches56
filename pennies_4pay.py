##Jairo Gutierrez Introduction to python 115
## Pennies for Pay
pay_per_day = 0.01
total_salary = 0
##Get the number of days
work_days = int(input('Enter the number of days (between 3 and 49):'))

#loop (data is BAD) 
while work_days < 3 or work_days > 49:
    print(work_days, "Invalid!")
      ##Ask for input again
    work_days = int(input('Enter the number of days (between 3 and 49):'))

##fstrings
print('Day\t\t\tSalary')
print('------------------------------------')

for num in range (work_days):
    print(f'{num+1:2.0f}\t\t\t\t${pay_per_day}')
    total_salary += pay_per_day
    pay_per_day *= 2

print(f'\ntotal_salary for {work_days} days : ${total_salary:.2f}')

##Test output
##Enter the number of days (between 3 and 49):15
##Day			Salary
##------------------------------------
## 1				$0.01
## 2				$0.02
## 3				$0.04
## 4				$0.08
## 5				$0.16
## 6				$0.32
## 7				$0.64
## 8				$1.28
## 9				$2.56
##10				$5.12
##11				$10.24
##12				$20.48
##13				$40.96
##14				$81.92
##15				$163.84
##
##total_salary for 15 days : $327.67
