#!/usr/bin/env python3
import random
from brain_games.cli import welcome_user, user_game_interface


def mul(a, b):
    return a * b


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def game_calc_logic():
    user_name = welcome_user()
    print('What is the result of the expression?')
    Q_and_A_list = []
    actions = ((add, ' + '), (sub, ' - '), (mul, ' * '))
    iteration = 0
    while iteration < 3:
        a = random.randint(0, 30)
        b = random.randint(0, 30)
        act = random.randint(0, 2)
        answer = actions[act][0](a, b)
        Q_and_A_list.append((str(a) + actions[act][1] + str(b), str(answer)))
        iteration += 1
    user_game_interface(Q_and_A_list, user_name)
