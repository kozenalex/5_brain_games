#!/usr/bin/env python3
import random
MAX_NUMBER = 30


def mul(a, b):
    return a * b


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def game_calc_logic():
    acts = ((add, ' + '), (sub, ' - '), (mul, ' * '))
    num1 = random.randint(1, MAX_NUMBER)
    num2 = random.randint(1, MAX_NUMBER)
    sign = random.randint(0, 2)
    question = str(num1) + acts[sign][1] + str(num2)
    answer = str(acts[sign][0](num1, num2))
    return (question, answer)
