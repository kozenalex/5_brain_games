import random
MAX_NUMBER = 30


def gen_game_calc_que_and_answ():
    num1 = random.randint(1, MAX_NUMBER)
    num2 = random.randint(1, MAX_NUMBER)
    sign = random.randint(0, 2)
    if sign == 0:
        question = str(num1) + ' + ' + str(num2)
        answer = str(num1 + num2)
    if sign == 1:
        question = str(num1) + ' - ' + str(num2)
        answer = str(num1 - num2)
    if sign == 2:
        question = str(num1) + ' * ' + str(num2)
        answer = str(num1 * num2)
    return (question, answer)
