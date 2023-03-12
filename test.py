import matplotlib.pyplot as plt
import numpy as np

epsilon = 0.9999
limit_list = []
epsilon_decs = [0.999, 0.9991, 0.9992, 0.9993, 0.9994, 0.9995, 0.9996, 0.9997, 0.9998, 0.99985, 0.99987, 0.9999, 0.99991, 0.99992, 0.99993, 0.99994, 0.99995, 0.99996, 0.99997]
epsilon_list_list = []


for epsilon_dec in epsilon_decs:
    print(epsilon_dec)
    epsilon_list = []
    epsilon = 0.9999
    flag = False
    for i in range(100000):
        epsilon = epsilon * epsilon_dec
        epsilon_list.append(epsilon)
        if epsilon < 0.0001 and not flag:
            limit = i
            limit_list.append(limit)
            flag = True
    
    if(not flag):
        limit_list.append(100000)
    epsilon_list_list.append(epsilon_list)

print(len(epsilon_list_list))
i = 0
for epsilon_list, limit in zip(epsilon_list_list, limit_list):
    plt.plot(epsilon_list, label=r'$\epsilon=${}'.format(epsilon_decs[i]))
    # plt.axvline(x = limit, label=f'limit={limit}')
    i += 1

plt.xlabel('Episodes')
plt.ylabel('Epsilon')
plt.title('Epsilon Decay')
plt.legend()
plt.show()

