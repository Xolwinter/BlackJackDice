
class BlackJack:

    def __init__(self):
        return
        

    def successors(self, state):
        """
            Desc : Return the successors of the different actions, depending on the state
            Params : Current player score as state
        """
        
        assert not self.is_terminal(state)
        roll_successors = self.roll_successors(state)
        stop_successors = self.stop_successors(state)

        return [roll_successors, stop_successors]

    def is_terminal(self, state):

        return state==-1

    def stop_successors(self, state, max_score=21):
        """
            Desc : Return the successors if the move is 'stop'
            Params : 
        """
        
        assert 0 <= state <= max_score
        END_STATE = -1

        action = 'stop'
        next_states = [-1]
        transitions = [1]
        rewards = [state]
        return action, next_states, transitions, rewards

    def roll_successors(self, state, max_score=21):
        
        assert 0 <= state <= max_score
        END_STATE = -1

        next_states = []
        action = "roll"

        if(state<17):

            rewards = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            transitions = [1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11]
            dices = [2,3,4,5,6,7,8,9,10,11,12]

        else:
            rewards = [0, 0, 0, 0, 0, 0]
            transitions = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
            dices = [1,2,3,4,5,6]
        
        for dice in dices:
            after_state = state + dice
            if(after_state>21):
                after_state=-1
            next_states.append(after_state)

        return action, next_states, transitions, rewards

    
        
        
