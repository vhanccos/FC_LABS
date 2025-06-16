import numpy as np
import matplotlib.pyplot as plt
import time

plt.clf()
plt.grid(True)

# Condiciones Iniciales
v = 1.0
tfin = 8

# Inicio de la simulación
for t in np.arange(0, tfin + 0.1, 2.0):
    px = []
    py = []

    for ix in np.arange(-1, 1.01, 0.01):
        x = ix + v * t
        y = x - v * t
        px.append(x)
        py.append(y)

    plt.plot(px, py)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.pause(0.2)

plt.show()
