import gymnasium as gym
import numpy as np
from numpy import loadtxt

epsilon_dec= 0.99999

def test_01(): 

    env = gym.make("FrozenLake-v1", map_name="8x8", is_slippery=True).env
    q_table = loadtxt(f'data/q-table-{epsilon_dec}.csv', delimiter=',')
    rewards = 0

    for i in range(0,1000):    
        (state, _) = env.reset()
        done = False
        while not done:
            action = np.argmax(q_table[state])
            state, reward, done, _, info = env.step(action)
        rewards += reward
    print(rewards)
    assert rewards >= 700

def test_02(): 

    env = gym.make("FrozenLake-v1", map_name="8x8", is_slippery=True).env
    q_table = loadtxt(f'data/q-table-{epsilon_dec}.csv', delimiter=',')
    rewards = 0

    for i in range(0,1000):    
        (state, _) = env.reset()
        done = False
        while not done:
            action = np.argmax(q_table[state])
            state, reward, done, _, info = env.step(action)
        rewards += reward
    print(rewards)
    assert rewards >= 800

def test_03(): 

    env = gym.make("FrozenLake-v1", map_name="8x8", is_slippery=True).env
    q_table = loadtxt(f'data/q-table-{epsilon_dec}.csv', delimiter=',')
    rewards = 0

    for i in range(0,1000):    
        (state, _) = env.reset()
        done = False
        while not done:
            action = np.argmax(q_table[state])
            state, reward, done, _, info = env.step(action)
        rewards += reward
    print(rewards)
    assert rewards >= 800

def test_04(): 

    env = gym.make("FrozenLake-v1", map_name="8x8", is_slippery=True).env
    q_table = loadtxt(f'data/q-table-{epsilon_dec}.csv', delimiter=',')
    rewards = 0

    for i in range(0,1000):    
        (state, _) = env.reset()
        done = False
        while not done:
            action = np.argmax(q_table[state])
            state, reward, done, _, info = env.step(action)
        rewards += reward
    print(rewards)
    assert rewards >= 800