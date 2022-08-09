import prompt
WRNG_ANS_STR = ' is wrong answer ;(. Correct answer was '
GOOD_ANS_STR = 'Correct!'
MAX_ROUNDS = 3


def start(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, ' + user_name)
    print(game.DESCRIPTION)
    for game_round in range(MAX_ROUNDS):
        question, answer = game.generate_round()
        print('Question: ' + question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print(GOOD_ANS_STR)
        else:
            print(user_answer + WRNG_ANS_STR + answer + '.')
            print('Let\'s try again, ' + user_name + '!')
            return
    print('Congratulations, ' + user_name + '!')
