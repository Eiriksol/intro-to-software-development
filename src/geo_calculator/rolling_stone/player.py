import regex as re


class InvalidPlayerNameException(Exception):
    def __init__(self, message="Name must have at least one character"):
        super().__init__(message)


class Player:
    def __init__(self):
        self.score = 0
        self.name = None

    def prompt_for_name(self):
        name = self._get_name_for_player_from_input()
        if name != None:
            if len(name.strip()) < 1:
                raise InvalidPlayerNameException()
            if not re.fullmatch(r"[A-Za-zæøåÆØÅ ]+", name):
                raise InvalidPlayerNameException(
                    "Name can only contain alphabetic characters and spaces"
                )
            if "  " in name:
                raise InvalidPlayerNameException(
                    "Name cannot have multiple spaces in a row"
                )
        self.name = name
        return self._get_name_for_player_from_input

    def _get_name_for_player_from_input(self):
        pass

    def receive_score(self, score: int):
        self.score += score
