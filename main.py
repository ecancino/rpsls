from game import game
from scoreboard import Scoreboard
from setup import play_music
from ui import display_welcome


def main() -> None:
    play_music()
    display_welcome()

    game(Scoreboard())


if __name__ == '__main__':
    main()
