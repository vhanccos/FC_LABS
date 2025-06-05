import numpy as np
import matplotlib.pyplot as plt

plt.clf()
xa = np.arange(-2, 2.5, 0.5)
ya = np.arange(-2, 2.5, 0.5)
k = 1.0
q1 = 1
q2 = -1
x1 = 1
x2 = -1
x, y = np.meshgrid(xa, ya)

Ex = (
    k * q1 * (x - x1) / ((x - x1) ** 2 + y**2) ** 1.5
    + k * q2 * (x - x2) / ((x - x2) ** 2 + y**2) ** 1.5
)
Ey = (
    k * q1 * y / ((x - x1) ** 2 + y**2) ** 1.5
    + k * q2 * y / ((x - x2) ** 2 + y**2) ** 1.5
)

plt.quiver(x, y, Ex, Ey)
plt.axis("square")
plt.title("Campo Eléctrico de un Dipolo")
plt.show()
