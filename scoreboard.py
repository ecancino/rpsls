class Scoreboard:
    def __init__(self) -> None:
        self.__points: dict[str, int] = {}

    def register_player(self, player_name: str) -> None:
        self.__points[player_name] = 0

    def update_score(self, player_name: str) -> None:
        self.__points[player_name] += 1

    def get_scores(self) -> dict[str, int]:
        return self.__points.items()
