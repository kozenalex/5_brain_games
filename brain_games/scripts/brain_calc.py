#!/usr/bin/env python3
from brain_games.games.game_calc import game_calc_logic
from brain_games.cli import user_game_interface
GREETING = 'What is the result of the expression?'


def main():
    user_game_interface(game_calc_logic, GREETING)


if __name__ == '__main__':
    main()
