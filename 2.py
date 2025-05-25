import numpy as np
import matplotlib.pyplot as plt

h = 0.01
k = 0.05
tfin = 30
lim = 7
r_limite = 3


def ax(x, y):
    r2 = x**2 + y**2
    if r2 == 0:
        return 0
    return -x / (r2 ** (3 / 2))


def ay(x, y):
    r2 = x**2 + y**2
    if r2 == 0:
        return 0
    return -y / (r2 ** (3 / 2))


plt.figure()

for vx0 in np.arange(0.01, 3 + k, k):
    vy = 0.0
    y = -4
    x = 0
    vx = vx0

    px = [x]
    py = [y]
    t = 0

    while t <= tfin:
        if np.sqrt(x**2 + y**2) <= r_limite:
            t += h
            continue

        x += vx * h
        y += vy * h
        vx += ax(x, y) * h
        vy += ay(x, y) * h

        px.append(x)
        py.append(y)
        t += h

    if abs(x) > lim or abs(y) > lim:
        continue

    plt.plot(px, py)

theta = np.linspace(0, 2 * np.pi, 200)
circle_x = r_limite * np.cos(theta)
circle_y = r_limite * np.sin(theta)
plt.plot(circle_x, circle_y, "b")

plt.axis("equal")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
