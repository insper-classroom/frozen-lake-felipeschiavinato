import gymnasium as gym
import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt
import sys

epsilon_decs = [0.9994, 0.9995, 0.9996, 0.9997, 0.9998, 0.99985, 0.99987, 0.9999, 0.99991, 0.99992, 0.99993, 0.99994, 0.99995, 0.99996, 0.99997, 0.99998, 0.99999]

bar_list = [[],[],[],[]]
for epsilon_dec in epsilon_decs:
    print(epsilon_dec)

    samples = []
    for i in range(0,100):
        env = gym.make('FrozenLake-v1', map_name="8x8", render_mode='ansi').env
        q_table = loadtxt(f'data/q-table-{epsilon_dec}.csv', delimiter=',')

        rewards = 0

        print(f'Episode {i+1}')
        for i in range(0,1000):    
            (state, _) = env.reset()
            done = False
            while not done:
                action = np.argmax(q_table[state])
                state, reward, done, _, info = env.step(action)
            rewards += reward
        samples.append(rewards)

    min = np.min(samples)
    max = np.max(samples)
    mean = np.mean(samples)
    std = np.std(samples)
    bar_list[0].append(max)
    bar_list[1].append(mean)
    bar_list[2].append(min)
    bar_list[3].append(std)
    print(bar_list)


# bar_list = [[902.0, 931.0, 894.0, 919.0, 928.0, 829.0, 925.0, 922.0, 915.0, 917.0, 911.0, 820.0, 914.0, 996.0, 956.0], [877.15, 905.8, 874.01, 897.15, 908.28, 800.82, 900.38, 883.87, 889.8, 892.21, 891.91, 793.67, 893.37, 991.78, 940.93], [849.0, 876.0, 846.0, 876.0, 882.0, 776.0, 872.0, 860.0, 862.0, 873.0, 860.0, 770.0, 866.0, 983.0, 923.0], [10.055222523644119, 9.588534820294495, 9.454623207722241, 9.326708958684193, 9.175053133361136, 11.175312076179349, 11.126347109451512, 9.546365800659432, 9.682974749528162, 9.714211239210314, 10.451884997453808, 11.930678941284105, 9.047270306562085, 2.773373397146515, 6.822396939492746]]
X = np.arange(len(epsilon_decs))
plt.barh(X + 0.00, bar_list[0], color = 'skyblue', height = 0.25)
plt.barh(X + 0.25, bar_list[1], color = 'gold', height = 0.25)
plt.barh(X + 0.50, bar_list[2], color = 'tomato', height = 0.25)
plt.yticks(X, epsilon_decs)
plt.xlabel('Rewards')
plt.title('Frozen Lake Rewards')
plt.legend(['Max', 'Mean', 'Min', 'Std'])
plt.grid()
plt.show()

