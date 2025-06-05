import numpy as np
import matplotlib.pyplot as plt

k = 9e9
q = -1e-9

lado = 0.01
radio = lado

cargas = []
for i in range(6):
    angulo = np.pi / 3 * i
    xi = radio * np.cos(angulo)
    yi = radio * np.sin(angulo)
    cargas.append((q, xi, yi))

x_vals = np.linspace(-0.03, 0.03, 100)
y_vals = np.linspace(-0.03, 0.03, 100)
x, y = np.meshgrid(x_vals, y_vals)

z = np.zeros_like(x)
for qi, xi, yi in cargas:
    r = np.sqrt((x - xi) ** 2 + (y - yi) ** 2) + 1e-20
    z += k * qi / r

zmax = np.max(z)
zmin = np.min(z)
dz = (zmax - zmin) / 50
niveles = np.arange(zmin, zmax, dz)

plt.figure(figsize=(6, 6))
plt.contour(x, y, z, niveles, colors="purple")
plt.scatter([c[1] for c in cargas], [c[2] for c in cargas], c="red")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.axis("square")
plt.title("Líneas equipotenciales")
plt.grid(True)
plt.show()
