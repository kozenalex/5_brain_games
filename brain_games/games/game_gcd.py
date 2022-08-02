#!/usr/bin/env python3
import random
from brain_games.cli import welcome_user, user_game_interface


def find_gcd(a, b):
    gcd = 1
    temp_devisor = 1
    while temp_devisor <= max(a, b) / 2:
        if a % temp_devisor == 0 and b % temp_devisor == 0:
            gcd = temp_devisor
        temp_devisor += 1
    return gcd


def game_gcd_logic():
    user_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    Q_and_A_list = []
    iteration = 0
    while iteration < 3:
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        Q_and_A_list.append((str(a) + ' ' + str(b), str(find_gcd(a, b))))
        iteration += 1
    user_game_interface(Q_and_A_list, user_name)
