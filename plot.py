from utils import load_list_from_file
import matplotlib.pyplot as plt
import numpy as np

epsilon_decs = [0.9994, 0.9995, 0.9996, 0.9997, 0.9998, 0.99985, 0.99987, 0.9999, 0.99991, 0.99992, 0.99993, 0.99994, 0.99995, 0.99996, 0.99997, 0.99998, 0.99999]

for epsilon_dec in epsilon_decs:
    rewards_per_episode = load_list_from_file(f'data/rewards_per_episode_{epsilon_dec}.pkl')


    weights = np.repeat(1.0, 5000) / 5000
    moving_average = np.convolve(rewards_per_episode, weights, 'valid')

    plt.plot(moving_average, label=r'$\epsilon$ = {}'.format(epsilon_dec))


plt.xlabel('Episodes')
plt.ylabel(r'$\sum$ '  + 'Rewards')
plt.grid()
plt.title('Frozen Lake Rewards')
# plt.legend()
plt.show()