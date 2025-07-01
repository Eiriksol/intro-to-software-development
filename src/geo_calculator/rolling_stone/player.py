class Player():
    def __init__(self):
        self.name = "Eirik"     
        self.score = 0
    
    def receive_score(self, score: int):
        self.score += score