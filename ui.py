from playsound import playsound
from choice import Choice
from setup import RULES


def create_message(choiceA: Choice, choiceB: Choice):
    return f"{choiceA} {RULES[(choiceA, choiceB)]} {choiceB}"


def play_music():
    playsound('The_Big_Bang_Theory_Theme_Song.mp3', block=False)


def print_line() -> None:
    print('#' * 50, end='\n')


def diplay_winner(player_name: str, message: str) -> None:
    print(f"{player_name} wins!")
    print(message)


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
    for winner, loser in RULES:
        print(create_message(winner, loser))
    print_line()


def read_player_name() -> str:
    print("Write your user name:", end=" ")
    return input().strip()


def display_retry_choice(option: str) -> None:
    print(f"Option '{option}' is not a valid choice.")


def read_user_choice() -> Choice:
    print(
        f"Input your selection: {Choice.Rock}, {Choice.Paper}, {Choice.Scissor}, {Choice.Lizard} or {Choice.Spock}:", end=" ")
    _ = input().strip().capitalize()

    try:
        return Choice[_]
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


def display_versus(user_choice: Choice, computer_choice: Choice) -> None:
    print(f"{user_choice} vs. {computer_choice}")
