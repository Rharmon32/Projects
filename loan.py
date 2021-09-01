#This program will determin if a customer is
#eligible for a loan

#Minimum salary
minimum_salary = 30000.0
minimum_years = 2

#
years_worked = int(input('How many years have you been at your job? '))
verify_salary = float(input('What is your annual salary? '))

if years_worked >= minimum_years:
    print('You have met the minimum years required')

    if verify_salary >= minimum_salary:
        print('You qualify for the loan!')

    else:
        print('I am sorry you do not meet the minimum salary of', minimum_salary)

    
else:
    print('But I am sorry, you do not meet the minimum years required.')

    
