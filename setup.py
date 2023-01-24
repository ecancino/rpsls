from choice import Choice


RULES: dict[tuple[Choice, Choice], str] = {
    (Choice.Scissor, Choice.Paper): 'cuts',
    (Choice.Paper, Choice.Rock): 'covers',
    (Choice.Rock, Choice.Lizard): 'crushes',
    (Choice.Lizard, Choice.Spock): 'poisons',
    (Choice.Spock, Choice.Scissor): 'smashes',
    (Choice.Scissor, Choice.Lizard): 'decapitates',
    (Choice.Lizard, Choice.Paper): 'eats',
    (Choice.Paper, Choice.Spock): 'disproves',
    (Choice.Spock, Choice.Rock): 'vaporizes',
    (Choice.Rock, Choice.Scissor): 'crushes',
}
