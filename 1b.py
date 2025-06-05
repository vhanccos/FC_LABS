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

x_vals = np.linspace(-0.02, 0.02, 40)
y_vals = np.linspace(-0.02, 0.02, 40)
x, y = np.meshgrid(x_vals, y_vals)

Ex = np.zeros_like(x)
Ey = np.zeros_like(y)

for qi, xi, yi in cargas:
    dx = x - xi
    dy = y - yi
    r_squared = dx**2 + dy**2
    r_cubed = r_squared**1.5 + 1e-20
    Ex += k * qi * dx / r_cubed
    Ey += k * qi * dy / r_cubed

plt.figure(figsize=(6, 6))
plt.quiver(x, y, Ex, Ey, color="blue")
plt.scatter([c[1] for c in cargas], [c[2] for c in cargas], c="red")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.axis("square")
plt.grid(True)
plt.show()
