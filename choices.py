from enum import Enum, auto

emoji = {
    'Rock': '🪨',
    'Paper': '📃',
    'Scissor': '✂️',
    'Lizard': '🦎',
    'Spock': '🖖'
}


class Choices(Enum):
    Rock = auto()
    Paper = auto()
    Scissor = auto()
    Spock = auto()
    Lizard = auto()

    def __repr__(self) -> str:
        return f"({self.name}:{self.value})"

    def __str__(self) -> str:
        return f"{self.name} {emoji[self.name]}"
