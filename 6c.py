import numpy as np
import matplotlib.pyplot as plt

k = 9e9
q = 1e-9
lado = 0.01
n = 2
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
    signo *= -1

# Lados
for i in range(1, n + 1):
    x = -lado / 2 + i * sep
    y = lado / 2
    cargas.append((signo * q, x, y))
    signo *= -1

for i in range(1, n + 1):
    x = lado / 2
    y = lado / 2 - i * sep
    cargas.append((signo * q, x, y))
    signo *= -1

for i in range(1, n + 1):
    x = lado / 2 - i * sep
    y = -lado / 2
    cargas.append((signo * q, x, y))
    signo *= -1

for i in range(1, n + 1):
    x = -lado / 2
    y = -lado / 2 + i * sep
    cargas.append((signo * q, x, y))
    signo *= -1

# Malla para graficar el potencial
x_vals = np.linspace(-0.02, 0.02, 200)
y_vals = np.linspace(-0.02, 0.02, 200)
x, y = np.meshgrid(x_vals, y_vals)

# Cálculo del potencial eléctrico
V = np.zeros_like(x)
for qi, xi, yi in cargas:
    r = np.sqrt((x - xi) ** 2 + (y - yi) ** 2) + 1e-20
    V += k * qi / r

# Niveles para las líneas equipotenciales
zmax = np.max(V)
zmin = np.min(V)
dz = (zmax - zmin) / 400
nivel = np.arange(zmin, zmax, dz)

# Gráfico del potencial
plt.figure(figsize=(6, 6))
plt.contour(x, y, V, nivel)
plt.scatter([c[1] for c in cargas], [c[2] for c in cargas], c="red")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("Líneas Equipotenciales")
plt.axis("square")
plt.grid(True)
plt.show()

