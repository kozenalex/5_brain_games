#!/usr/bin/env python3
from brain_games.games.game_gcd import game_gcd_logic
from brain_games.cli import user_game_interface
GREETING = 'Find the greatest common divisor of given numbers.'


def main():
    user_game_interface(game_gcd_logic, GREETING)


if __name__ == '__main__':
    main()
