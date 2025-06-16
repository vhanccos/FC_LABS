import numpy as np
import matplotlib.pyplot as plt
import time

plt.clf()
plt.grid(True)

# Condiciones Iniciales
v = 1.0
tfin = 16
dt = 2 * np.pi

# Inicio de la simulación
for t in np.arange(0, tfin + dt, dt):
    px = []
    py = []

    for ix in np.arange(0, 2 * np.pi + 0.01, 0.01):
        x = ix + v * t
        mod = ix % (2 * np.pi)
        if mod < np.pi / 3:
            y = (6 / np.pi) * (x - v * t)
        if mod > 1 * np.pi / 3 and mod < 2 * np.pi / 3:
            y = 2
        if mod > 2 * np.pi / 3 and mod < 3 * np.pi / 3:
            y = -(6 / np.pi) * (x - v * t) + 6
        if mod > 3 * np.pi / 3 and mod < 4 * np.pi / 3:
            y = -(6 / np.pi) * (x - v * t) + 6
        if mod > 4 * np.pi / 3 and mod < 5 * np.pi / 3:
            y = -2
        else:
            y = (6 / np.pi) * (x - v * t)

        px.append(x)
        py.append(y)

    plt.plot(px, py)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.pause(0.2)

plt.show()
