import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def circulo(ax, r, cx, cy):
    t = np.linspace(0, 2 * np.pi, 100)
    x = r * np.cos(t) + cx
    y = r * np.sin(t) + cy
    ax.plot(x, y, "b")


def simular_trayectoria(p0, v0, cx1, cy1, cx2, cy2, r, dt=0.05, t_final=80):
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

condiciones = [
    ([1.0, 5.0], [0.3, -0.3]),
    ([2.0, 4.0], [0.2, -0.1]),
    ([2.0, 2.0], [-0.2, -0.2]),
    ([3.0, 2.0], [0.5, 0.5]),
]
colores = ["r", "g", "m", "c"]

trayectorias = [
    simular_trayectoria(p0, v0, cx1, cy1, cx2, cy2, r) for (p0, v0) in condiciones
]

fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.grid(True)
ax.set_title("Simulación de 4 trayectorias (animación)")

for cx, cy in centros:
    circulo(ax, r, cx, cy)

lines = [
    ax.plot([], [], color=colores[i], label=f"Trayectoria {i + 1}")[0] for i in range(4)
]
points = [ax.plot([], [], "o", color=colores[i])[0] for i in range(4)]

all_x = np.concatenate([traj[:, 0] for traj in trayectorias])
all_y = np.concatenate([traj[:, 1] for traj in trayectorias])
ax.set_xlim(np.min(all_x) - 1, np.max(all_x) + 1)
ax.set_ylim(np.min(all_y) - 1, np.max(all_y) + 1)
ax.legend()

max_len = max(len(traj) for traj in trayectorias)


def update(frame):
    for i, traj in enumerate(trayectorias):
        if frame < len(traj):
            lines[i].set_data(traj[: frame + 1, 0], traj[: frame + 1, 1])
            points[i].set_data([traj[frame, 0]], [traj[frame, 1]])
    return lines + points


ani = animation.FuncAnimation(fig, update, frames=max_len, interval=1, blit=True)
plt.show()
