from game import Game
from player import Player


def start_game(n_player, n_round=10):
    """
    Start a new game
    param: n_player - Number of player between 1 and 2
    param: n_round - Number of round that should be played
    
    """
    
    players = []
    player_name = input('Write the name of the first player : ')
    while player_name == "":
        player_name = input('A name cannot be blank. Write the name of the player : ')
    player_type = input('Write 1 if this player is a human, 0 otherwise : ')
    while player_type != "1" and player_type != "0":
        player_type = input('A name cannot be blank. Write the name of the player : ')
    players.append(Player(player_name, player_type))

    if(n_player == 2):
        player_name = input('Write the name of the second player : ')
        while player_name == "":
            player_name = input('A name cannot be blank. Write the name of the player : ')
        player_type = input('Write 1 if this player is a human, 0 otherwise : ')
        while player_type != "1" and player_type != "0":
            player_type = input('A name cannot be blank. Write the name of the player : ')
        players.append(Player(player_name))

    game = Game(n_round, players)
    game.infos()
    game.start_game()
    

    return 0
 

def main():

    print('Hey there, welcome on a game of blackjack dice performed by IA !')
    n_player = input('First, type 1 or 2 to select the number of player.\n')
    n_round = input('Please select a number of round.\n')

    if(n_round==''):
        print('Starting a ' + n_player + ' player game of 10 rounds....')
    else:
        print('Starting a ' + n_player + ' player game of '+ n_round + ' rounds....')


    while(1):
        
        if(n_player!='1' and n_player!='2'):
            n_player = input('Configuration failed, please select a number of player between 1 and 2.\n')
        elif(n_round==''):
            start_game(int(n_player))
            return 0
        else:
            start_game(int(n_player), n_round=int(n_round))
            return 0
            

if __name__ == "__main__":
    main()