import pandas as pd
from collections import Counter

def get_transition_matrix(df):
    """obtain the transition matrix - outputted as a Counter object - from the input of a dataframe consisting of states with time as an index. A trivial example input is a dataframe with values 1, 2 in row 1,         
    corresponding to the states at t=0. Then values 2, 3 in row 2, corresponding to states in t=1."""
    #get sorted list of the individual values in the state matrix
    states = sorted(list(set(pd.Series(df.values.ravel()))))
    #convert the states to a set
    states_set = set(states)
    #obtain the potential state transitions
    state_transitions = [ (init_state, next_state) for init_state in states_set for next_state in states_set ]
    #create a Counter object of each state transition: this is our transition matrix representation
    state_transitions = Counter(state_transitions)
    transition_matrix = state_transitions
    #now update the transition matrix to reflect the transition of states in the input dataframe 
    for col in df:
        for i in range(len(df[col])-1):
            transition_matrix[(df[col][i], df[col][i+1])]+=1
    #get the denominator for the transition matrix
    num_transitions = sum(transition_matrix.values())
    #python 3 use 
    #for key, value in color_transitions.items()
    for key, value in transition_matrix.iteritems():
        #updating the transitions matrix into a probability matrix (an actual transition matrix)
        transition_matrix[key] = value/ float(num_transitions) # no need for float conversion in python 3
    return transition_matrix

