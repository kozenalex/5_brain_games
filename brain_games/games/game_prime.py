#!/usr/bin/env python3
import random
from brain_games.cli import welcome_user, user_game_interface


def is_prime(n):
    devisor = 2
    while devisor <= n / 2:
        if n % devisor == 0:
            return 'no'
        else:
            devisor += 1
    return 'yes'


def game_prime_logic():
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    Q_and_A_list = []
    iteration = 0
    while iteration < 3:
        question_number = random.randint(1, 100)
        Q_and_A_list.append((str(question_number), is_prime(question_number)))
        iteration += 1
    user_game_interface(Q_and_A_list, user_name)
