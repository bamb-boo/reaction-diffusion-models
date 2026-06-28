import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap

# initializaiton
dU, dV = 0.2, 0.1
k, f = 0.05204, 0.01887
time_steps = 1000
grid_size = 128  

U = []
V = []
for r in range(grid_size):
    row_u = []
    row_v = []
    for c in range(grid_size):
        row_u.append(1.0)
        row_v.append(0.0)
    U.append(row_u)
    V.append(row_v)

# generating random disturbance
r_size = 10
center = (grid_size // 2) + 1
for r in range(center - r_size, center + r_size):
    for c in range(center - r_size, center + r_size):
        U[r][c] = 0.50
        V[r][c] = 0.25 + random.uniform(-0.02, 0.02)

ortho = 1.0 / 6.0
diag = 0.5 / 6.0
center = -6.0 / 6.0

# colormap
cmap1 = plt.get_cmap('Reds', 128)
cmap2 = plt.get_cmap('YlGn', 128)
colors_list = []
for i in range(128):
    colors_list.append(cmap1(i / 127.0))
for i in range(128):
    colors_list.append(cmap2(i / 127.0))
Purples_YlGnBu = ListedColormap(colors_list)

fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(V, cmap=Purples_YlGnBu, vmin=0, vmax=1, interpolation='bilinear')
ax.axis('off')

# pde + diffusion
def update(frame):
    global U, V
    next_U = []
    next_V = []
    for r in range(grid_size):
        u_row = []
        v_row = []
        for c in range(grid_size):
            u_row.append(1.0)
            v_row.append(0.0)
        next_U.append(u_row)
        next_V.append(v_row)

    for r in range(1, grid_size + 1):
        for c in range(1, grid_size + 1):

            lap_u = (center * U[r][c] +
                     ortho  * (U[r][c-1] + U[r][c+1] + U[r-1][c] + U[r+1][c]) +
                     diag   * (U[r-1][c-1] + U[r-1][c+1] + U[r+1][c-1] + U[r+1][c+1]))
                     
            lap_v = (center * V[r][c] +
                     ortho  * (V[r][c-1] + V[r][c+1] + V[r-1][c] + V[r+1][c]) +
                     diag   * (V[r-1][c-1] + V[r-1][c+1] + V[r+1][c-1] + V[r+1][c+1]))
            nu = U[r][c] + dU * lap_u - (U[r][c] * V[r][c] * V[r][c]) + f * (1.0 - U[r][c])
            nv = V[r][c] + dV * lap_v + (U[r][c] * V[r][c] * V[r][c]) - (k + f) * V[r][c]

            next_U[r][c] = max(0.0, min(1.0, nu))
            next_V[r][c] = max(0.0, min(1.0, nv))
            
    U = next_U
    V = next_V
    im.set_data(V)
    return [im]

ani = FuncAnimation(fig, update, frames=time_steps, blit=True, interval=1)
plt.tight_layout()
plt.show()
