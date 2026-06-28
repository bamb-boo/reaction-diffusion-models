import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
import random
import scipy.signal as sp
from matplotlib.animation import FFMpegWriter
import os
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

# diffusion rates
dU = 0.2
dV = 0.1

# default feed kill rate
#f = 0.055
#k = 0.062

# worms
# f = 0.025
# k = 0.056

# "mitosis" simulation
# f = 0.0367
# k = 0.0649

# "coral growth" simulation
# f = 0.0545
# k = 0.062

# spagetti
# k = 0.06264
# f = 0.06100

# big patches
# k = 0.05207
# f = 0.10950

# swirls
k = 0.05204
f = 0.01887

# User inputs
initial_V = 0.5
time_steps = 200
grid_size = 512


# Grid 
U = np.ones((grid_size, grid_size)) 
V = np.full((grid_size, grid_size), initial_V)

# Disturbance
def initialise_v(x):
    if random.random() < 0.05:  
        return 1
    else:
        return 0
initialise_v_vf = np.vectorize(initialise_v)

V = initialise_v_vf(V)



ani = matplotlib.animation.FuncAnimation(fig, update, frames = time_steps, init_func=init, blit=True, interval=10)
text = f"Kill rate: {k}\nFeed rate: {f}"
plt.text(550, 300, text, fontsize = 12)
plt.show()
