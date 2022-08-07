#!/usr/bin/env python3
from brain_games.games.prime import gen_game_prime_que_and_answ
from brain_games.engine import user_game_interface
GREETING = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    user_game_interface(gen_game_prime_que_and_answ, GREETING)


if __name__ == '__main__':
    main()
