import random
GAME_NUMBER_MAX = 100


def gen_game_even_que_and_answ():
    game_number = random.randint(1, GAME_NUMBER_MAX)
    if game_number % 2 == 0:
        return (str(game_number), 'yes')
    else:
        return (str(game_number), 'no')
