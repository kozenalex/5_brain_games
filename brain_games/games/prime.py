import random
MAX_NUMBER = 100
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    devisor = 2
    while devisor <= n / 2:
        if n % devisor == 0:
            return False
        else:
            devisor += 1
    return True


def generate_round():
    num = random.randint(1, MAX_NUMBER)
    question = str(num)
    if is_prime(num):
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
