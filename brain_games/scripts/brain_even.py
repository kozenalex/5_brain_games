#!/usr/bin/env python3
from brain_games.games.even import gen_game_even_que_and_answ
from brain_games.engine import user_game_interface
GREETING = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    user_game_interface(gen_game_even_que_and_answ, GREETING)


if __name__ == '__main__':
    main()
