import prompt
import random


def game_even_logic():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, ' + user_name)
    game_iterations = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while game_iterations < 3:
        question_number = random.randint(1, 100)
        print('Question: ' + str(question_number))
        user_answer = prompt.string('Your answer: ')

        if question_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        
        if user_answer == correct_answer:
            game_iterations += 1
            print('Correct!')       
        else:
            print(user_answer + ' is wrong answer ;(. Correct answer was ' + correct_answer+'.')
            print('Let\'s try again, ' + user_name + '!')
            
            return
    print('Congratulations, ' + user_name + '!')
