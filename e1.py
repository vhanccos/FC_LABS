import numpy as np
import matplotlib.pyplot as plt


def circulo(r, cx, cy):
    t = np.linspace(0, 2 * np.pi, 100)
    x = r * np.cos(t) - cx
    y = r * np.sin(t) - cy

    plt.plot(x, y, "b")


r = 1
b = 2
c = 3

cx1 = -b
cy1 = c
cx2 = b
cy2 = -c


centros = [(cx1, cy1), (cx2, cy2)]

for cx, cy in centros:
    circulo(r, cx, cy)

p = np.array([1.0, 5.0])
v = np.array([0.3, -0.3])
trayectoria = [p.copy()]

dt = 0.01
t_final = 80
t = 0.0

# Simulación

while t < t_final:
    x, y = p[0], p[1]

    # Diferencias
    dx1 = x - cx1
    dy1 = y - cy1
    dx2 = x - cx2
    dy2 = y - cy2

    # Distancias
    r1 = np.sqrt(dx1**2 + dy1**2)
    r2 = np.sqrt(dx2**2 + dy2**2)

    # Ángulos
    zeta1 = np.arctan2(dy1, dx1)
    zeta2 = np.arctan2(dy2, dx2)

    # Aceleraciones
    ax = -np.cos(zeta1) / r1**2 - np.cos(zeta2) / r2**2
    ay = -np.sin(zeta1) / r1**2 - np.sin(zeta2) / r2**2

    a = np.array([ax, ay])

    # Integración
    v += a * dt
    p += v * dt
    trayectoria.append(p.copy())
    t += dt


# Dibujar trayectoria del punto
trayectoria = np.array(trayectoria)
plt.plot(trayectoria[:, 0], trayectoria[:, 1], "r-")
plt.plot(1, 5, "go")

plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()
