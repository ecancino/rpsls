from dataclasses import dataclass
from choices import Choices

Outcome = tuple[bool, str]


@dataclass
class Choice():
    choice: Choices
    rules: dict[Choices, Outcome]

    def get_outcome(self, choice: Choices) -> Outcome:
        return self.rules[choice]
