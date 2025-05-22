import numpy as np
import matplotlib.pyplot as plt

h = 0.001
tfin = 20

l = 4
n = 5
m1 = m2 = 1
k1 = l**2
k2 = n**2

x = 1
vx = 2.36
y = 1
vy = 0
t = 0

px = []
py = []

while t <= tfin:
    ax = -k1 * x / m1
    vx += h * ax
    x += h * vx

    ay = -k2 * y / m2
    vy += h * ay
    y += h * vy

    px.append(x)
    py.append(y)

    t += h

plt.figure(figsize=(6, 6))
plt.plot(px, py)
# plt.title(f"Figuras de Lissajous para l={l}, n={n}")
plt.xlabel("x(t)")
plt.ylabel("y(t)")
plt.grid(True)
plt.axis("equal")
plt.show()
