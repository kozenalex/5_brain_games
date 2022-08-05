#!/usr/bin/env python3
import random
MAX_NUMBER = 100


def is_prime(n):
    devisor = 2
    while devisor <= n / 2:
        if n % devisor == 0:
            return 'no'
        else:
            devisor += 1
    return 'yes'


def game_prime_logic():
    num = random.randint(1, MAX_NUMBER)
    question = str(num)
    answer = is_prime(num)
    return (question, answer)
