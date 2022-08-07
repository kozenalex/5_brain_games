#!/usr/bin/env python3
from brain_games.games.calc import gen_game_calc_que_and_answ
from brain_games.engine import user_game_interface
GREETING = 'What is the result of the expression?'


def main():
    user_game_interface(gen_game_calc_que_and_answ, GREETING)


if __name__ == '__main__':
    main()
