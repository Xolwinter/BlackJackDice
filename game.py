from random import randint
from black_jack_MDP import BlackJack
from black_jack import BlackJackTrain
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

        print("Player 1 : " + player1["name"] + " - Score : " + str(player1["score"]) + " - Points : " + str(player1["victories"]) + " - Type : " + str(player1["type"]) )
        
        if(len(self.players)>1):
            player2 = self.players[1].infos()
            print("Player 2 : " + player2["name"] + " - Score : " + str(player2["score"]) + " - Points : " + str(player2["victories"]) + " - type : " + str(player1["type"]) )
        print("")
        return 0
        

    def start_game(self):
        """
        Start a game by creating a BlackJack game for each player

        TO DO : Keep track of victories and defeat
        
        """
        
        optimal_actions = select_policy()

        for round in range(self.round):
            
            print('Round : ' + str(self.round) + '\n')
            
            for player in self.players:
                
                print("Turn of "+ player.name +" to play ! Your current number of point won : " + str(player.victories) + '\n')
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
                                print("You juste rolled a " + str(dice) + '\n')
                                print("Round failed \n")
                                player.score = -1
                                player_move = "stop"
                                break
                            player.score += dice
                            print("You juste rolled a ", str(dice) + '\n')
                            print("Your score is now : " + str(player.score)+ '\n')
                            player_move = player.move(player.score, optimal_actions)
                        #print(player_move)
                    

                else:
                    
                    player_move = input("\nNow select your next move between roll and stop : ")
                    while(player_move != "stop"):
                        if(player_move != "roll"):
                            player_move = input("\nPlease select an action between roll and stop : ")
                        else:
                            
                            dice = roll_dice(player.score)
                            if(player.score+dice > 21):
                                print("\n You juste rolled a :" + str(dice) + "\n")
                                print("Round failed\n")
                                player.score = -1
                                player_move = "stop"
                                check_win(self)
                                break
                            player.score += dice
                            print("You juste rolled a " + str(dice) + "\n")
                            print("Your score is now : " + str(player.score) + "\n")
                            player_move = input("\nPlease select an action between roll and stop : ")
                
                if(player.score==-1 or player.score==21 or player.score==0):
                    ##CASE 21 or >
                    break
            ##SWAP PLAYER POSITIOn
            
            if(len(self.players)>1):
                temp_player = self.players[0]
                self.players[0] = self.players[1]
                self.players[1] = temp_player

            check_win(self)
            self.round-=1 
        winner = check_win_game(self)
        if(winner != None):
            print("End of the game, the winner is... " + str(winner[0]) + " ! With " + str(winner[1]) + " points !\n") 
        else:
            print("End of the game, it is a draw !\n")  


        
    
        return 0


    def training(self, stopat):
        scores = []
        game = BlackJackTrain()
        for i in range(self.round):
            state = game.reset()
            while True:
                action = game.stop_at(stopat)
                state, reward, done = game.step(action)
                
                if(done):
                    break
            scores.append(reward)
        return sum(scores)/len(scores)
        

def roll_dice(score):
    """
        Desc : Return a random number depending on the score 
        Param : Current player score
    """
    if(score<17):
        randomNumber = randrange(2,12)
        return randomNumber #Random number between 2 and 12
    else:
        randomNumber = randrange(1,6)
        return randomNumber #Random number between 1 and 6 

def select_policy():
    """
        TO DO : Get the optimal strategy
        Desc : Get the optimal policy and train to find the optimal strategy
    """

    mdp = BlackJack()
    res = set()
    reverse = algo.reverse_sort(mdp, 0, res)
    optimal_actions = list()
    b_i = algo.backward_induction(mdp, list(reverse))
    for item in res:
        optimal_actions.append({'action':algo.optimal_action(item, mdp, b_i), 'state':item})
    return optimal_actions

def check_win(self):
    """
        Desc : Update the players victory depending on the scores
    """

    if(len(self.players)==1):
        if(self.players[0].score==-1):
            self.players[0].update_victories(False)
        elif(self.players[0].score == 21):
            self.players[0].update_victories(True, ace=True)
        else:
            self.players[0].update_victories(True)
    else:
        if(self.players[0].score == 21 and self.players[1].score == 21):
            self.players[0].update_victories(True, ace=True)
            self.players[1].update_victories(True, ace=True)
        elif(self.players[0].score == 21):
            print("Ace")
            self.players[0].update_victories(True, ace=True)
        elif(self.players[1].score == 21):
            print("Ace")
            self.players[1].update_victories(True, ace=True)
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
            #print(self.players[0].score, self.players[1].score)

def check_win_game(self):
    """
        Desc : Verify which player won the game
    """
    if(len(self.players)==1):
        return (self.players[0].name,self.players[0].victories) 
    else:
        if(self.players[0].victories > self.players[1].victories):
            return (self.players[0].name,self.players[0].victories)
        elif(self.players[0].victories == self.players[1].victories):
            return None
        else:
            return (self.players[1].name,self.players[1].victories)

