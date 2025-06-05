import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Necesario para 3D

k = 9e9
q = 1e-9
lado = 0.01
n = 18
sep = lado / (n + 1)

cargas = []
signo = 1

# Esquinas
esquinas = [
    (lado / 2, lado / 2),
    (-lado / 2, lado / 2),
    (-lado / 2, -lado / 2),
    (lado / 2, -lado / 2),
]
for x, y in esquinas:
    cargas.append((signo * q, x, y))
    signo *= -1  # Intercalamos signos

# Lados
for i in range(1, n + 1):
    cargas.append((signo * q, -lado / 2 + i * sep, lado / 2))
    signo *= -1
for i in range(1, n + 1):
    cargas.append((signo * q, lado / 2, lado / 2 - i * sep))
    signo *= -1
for i in range(1, n + 1):
    cargas.append((signo * q, lado / 2 - i * sep, -lado / 2))
    signo *= -1
for i in range(1, n + 1):
    cargas.append((signo * q, -lado / 2, -lado / 2 + i * sep))
    signo *= -1

# Malla de evaluación
x_vals = np.linspace(-0.02, 0.02, 200)
y_vals = np.linspace(-0.02, 0.02, 200)
x, y = np.meshgrid(x_vals, y_vals)

# Potencial eléctrico
V = np.zeros_like(x)
for qi, xi, yi in cargas:
    r = np.sqrt((x - xi) ** 2 + (y - yi) ** 2) + 1e-20
    V += k * qi / r

# Gráfico en 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(x, y, V, cmap="viridis", linewidth=0, antialiased=True)

ax.set_title("Potencial Eléctrico 3D")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("V [V]")
plt.tight_layout()
plt.show()
