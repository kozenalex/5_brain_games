import random
MAX_START = 30
MAX_STEP = 10


def gen_game_progression_que_and_answ():
    first_item = random.randint(1, MAX_START)
    step = random.randint(1, MAX_STEP)
    steps = random.randint(5, 15)
    mask_unit = random.randint(1, steps - 1)
    iteration = 0
    question = str(first_item) + ' '
    while iteration < steps:
        first_item = first_item + step
        if (iteration != mask_unit):
            question = question + str(first_item) + ' '
        else:
            answer = str(first_item)
            question = question + '.. '
        iteration += 1
    return (question, answer)
