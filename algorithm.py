def bellman(state, mdp, value, discount=1):

    if(mdp.is_terminal(state)):
        return 0
    else:
        action_values=[]
        for action, next_states, transitions, rewards in mdp.successors(state):
            mean = 0
            for i, next_state in enumerate(next_states):
                
                mean += transitions[i] * (rewards[i] + (discount * value[next_state]))
            
            action_values.append(mean)
        max_val = max(action_values)
        value[state]=max_val
        return max_val


def reverse_sort(mdp, state, visited=None) -> int:
    """Generator of states in reverse topological order"""

    if visited is None: visited = set()
    visited.add(state)
    if not mdp.is_terminal(state):
        for _, next_states, _, _ in mdp.successors(state):
            for child in next_states:
                if child not in visited:
                    yield from reverse_sort(mdp, child, visited)
    
    yield state


def backward_induction(mdp, reverse_topological_order):
    
    value = {}

    for state in reverse_topological_order:
        v = bellman(state, mdp, value)
        print(v, state)
        value[state] = v
        
    return value

def optimal_action(state, mdp, value: dict, discount=1):
    if mdp.is_terminal(state):
        return None
    else:
        max_val = -float('inf')
        best_action = None
        for action, next_states, probas, rewards in mdp.successors(state):
            mean = 0
            for next_state, proba, reward in zip(next_states, probas, rewards):
                mean += proba*(reward + discount * value[next_state])

            if mean > max_val:
                max_val = mean
                best_action = action
        return best_action