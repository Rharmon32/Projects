import random

number = random.randint(1, 25)

for i in range(6):
        print('guess a number between 1 and 25:')
        guess = input()
        guess = int(guess)

        if guess < number:
            print('Your guess is too low')

        if guess > number:
                print('Your guess is too high')

        if guess == number:
                    break

        if guess == number:
             print('You got the answer correct')

        else:
             print('You did not guess the number. the number was ' + str(number))
            
