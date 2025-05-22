import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

h = 0.1
tfin = 3
k = 0.1
m = 0.2
c = 0.5


t = 0
x = 0
v = -2
n = 0

pt = [t]
px = [x]
pv = [v]
pa = []


def armonico(x, k, m):
    return -k * x / m


def friccion(x, k, m):
    return -c * v / m


def armonico_friccion(x, k, m):
    return -k * x / m - c * v / m


while t <= tfin:
    n += 1
    a = armonico_friccion(x, k, m)
    v = v + h * a
    x = x + h * v
    t = t + h

    pt.append(t)
    px.append(x)
    pv.append(v)
    pa.append(a)

pa = [pa[0]] + pa

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.plot(pv, px, pt, color="blue")

plt.tight_layout()
# plt.show()

plt.figure(figsize=(8, 6))
plt.plot(px, pv, color="blue")
plt.xlabel("Posición (x)")
plt.ylabel("Velocidad (v)")
plt.title("Espacio de Fases (x vs v)")
plt.grid(True)
plt.show()

print((x / (2 * m)) ** 2, (k / m) ** 2)
