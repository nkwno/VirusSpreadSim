import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Different states a cell can be
HEALTHY = 0
INFECTED = 1
RECOVERED = 2
DEAD = 3

# size of the grid (population size)
GRID_SIZE = 50

# Probabilities
P_INFECT = 0.3
P_RECOVER = 0.7

#number of "time" steps a cell has spent in an infected state before it has a chance to die or recover
T_INFECTED = 5

# init grid
np.random.seed(42)
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
infection_timer = np.zeros_like(grid)

# infect the middle to start
grid[GRID_SIZE // 2, GRID_SIZE // 2] = INFECTED

# colors that are associated with different states
colors = {
    HEALTHY: 'lightgreen',
    INFECTED: 'red',
    RECOVERED: 'blue',
    DEAD: 'black'
}
cmap = plt.matplotlib.colors.ListedColormap([colors[i] for i in range(4)])


def update(frame):
    global grid, infection_timer
    new_grid = grid.copy()
    new_timer = infection_timer.copy()

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i, j] == HEALTHY:
                # check neighbors for infection
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < GRID_SIZE and 0 <= nj < GRID_SIZE:
                        if grid[ni, nj] == INFECTED and np.random.rand() < P_INFECT:
                            new_grid[i, j] = INFECTED
                            break
            elif grid[i, j] == INFECTED:
                new_timer[i, j] += 1
                if new_timer[i, j] >= T_INFECTED:
                    if np.random.rand() < P_RECOVER:
                        new_grid[i, j] = RECOVERED
                    else:
                        new_grid[i, j] = DEAD
    grid = new_grid
    infection_timer = new_timer
    mat.set_data(grid)
    return [mat]


# setting up the plot
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap=cmap, vmin=0, vmax=3)
plt.title("Virus Spread Automaton")

ani = animation.FuncAnimation(fig, update, interval=500, frames=50, repeat=False)
plt.show()