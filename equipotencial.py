import numpy as np
import matplotlib.pyplot as plt

plt.clf()
xa = np.arange(-2.1, 2.12, 0.12)
ya = np.arange(-2.1, 2.12, 0.12)
k = 1.0
q1 = 1
q2 = 1
x1 = 1
x2 = -1
x, y = np.meshgrid(xa, ya)

z = k * q1 / np.sqrt((x - x1) ** 2 + y**2) + k * q2 / np.sqrt((x - x2) ** 2 + y**2)
zmax = np.max(z)
zmin = np.min(z)
dz = (zmax - zmin) / 400
nivel = np.arange(zmin, zmax, dz)

plt.contour(x, y, z, nivel)
plt.axis("square")
plt.title("Líneas Equipotenciales")
plt.show()
