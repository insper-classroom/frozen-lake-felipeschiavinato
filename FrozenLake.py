from IPython.display import clear_output
import gymnasium as gym
import numpy as np
from QLearning import QLearning
from numpy import loadtxt
import warnings
import matplotlib.pyplot as plt
from utils import *
warnings.simplefilter("ignore")# exemplo de ambiente nao determinístico

epsilon_decs = [0.99998, 0.99999]

for epsilon_dec in epsilon_decs:
    env = gym.make('FrozenLake-v1',map_name="8x8").env

    # only execute the following lines if you want to create a new q-table
    qlearn = QLearning(env, alpha=0.1, gamma=0.99, epsilon=0.9999, epsilon_min=0.0001, epsilon_dec=epsilon_dec, episodes=100000)
    q_table, rewards_per_episode = qlearn.train(f'data/q-table-{epsilon_dec}.csv',f'results/frozen_lake_qlearning_{epsilon_dec}')
    q_table = loadtxt(f'data/q-table-{epsilon_dec}.csv', delimiter=',')

    env = gym.make('FrozenLake-v1',map_name="8x8").env

    (state, _) = env.reset()
    epochs = 0
    rewards = 0
    done = False
        
    while not done:
        action = np.argmax(q_table[state])
        state, reward, done, _, info = env.step(action)
        epochs += 1
        rewards += reward

    print("\n")
    print("Timesteps taken: {}".format(epochs))
    print("Rewards: {}".format(rewards))

    save_list_to_file(rewards_per_episode, f'data/rewards_per_episode_{epsilon_dec}.pkl')
