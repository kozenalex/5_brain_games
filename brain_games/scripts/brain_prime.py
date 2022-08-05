#!/usr/bin/env python3
from brain_games.games.game_prime import game_prime_logic
from brain_games.cli import user_game_interface
GREETING = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    user_game_interface(game_prime_logic, GREETING)


if __name__ == '__main__':
    main()
