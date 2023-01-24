import random
from enum import Enum, auto
from choice import Choice
from scoreboard import Scoreboard
from setup import get_choices
from ui import diplay_winner, display_game_header, display_scores, display_tie, display_versus, read_user_choice,  display_round_header, read_player_name


class Outcomes(Enum):
    WIN = auto()
    TIE = auto()
    LOSS = auto()


choices = get_choices()


def pick_computer_choice() -> Choice:
    return random.choice(choices)


def play_round(current_round: int) -> Outcomes:
    display_round_header(current_round)

    user_choice = read_user_choice()
    bot_choice = pick_computer_choice()

    display_versus(user_choice, bot_choice.choice)

    if (user_choice == bot_choice.choice):
        return Outcomes.TIE

    else:
        winner, message = bot_choice.get_outcome(user_choice)
        print(message)

        return Outcomes.WIN if winner else Outcomes.LOSS


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
        match play_round(current_round):
            case Outcomes.TIE:
                display_tie()
                scoreboard.update_score(ties_name)

            case Outcomes.LOSS:
                diplay_winner(player_name)
                scoreboard.update_score(player_name)

            case Outcomes.WIN:
                diplay_winner(bot_name)
                scoreboard.update_score(bot_name)

    display_scores(scoreboard.get_scores())
