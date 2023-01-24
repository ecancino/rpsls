from enum import Enum, auto

emoji = {
    'Rock': '🪨',
    'Paper': '📃',
    'Scissor': '✂️',
    'Lizard': '🦎',
    'Spock': '🖖'
}


class Choice(Enum):
    Rock = auto()
    Paper = auto()
    Scissor = auto()
    Spock = auto()
    Lizard = auto()

    def __str__(self) -> str:
        return self.name
