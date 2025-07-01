class Player():
    def __init__(self):  
        self.score = 0
        self.name = None

    def prompt_for_name(self):
        self.name = self._get_name_for_player_from_input()
    
    def _get_name_for_player_from_input(self):
        self.name = input("Set name: ")

    def receive_score(self, score: int):
        self.score += score
