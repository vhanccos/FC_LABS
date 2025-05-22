import numpy as np
import matplotlib.pyplot as plt

h = 0.1
tfin = 60
k = 0.1
m = 0.2
c = 0.05
f0 = 0.01
w = 0.3

t1 = 0
x1 = -1
v1 = 1

pt1 = [t1]
px1 = [x1]
pv1 = [v1]
pa1 = []

t2 = 0
x2 = -1
v2 = 1

pt2 = [t2]
px2 = [x2]
pv2 = [v2]
pa2 = []

while t1 <= tfin:
    a1 = (-k * x1 - c * v1) / m
    v1 += h * a1
    x1 += h * v1
    t1 += h

    pt1.append(t1)
    px1.append(x1)
    pv1.append(v1)
    pa1.append(a1)

while t2 <= tfin:
    a2 = (-k * x2 - c * v2 + f0 * np.sin(w * t2)) / m
    # a2 = (-k * x2 - c * v2 + f0 * np.cos(w)) / m
    v2 += h * a2
    x2 += h * v2
    t2 += h

    pt2.append(t2)
    px2.append(x2)
    pv2.append(v2)
    pa2.append(a2)

pa1 = [pa1[0]] + pa1
pa2 = [pa2[0]] + pa2

plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
plt.plot(pt1, pa1)
plt.plot(pt2, pa2)
plt.grid(True)
plt.xlabel("Tiempo (s)")
plt.ylabel("Aceleración (m/s²)")
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(pt1, pv1)
plt.plot(pt2, pv2)
plt.grid(True)
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(pt1, px1)
plt.plot(pt2, px2)
plt.grid(True)
plt.xlabel("Tiempo (s)")
plt.ylabel("Desplazamiento (m)")
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(px1, pv1)
plt.plot(px2, pv2)
plt.grid(True)
plt.xlabel("Desplazamiento (m)")
plt.ylabel("Velocidad (m/s)")

plt.tight_layout()
plt.show()
