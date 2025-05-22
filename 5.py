import numpy as np
import matplotlib.pyplot as plt


def circulo(r, cx, cy):
    t = np.linspace(0, 2 * np.pi, 100)
    x = r * np.cos(t) + cx
    y = r * np.sin(t) + cy
    plt.plot(x, y, "b")


def simular_trayectoria(p0, v0, cx1, cy1, cx2, cy2, r, dt=0.01, t_final=80):
    p = np.array(p0, dtype=float)
    v = np.array(v0, dtype=float)
    trayectoria = [p.copy()]
    t = 0.0

    while t < t_final:
        x, y = p[0], p[1]
        dx1, dy1 = x - cx1, y - cy1
        dx2, dy2 = x - cx2, y - cy2
        r1 = np.sqrt(dx1**2 + dy1**2)
        r2 = np.sqrt(dx2**2 + dy2**2)

        if r1 <= r or r2 <= r:
            break

        zeta1 = np.arctan2(dy1, dx1)
        zeta2 = np.arctan2(dy2, dx2)

        ax = -np.cos(zeta1) / r1**2 - np.cos(zeta2) / r2**2
        ay = -np.sin(zeta1) / r1**2 - np.sin(zeta2) / r2**2
        a = np.array([ax, ay])

        v += a * dt
        p += v * dt
        trayectoria.append(p.copy())
        t += dt

    return np.array(trayectoria)


r = 1
b = 1.8
c = 3
cx1, cy1 = -b, c
cx2, cy2 = b, -c
centros = [(cx1, cy1), (cx2, cy2)]

for cx, cy in centros:
    circulo(r, cx, cy)

condiciones = [
    ([1.0, 5.0], [0.3, -0.3]),
    ([2.0, 4.0], [0.2, -0.1]),
    ([2.0, 2.0], [-0.2, -0.2]),
    ([3.0, 2.0], [0.5, 0.5]),
]

colores = ["r-", "g-", "m-", "c-"]
for i, (p0, v0) in enumerate(condiciones):
    trayectoria = simular_trayectoria(p0, v0, cx1, cy1, cx2, cy2, r)
    plt.plot(
        trayectoria[:, 0], trayectoria[:, 1], colores[i], label=f"Trayectoria {i + 1}"
    )
    plt.plot(p0[0], p0[1], "o", label=f"Inicio {i + 1}", markersize=4)

plt.axis("equal")
plt.grid(True)
plt.legend()
plt.title("Simulación de 4 trayectorias")
plt.show()

