from random import randint
from black_jack_MDP import BlackJack
import algorithm as algo


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

        for player in self.players:

            if(player.type==0):       
                print("mdp : ",mdp)
                print("reverse : ", reverse)
                optimal_actions = list()
                b_i = algo.backward_induction(mdp, list(reverse))
                for item in res:
                    optimal_actions.append({'action':algo.optimal_action(item, mdp, b_i), 'state':item})
            else:
                print("Your turn to play ! Your current number of round won : " + player.victories)
                player_move = input("Now select your next move between roll and stop !")
                while(player_move != "stop"):
                    if(player_move != "roll"):
                        player_move = input("Please select an action between roll and stop !")
                    else:
                        player.score = roll_dice(player.score)
                    
                    
                


        for round in range(self.round):
            
            print('round '+self.round)
            print()





            self.round-=1
    
        return res

    
def roll_dice(score):
    if(score<17):
        return score + 10
    else:
        return score + 4