import numpy as np
import math
import matplotlib.pyplot as plt


def bias_variance_dartboard():

    # Dartboard example
    N_DARTS = 20
    LABEL_SIZE = 14
    fig, axes = plt.subplots(2, 2, subplot_kw=dict(polar=True))
    fig.set_size_inches((8, 8))
    theta = np.linspace(0, 2*math.pi, 1000)

    data = np.array([[
        # low-bias, low-variance
        [np.random.uniform(0, 2*math.pi, N_DARTS),
        np.random.uniform(0, 2, N_DARTS)], 
        # high-bias, low-variance
        [np.random.normal(3, 0.2, N_DARTS),
        np.random.normal(5, 0.5, N_DARTS)]],
        # low-bias, high-variance
        [[np.linspace(0, 2*math.pi, N_DARTS),
        np.random.uniform(0, 6, N_DARTS)],
        # high-bias, high-variance
        [np.random.normal(3, 0.5, N_DARTS),
        np.random.uniform(2, 9.8, N_DARTS)]
        ]])

    for i in range(2):
        for j in range(2):
            ax = axes[i,j]
            for k in range(4):
                ax.plot(theta, np.ones_like(theta)*k*3+0.4, lw=5, c='red',
                        alpha=0.5)
            ax.set_ylim(0, 11)
            ax.set_xticks([])
            ax.set_yticks([])
            x = data[i, j, 0, :]
            y = data[i, j, 1, :]
            ax.scatter(x, y, marker='x', c='navy', s=70, lw=1.6, zorder=100)
        axes[0,0].set_title('Low bias', fontsize=LABEL_SIZE)
        axes[0,1].set_title('High bias', fontsize=LABEL_SIZE)
        axes[0,0].set_ylabel('Low variance', fontsize=LABEL_SIZE, labelpad=20)
        axes[1,0].set_ylabel('High variance', fontsize=LABEL_SIZE, labelpad=20)
