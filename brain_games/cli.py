import prompt
WRNG_ANS_STR = ' is wrong answer ;(. Correct answer was '
GOOD_ANS_STR = 'Correct!'


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    return name


def user_game_interface(game_func, greet):
    user_name = welcome_user()
    print(greet)
    game_step = 0
    while game_step < 3:
        Q_and_A = game_func()
        print('Question: ' + Q_and_A[0])
        answer = prompt.string('Your answer: ')
        if answer == Q_and_A[1]:
            game_step += 1
            print(GOOD_ANS_STR)
        else:
            print(answer + WRNG_ANS_STR + Q_and_A[1] + '.')
            print('Let\'s try again, ' + user_name + '!')
            return
    print('Congratulations, ' + user_name + '!')
