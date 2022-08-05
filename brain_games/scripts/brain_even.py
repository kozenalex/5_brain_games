#!/usr/bin/env python3
from brain_games.games.game_even_numbers import game_even_logic
from brain_games.cli import user_game_interface
GREETING = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    user_game_interface(game_even_logic, GREETING)


if __name__ == '__main__':
    main()
