from choice import Choice
from choices import Choices
from messages import messages
from playsound import playsound


def play_music():
    pass
    # playsound('The_Big_Bang_Theory_Theme_Song.mp3', block=False)


def get_choices() -> list[Choice]:
    return [
        Choice(Choices.Rock, {
            Choices.Paper: (False, messages['paper_vs_rock']),
            Choices.Scissor: (True, messages['rock_vs_scissor']),
            Choices.Lizard: (True, messages['rock_vs_lizard']),
            Choices.Spock: (False, messages['spock_vs_rock']),
        }),

        Choice(Choices.Paper, {
            Choices.Rock: (True, messages['paper_vs_rock']),
            Choices.Scissor: (False, messages['scissor_vs_paper']),
            Choices.Lizard: (False, messages['lizard_vs_paper']),
            Choices.Spock: (True, messages['paper_vs_spock']),
        }),

        Choice(Choices.Scissor, {
            Choices.Rock: (False, messages['rock_vs_scissor']),
            Choices.Paper: (True, messages['scissor_vs_paper']),
            Choices.Lizard: (True, messages['scissor_vs_lizard']),
            Choices.Spock: (False, messages['spock_vs_scissor']),
        }),

        Choice(Choices.Lizard, {
            Choices.Rock: (False, messages['rock_vs_lizard']),
            Choices.Paper: (True, messages['lizard_vs_paper']),
            Choices.Scissor: (False, messages['scissor_vs_lizard']),
            Choices.Spock: (True, messages['lizard_vs_spock'])
        }),

        Choice(Choices.Spock, {
            Choices.Rock: (True, messages['spock_vs_rock']),
            Choices.Paper: (False, messages['paper_vs_spock']),
            Choices.Scissor: (True, messages['spock_vs_scissor']),
            Choices.Lizard: (False, messages['lizard_vs_spock'])
        })
    ]
