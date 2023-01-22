from random import randint


class Player:

    def __init__(self, name, type=1) -> None:
        self.name = name
        self.score = 0
        self.victories = 0
        self.type = type
        
    def infos(self):
        return {
            "name":self.name,
            "score":self.score,
            "victories":self.victories,
            "type":int(self.type)
        }
