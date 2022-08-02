import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    return name


def user_game_interface(Q_and_A_list, user_name):
    for q in Q_and_A_list:
        print('Question: ' + q[0])
        user_answer = prompt.string('Your answer: ')
        if user_answer == q[1]:
            print('Correct!')
        else:
            print(user_answer + ' is wrong answer ;(. Correct answer was ' + q[1] + '.')
            print('Let\'s try again, ' + user_name + '!')
            return
    print('Congratulations, ' + user_name + '!')
