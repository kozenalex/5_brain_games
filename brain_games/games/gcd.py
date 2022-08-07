import random
MAX_NUMBER = 100


def find_gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    if a == b:
        return a
    gcd = 1
    temp_devisor = 1
    while temp_devisor <= max(a, b) / 2:
        if a % temp_devisor == 0 and b % temp_devisor == 0:
            gcd = temp_devisor
        temp_devisor += 1
    return gcd


def gen_game_gcd_que_and_answ():
    num1 = random.randint(1, MAX_NUMBER)
    num2 = random.randint(1, MAX_NUMBER)
    question = str(num1) + ' ' + str(num2)
    answer = str(find_gcd(num1, num2))
    return (question, answer)
