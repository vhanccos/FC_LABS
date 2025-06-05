import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.clf()
xa = np.arange(-2.1, 2.12, 0.12)
ya = np.arange(-2.1, 2.12, 0.12)
k = 1.0
q1 = 1
q2 = -1
x1 = 1
x2 = -1
x, y = np.meshgrid(xa, ya)

z = k * q1 / np.sqrt((x - x1) ** 2 + y**2) + k * q2 / np.sqrt((x - x2) ** 2 + y**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(x, y, z, cmap="viridis")
ax.set_title("Potencial Eléctrico 3D")
plt.show()
