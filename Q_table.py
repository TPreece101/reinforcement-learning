import random
import numpy as np
from itertools import product

from Game import Game

if __name__ == "__main__":
    
    MAX_NUM_TURNS = 30
    EPISODES = 1000
    ACTIONS = [0,1,2,3]

    # Discount rate
    gamma = 0.05
    # Epsilon
    epsilon = 0.2

    # Build Q table
    ## Create a dictionary for each state which holds a list of Q values for each possible action
    Q_table = {}

    for a,b,c,d in product(range(2), repeat=4):
        tmpList = [a,b,c,d]
        Q_table[str(tmpList)] = np.zeros(4)
    
    print(Q_table)

    for e in range(EPISODES):
        # Initalize game
        game = Game()

        cum_reward = 0
        for i in range(MAX_NUM_TURNS):
            # Get current state
            curr_state = list(game.state)
            if random.random() < epsilon:
                # Select a random action
                action = random.choice(ACTIONS)
            else:
                # Choose move using Q table
                action = np.argmax(Q_table[str(curr_state)])

            # Play action
            new_state, reward = game.play(action)

            # Update Q table entry according to Bellman's equation
            r_sa = reward
            max_Q = max(Q_table[str(new_state)])
            Q_table[str(curr_state)][action] = r_sa + (gamma * max_Q)  

            # Update cum reward
            cum_reward += reward
            # Check if end
            if game.isEnd():
                break
        
        print("Game finished, final reward: ", cum_reward)

    print(Q_table)
