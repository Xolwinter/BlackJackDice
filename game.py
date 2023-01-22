from random import randint
from black_jack_MDP import BlackJack
import algorithm as algo
from random import randrange


class Game:

    def __init__(self, n_round, players) -> None:
        self.round = int(n_round)
        self.players = players

    def infos(self) :
        """
        Display information about the current game

        """

        print("GAME INFORMATIONS : \n")
        print("Number of rounds remaining : ", self.round )
        print("Number of player : ", len(self.players))
        player1 = self.players[0].infos()

        print("Player 1 : " + player1["name"] + " - Score : " + str(player1["score"]) + " - Victories : " + str(player1["victories"]) + " - Type : " + str(player1["type"]) )
        
        if(len(self.players)>1):
            player2 = self.players[1].infos()
            print("Player 2 : " + player2["name"] + " - Score : " + str(player2["score"]) + " - Victories : " + str(player2["victories"]) + " - type : " + str(player1["type"]) )
        print("")
        return 0
        

    def start_game(self):
        """
        Start a game by creating a BlackJack game for each player

        TO DO : Add a verification of human and IA player
        TO DO : Keep track of victories and defeat
        
        """
        mdp = BlackJack()
        res = set()
        reverse = algo.reverse_sort(mdp, 0, res)
        optimal_actions = list()
        b_i = algo.backward_induction(mdp, list(reverse))
        for item in res:
            optimal_actions.append({'action':algo.optimal_action(item, mdp, b_i), 'state':item})

        for round in range(self.round):
            
            print('round ',self.round)
            
            for player in self.players:
                print("Turn of "+ player.name +" to play ! Your current number of round won : ", player.victories)
                if(player.type=="0"):       
                    
                    
                    player_move = player.move(player.score, optimal_actions)
                    while(player_move != "stop"):
                        if(player_move == None):
                            player.score = -1
                            player_move = "stop"
                            break
                        else:
                            dice = roll_dice(player.score)
                            if(player.score+dice > 21):
                                print("You juste rolled a ", dice)
                                print("Round failed")
                                player.score = -1
                                player_move = "stop"
                                break
                            player.score += dice
                            print("You juste rolled a ", dice)
                            print("Your score is now : ", player.score)
                            player_move = player.move(player.score, optimal_actions)
                        print(player_move)
                    
                else:
                    
                    player_move = input("Now select your next move between roll and stop : ")
                    while(player_move != "stop"):
                        if(player_move != "roll"):
                            player_move = input("Please select an action between roll and stop : ")
                        else:
                            
                            dice = roll_dice(player.score)
                            if(player.score+dice > 21):
                                print("You juste rolled a ", dice)
                                print("Round failed")
                                player.score = -1
                                player_move = "stop"
                                break
                            player.score += dice
                            print("You juste rolled a ", dice)
                            print("Your score is now : ", player.score)
                            player_move = input("Please select an action between roll and stop : ")
            print("checkwin")
            check_win(self)
            self.round-=1 
        winner = check_win_game(self)
        if(winner != None):
            print(winner)
            print("End of the game, the winner is... " + str(winner[0]) + " ! With " + str(winner[1]) + " victories !") 
        else:
            print("End of the game, it is a draw !")  


        
    
        return 0

    
def roll_dice(score):
    if(score<17):
        randomNumber = randrange(2,12)
        return randomNumber #Random number between 2 and 12
    else:
        randomNumber = randrange(1,6)
        return randomNumber #Random number between 1 and 6 


def check_win(self):
    if(len(self.players)==1):
        if(self.players[0].score==-1):
            self.players[0].update_victories(False)
        else:
            self.players[0].update_victories(True)
    else:
        if(self.players[0].score == 21 and self.players[1].score == 21):
            self.players[0].update_victories(True)
            self.players[1].update_victories(True)
        elif(self.players[0].score == -1 and self.players[1].score == -1):
            self.players[0].update_victories(False)
            self.players[1].update_victories(False)
        elif(self.players[0].score == -1 and self.players[1].score != -1):
            self.players[0].update_victories(False)
            self.players[1].update_victories(True)
        elif(self.players[0].score != -1 and self.players[1].score == -1):
            self.players[0].update_victories(True)
            self.players[1].update_victories(False)
        elif(self.players[0].score > self.players[1].score ):
            self.players[0].update_victories(True)
            self.players[1].update_victories(False)
        elif(self.players[0].score < self.players[1].score):
            self.players[0].update_victories(False)
            self.players[1].update_victories(True)
        elif(self.players[0].score == self.players[1].score):
            self.players[0].update_victories(False)
            self.players[1].update_victories(False)
        else:
            print("Case not existing")
            print(self.players[0].score, self.players[1].score)

def check_win_game(self):
    if(len(self.players)==1):
        return (self.players[0].name,self.players[0].victories) 
    else:
        if(self.players[0].victories > self.players[1].victories):
            return (self.players[0].name,self.players[0].victories)
        elif(self.players[0].victories == self.players[1].victories):
            return None
        else:
            return (self.players[1].name,self.players[1].victories)