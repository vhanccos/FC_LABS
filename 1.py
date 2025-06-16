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

    for ix in np.arange(-2 * np.pi, 0.01, 0.01):
        x = ix + v * t
        # y = x - v * t
        y = (1 / np.pi) * (x - v * t) + 2
        px.append(x)
        py.append(y)

    plt.plot(px, py)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.pause(0.2)

plt.show()
