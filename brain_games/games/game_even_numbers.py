#!/usr/bin/env python3
import random
from brain_games.cli import welcome_user, user_game_interface


def game_even_logic():
    user_name = welcome_user()
    iterations = 0
    Q_and_A_list = []
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while iterations < 3:
        question_number = random.randint(1, 100)
        if question_number % 2 == 0:
            Q_and_A_list.append((str(question_number), 'yes'))
        else:
            Q_and_A_list.append((str(question_number), 'no'))
        iterations += 1
    user_game_interface(Q_and_A_list, user_name)
