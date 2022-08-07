#!/usr/bin/env python3
from brain_games.games.gcd import gen_game_gcd_que_and_answ
from brain_games.engine import user_game_interface
GREETING = 'Find the greatest common divisor of given numbers.'


def main():
    user_game_interface(gen_game_gcd_que_and_answ, GREETING)


if __name__ == '__main__':
    main()
