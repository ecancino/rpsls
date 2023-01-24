import random
from enum import Enum, auto
from typing import Optional
from choice import Choice
from scoreboard import Scoreboard
from setup import RULES
from ui import create_message, diplay_winner, display_game_header, display_scores, display_tie, display_versus, read_user_choice,  display_round_header, read_player_name


def pick_computer_choice() -> Choice:
    return random.choice(list(Choice))


def get_winner(choiceA: Choice, choiceB: Choice) -> tuple[Optional[Choice], str]:
    if (choiceA == choiceB):
        return (None, "")

    if (choiceA, choiceB) in RULES:
        return (choiceA, create_message(choiceA, choiceB))

    if (choiceB, choiceA) in RULES:
        return (choiceB, create_message(choiceB, choiceA))

    raise KeyError("Invalid Entities")


def play_round(scoreboard: Scoreboard, player_name: str, bot_name: str, ties_name: str) -> None:
    player_choice = read_user_choice()
    bot_choice = pick_computer_choice()

    display_versus(player_choice, bot_choice)

    winner, message = get_winner(player_choice, bot_choice)

    if winner is None:
        display_tie()
        scoreboard.update_score(ties_name)

    if winner is player_choice:
        diplay_winner(player_name, message)
        scoreboard.update_score(player_name)

    if winner is bot_choice:
        diplay_winner(bot_name, message)
        scoreboard.update_score(bot_name)


def game(scoreboard: Scoreboard, rounds: int = 3) -> None:
    current_round = 1
    ties_name = 'Ties'
    bot_name = 'Bebop'

    player_name = read_player_name()

    scoreboard.register_player(player_name)
    scoreboard.register_player(bot_name)
    scoreboard.register_player(ties_name)

    display_game_header(player_name, bot_name, rounds)

    for current_round in range(1, rounds + 1):
        display_round_header(current_round)
        play_round(scoreboard, player_name, bot_name, ties_name)

    display_scores(scoreboard.get_scores())
