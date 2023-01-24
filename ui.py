from itertools import repeat
from choices import Choices
from messages import messages


def print_line() -> None:
    print('#' * 50, end='\n')


def diplay_winner(player_name: str) -> None:
    print(f"{player_name} wins!")


def display_tie() -> None:
    print("It's a tie!")


def display_game_header(user_name: str, bot_name: str, rounds: int) -> None:
    print(f"{user_name} vs. {bot_name}")
    print(f"Playing {rounds} rounds")
    print_line()


def display_welcome() -> None:
    print("Welcome to the game!")
    print("Rock, Paper, Scissor, Lizard, Spock by Sam Kass")
    print_line()

    print("Rules are very simple:")
    print(messages['scissor_vs_paper'], end=", ")
    print(messages['paper_vs_rock'], end=", ")
    print(messages['rock_vs_lizard'], end=", ")
    print(messages['lizard_vs_spock'], end=", ")
    print(messages['spock_vs_scissor'], end=", ")
    print(messages['scissor_vs_lizard'], end=", ")
    print(messages['lizard_vs_paper'], end=", ")
    print(messages['paper_vs_spock'], end=", ")
    print(messages['spock_vs_rock'], end=", ")
    print("and, as it always has:", end=" ")
    print(messages['rock_vs_scissor'], end="\n")
    print_line()


def read_player_name() -> str:
    print("Write your user name:", end=" ")
    return input().strip()


def display_retry_choice(option: str) -> None:
    print(f"Option '{option}' is not a valid choice.")


def read_user_choice() -> Choices:
    print(
        f"Input your selection: {Choices.Rock}, {Choices.Paper}, {Choices.Scissor}, {Choices.Lizard} or {Choices.Spock}:", end=" ")
    _ = input().strip().capitalize()

    try:
        return Choices[_]
    except KeyError:
        display_retry_choice(_)
        return read_user_choice()


def display_round_header(current_round: int) -> None:
    print()
    print_line()
    print(f"Round {current_round}")
    print_line()


def display_scores(scores: tuple[str, int]) -> None:
    print("")
    print("Scoreboard:")
    print_line()
    for user, score in scores:
        print(f"{user}: {score}")
    print_line()


def display_versus(user_choice: Choices, computer_choice: Choices) -> None:
    print(f"{user_choice} vs. {computer_choice}")
