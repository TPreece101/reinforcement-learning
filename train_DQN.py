from Game import Game
from DQNAgent import DQNAgent

if __name__ == "__main__":

    MAX_NUM_TURNS = 30
    EPISODES = 1000
    ACTIONS = [0,1,2,3]

    agent = DQNAgent(state_size=4, action_size=4)
    first_train = True

    for e in range(EPISODES):
        # Initalize game
        game = Game()

        cum_reward = 0
        for i in range(MAX_NUM_TURNS):
            # Get current state
            curr_state = list(game.state)

            # Decide action
            action = agent.act(curr_state)

            # Play action
            new_state, reward = game.play(action)

            # Remember the previous state, action, reward, and done
            agent.remember(curr_state, action, reward, new_state, game.isEnd())

            # Update cum reward
            cum_reward += reward

            # Check if end
            if game.isEnd():
                break
        
        print(f"Game {e}/{EPISODES} finished Num Turns: {i} final reward: {cum_reward}")

        # Train the agent with the experience of the episode
        if i >= 16 or first_train is False:
            agent.replay(16)
            first_train = False
