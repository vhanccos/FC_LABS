import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

h = 0.01
tfin = 30
k = 1
m = 2

t = 0
x = 1
v = 0
n = 0

pt = [t]
px = [x]
pv = [v]
pa = []


def armonico(x, k, m):
    return -k * x / m


while t <= tfin:
    n += 1
    a = armonico(x, k, m)
    v = v + h * a
    x = x + h * v
    t = t + h

    pt.append(t)
    px.append(x)
    pv.append(v)
    pa.append(a)

ux = [0.5 * k * xi**2 for xi in px]
kx = [0.5 * m * vi**2 for vi in pv]
ex = [u + ke for u, ke in zip(ux, kx)]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection="3d")
ax.plot(pv, px, pt, color="blue")

plt.tight_layout()
plt.show()
