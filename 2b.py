import numpy as np
import matplotlib.pyplot as plt

k = 9e9
q = -1e-9

cargas = [
    (q, 0.005, 0.005),
    (q, -0.005, 0.005),
    (q, -0.005, -0.005),
    (q, 0.005, -0.005),
]

x_vals = np.linspace(-0.02, 0.02, 200)
y_vals = np.linspace(-0.02, 0.02, 200)
x, y = np.meshgrid(x_vals, y_vals)

V = np.zeros_like(x)
for qi, xi, yi in cargas:
    r = np.sqrt((x - xi) ** 2 + (y - yi) ** 2) + 1e-20
    V += k * qi / r

zmax = np.max(V)
zmin = np.min(V)
dz = (zmax - zmin) / 400
nivel = np.arange(zmin, zmax, dz)

plt.figure(figsize=(6, 6))
plt.contour(x, y, V, nivel)
plt.scatter([c[1] for c in cargas], [c[2] for c in cargas], c="red")
plt.axis("square")
plt.show()
