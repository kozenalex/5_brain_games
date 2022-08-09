import random
GAME_NUMBER_MAX = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    game_number = random.randint(1, GAME_NUMBER_MAX)
    if game_number % 2 == 0:
        return (str(game_number), 'yes')
    else:
        return (str(game_number), 'no')
