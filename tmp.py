import numpy as np
import matplotlib.pyplot as plt

v = 1.0
tfin = 16
dt = 2 * np.pi

plt.figure()
plt.grid(True)

for t in np.arange(0, tfin + dt, dt):
    px = []
    py = []

    for ix in np.arange(0, 2 * np.pi + 0.01, 0.01):
        x = ix + v * t

        phase = ix % (2 * np.pi)

        if phase < np.pi:
            y = -(2 / np.pi) * phase
        else:
            y = -(2 / np.pi) * (2 * np.pi - phase)

        px.append(x)
        py.append(y)

    plt.plot(px, py)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.pause(0.2)

plt.show()

