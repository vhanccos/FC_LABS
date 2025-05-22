import matplotlib.pyplot as plt
import numpy as np
import math

r1 = 1
r2 = 1
b = 1.8
c = 3

center1 = (-b, c)
center2 = (b, -c)

n_points = 400
theta = np.linspace(0, 2 * np.pi, n_points)
x1 = center1[0] + r1 * np.cos(theta)
y1 = center1[1] + r1 * np.sin(theta)
x2 = center2[0] + r2 * np.cos(theta)
y2 = center2[1] + r2 * np.sin(theta)


def ax(x, y):
    x1_ = x - center1[0]
    y1_ = y - center1[1]
    r1_ = math.sqrt(x1_**2 + y1_**2)
    x2_ = x - center2[0]
    y2_ = y - center2[1]
    r2_ = math.sqrt(x2_**2 + y2_**2)
    cos_theta1 = x1_ / r1_
    cos_theta2 = x2_ / r2_
    return -1 / r1_**2 * cos_theta1 - 1 / r2_**2 * cos_theta2


def ay(x, y):
    x1_ = x - center1[0]
    y1_ = y - center1[1]
    r1_ = math.sqrt(x1_**2 + y1_**2)
    x2_ = x - center2[0]
    y2_ = y - center2[1]
    r2_ = math.sqrt(x2_**2 + y2_**2)
    sin_theta1 = y1_ / r1_
    sin_theta2 = y2_ / r2_
    return -1 / r1_**2 * sin_theta1 - 1 / r2_**2 * sin_theta2


def esta_dentro_circulo(x, y, center, radius):
    return (x - center[0]) ** 2 + (y - center[1]) ** 2 < radius**2


def simulate_trajectory(x, y, vx, vy, dt, t_max):
    posX = []
    posY = []
    for t in np.arange(0, t_max, dt):
        posX.append(x)
        posY.append(y)

        ax_val = ax(x, y)
        ay_val = ay(x, y)

        vx += ax_val * dt
        vy += ay_val * dt

        x += vx * dt
        y += vy * dt

        if esta_dentro_circulo(x, y, center1, r1) or esta_dentro_circulo(
            x, y, center2, r2
        ):
            break

    return [posX, posY]


dt = 0.01
t_max = 200
x = 1
y = 5
vx = 0.3
vy = -0.3

nave1 = simulate_trajectory(x, y, vx, vy, dt, t_max)
nave2 = simulate_trajectory(x + 0.01, y, vx, vy, dt, t_max)

print("Momento de graficar")

fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.plot(x1, y1, color="black", label="C1")
ax.plot(x2, y2, color="black", label="C2")

print("Graficando los puntos")
print(len(nave1[0]))
print(len(nave1[1]))

ax.plot(nave1[0], nave1[1], color="blue", label="Nave 1")
ax.plot(nave2[0], nave2[1], color="red", label="Nave 2")

ax.legend()
plt.grid(True)
plt.title("Simulación de dos naves")
plt.show()
