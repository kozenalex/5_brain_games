#!/usr/bin/env python3
from brain_games.games.game_progression import game_progression_logic
from brain_games.cli import user_game_interface
GREETING = 'What number is missing in the progression?'


def main():
    user_game_interface(game_progression_logic, GREETING)


if __name__ == '__main__':
    main()
