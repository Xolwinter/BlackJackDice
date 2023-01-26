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
    
    def update_victories(self, win, ace=False):
        """
        Desc : Add a victory to the player
        Param : win - Boolean indicates if the player won the round
        """
        if(win):
            if(ace):
                self.victories += 2
            else:
                self.victories += 1
        self.score = 0

    def move(self, score, actions):
        """
        Desc : return the next move of the player
        Param : score - Current state of the player
                actions - List of all actions available depending of the state
        """
        for action in actions:
            
            if(action["state"] == score):
                return action["action"]
        print('Score not referenced')
        return "stop" 

