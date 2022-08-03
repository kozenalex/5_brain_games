#!/usr/bin/env python3
import random
from brain_games.cli import welcome_user, user_game_interface


def generate_progression(first_item, last_item, iterator):
    progression = list(range(first_item, last_item, iterator))
    mask_position = random.randint(1, len(progression) - 1)
    answer = progression[mask_position]
    progression[mask_position] = '..'
    return (' '.join(map(str, progression)), str(answer))


def game_progression_logic():
    user_name = welcome_user()
    print('What number is missing in the progression?')
    Q_and_A_list = []
    iteration = 0
    while iteration < 3:
        first_item = random.randint(1, 30)
        step = random.randint(1, 10)
        last_item = first_item + step * random.randint(5, 15)
        Q_and_A_list.append(generate_progression(first_item, last_item, step))
        iteration += 1
    user_game_interface(Q_and_A_list, user_name)
