#!/usr/bin/env python3
from brain_games.games.progression import gen_game_progression_que_and_answ
from brain_games.engine import user_game_interface
GREETING = 'What number is missing in the progression?'


def main():
    user_game_interface(gen_game_progression_que_and_answ, GREETING)


if __name__ == '__main__':
    main()
