import random
MAX_START = 30
MAX_STEP = 10


def gen_progression():
    first_item = random.randint(1, MAX_START)
    step = random.randint(1, MAX_STEP)
    last_item = first_item + step * random.randint(5, 15)
    res = list(range(first_item, last_item, step))
    return res


def gen_game_progression_que_and_answ():
    unmasked_str = gen_progression()
    mask_unit = random.randint(1, len(unmasked_str) - 1)
    answer = str(unmasked_str[mask_unit])
    unmasked_str[mask_unit] = '..'
    question = ' '.join(map(str, unmasked_str))
    return (question, answer)
