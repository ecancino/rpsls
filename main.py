from game import game
from scoreboard import Scoreboard
from ui import display_welcome, play_music


def main() -> None:
    play_music()
    display_welcome()

    game(Scoreboard())


if __name__ == '__main__':
    main()
