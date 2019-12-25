# state-matrix-to-transition-matrix
Code for translating a state matrix to a transition matrix representation using Python pandas

This code assumes you have a state matrix in a dataframe with time as the index column and fixed intervals between time periods
and require the output of transitions probabilities. The transition probabilities are outputted as a Counter object with the 
transitions as the keys.    

The code is initially written in Python 2 but is compatible with Python 3. 
