import algorithm as algo
from random import randrange

class BlackJackTrain():

    def __init__(self):
        self.state = 0
        self.end = False

    def reset(self):
        self.state = 0
        self.end = True
        return 0

    def step(self, action):
        if self.state == None:
            print("Terminal state")
            return 
        elif action != 0 and action != 1:
            print("Invalid action")
            return
        elif action == 0:
            return self._roll()
        else:
            return self._stop()

    def _stop(self):
        reward = self.state
        self.state = None
        done = True
        return self.state, reward, done

    def _roll(self):
        reward = 0
        self.state += self.roll_dice()
        done = False
        if(self.state > 21):
            self.state = None
            done = True
        return self.state, reward, done


    def roll_dice(self):
        """
            Desc : Return a random number depending on the score 
            Param : Current player score
        """
        if(self.state<17):
            randomNumber = randrange(2,12)
            return randomNumber #Random number between 2 and 12
        else:
            randomNumber = randrange(1,6)
            return randomNumber #Random number between 1 and 6     


    def stop_at(self, threshold=16):
        if self.state >= threshold:
            return 1
        else:
            return 0
    