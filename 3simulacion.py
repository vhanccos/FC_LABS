import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

h = 0.05
tfin = 60
k = 0.1
m = 0.2
c = 0.05
f0 = 0.01
w = 0.3

x1 = x2 = -1
v1 = v2 = 1
t = 0

pt = []
px1 = []
px2 = []

fig, ax = plt.subplots()
(line1,) = ax.plot([], [], color="blue", label="Sin fuerza externa")
(line2,) = ax.plot([], [], color="orange", label="Con fuerza externa")

ax.set_xlim(0, tfin)
ax.set_ylim(-2, 2)
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Desplazamiento (m)")
ax.grid(True)
ax.legend()


def update(frame):
    global x1, v1, x2, v2, t

    if t >= tfin:
        ani.event_source.stop()
        return line1, line2

    a1 = (-k * x1 - c * v1) / m
    v1 += h * a1
    x1 += h * v1

    a2 = (-k * x2 - c * v2 + f0 * np.sin(w * t)) / m
    v2 += h * a2
    x2 += h * v2

    t += h
    pt.append(t)
    px1.append(x1)
    px2.append(x2)

    line1.set_data(pt, px1)
    line2.set_data(pt, px2)
    ax.set_xlim(0, max(tfin, t + 1))

    return line1, line2


ani = FuncAnimation(fig, update, interval=5, blit=True)
plt.show()

