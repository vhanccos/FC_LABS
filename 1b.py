import numpy as np
import matplotlib.pyplot as plt

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

pa = [pa[0]] + pa

ux = [0.5 * k * xi**2 for xi in px]
kx = [0.5 * m * vi**2 for vi in pv]
ex = [u + ke for u, ke in zip(ux, kx)]

plt.figure(figsize=(8, 6))
plt.plot(px, ux, label="Energía Potencial (u)", color="blue")
plt.plot(px, kx, label="Energía Cinética (k)", color="red")
plt.plot(px, ex, label="Energía Total (e)", color="green")
plt.grid(True)
# plt.legend()
plt.tight_layout()
plt.show()
