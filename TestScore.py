#Create variables
a_score = 90
b_score = 80
c_score = 70
d_score = 60
f_score = 59

#
test_score = int(input('Enter a test score for evaluation: '))

if test_score >= a_score:
    print('Congrats! You did excellent')
    print('Your score was ', test_score)

else:
    if test_score >= b_score:
        print('Good Job. your test score is ', test_score)

    else:
        if test_score >= c_score:
            print('You passed the test with a grade of ', test_score)

        else:
            if test_score >= d_score:
                print('You must do a better job preparing for quizzes and test.')

            else:
                if test_score <= f_score:
                    print('You did not pass the test. Your grade is ', test_score  )