'''
Rules of the game:
    *   4 squares
    *   A turn involves putting a counter on a square
    *   If square empty then reward is +1
    *   If square full then reward is -1
    *   Game ends when all squares are full

State:
    List of length 4 [0,0,0,0]
    0 when no counter is present
    1 when counter is present

Possible actions:
    4 possilbe actions 0,1,2,3
'''

class Game:
    def __init__(self):
        # Initalize state of the game
        self.state = [0,0,0,0]
    
    def play(self, action):
        # Calculate reward
        reward = 1 if self.state[action] == 0 else -1
        # Update state
        self.state[action] = 1
        # Return new state and reward
        return (self.state, reward)

    def isEnd(self):
        output = True if sum(self.state)==4 else False
        return output