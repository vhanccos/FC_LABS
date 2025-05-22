import numpy as np
import matplotlib.pyplot as plt

h = 0.1
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

pa = [pa[0]] + pa

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(pt, pa)
plt.grid(True)
plt.xlabel("Tiempo (s)")
plt.ylabel("Aceleración (m/s²)")

plt.subplot(2, 2, 2)
plt.plot(pt, pv)
plt.grid(True)
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")

plt.subplot(2, 2, 3)
plt.plot(pt, px)
plt.grid(True)
plt.xlabel("Tiempo (s)")
plt.ylabel("Desplazamiento (m)")

plt.subplot(2, 2, 4)
plt.plot(px, pv)
plt.grid(True)
plt.xlabel("Desplazamiento (m)")
plt.ylabel("Velocidad (m/s)")

plt.tight_layout()
plt.show()
