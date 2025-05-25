import numpy as np
import matplotlib.pyplot as plt

h = 0.01
k = 0.02
tfin = 300
r_limite = 3


def ax(x, y):
    r2 = x**2 + y**2
    if r2 == 0:
        return 0
    return -x / (r2 ** (3 / 2))


def ay(x, y):
    r2 = x**2 + y**2
    if r2 == 0:
        return 0
    return -y / (r2 ** (3 / 2))


theta = np.linspace(0, 2 * np.pi, 100)
circle_x = r_limite * np.cos(theta)
circle_y = r_limite * np.sin(theta)

plt.figure()
plt.plot(circle_x, circle_y)
plt.axis("equal")
plt.grid(True)

vxe = 0.45
vxh = 0.55

vx_values = [0.28, 0.30]  # 2 parábolas
vxe_values = [vxe + k, vxe + 2 * k]  # 2 elipses
vxh_values = [vxh + k, vxh + 2 * k]  # 2 hiperbolas

for i in range(2):
    x, y, vy = 0.0, 4.0, 0.2
    xe, ye, vye = 0.0, 4.0, 0.2
    xh, yh, vyh = 0.0, 4.0, 0.2

    vx = vx_values[i]
    vxe_i = vxe_values[i]
    vxh_i = vxh_values[i]

    px, py = [x], [y]
    pxe, pye = [xe], [ye]
    pxh, pyh = [xh], [yh]

    t = 0
    while t <= tfin:
        r = np.sqrt(x**2 + y**2)
        x += vx * h
        y += vy * h
        vx += ax(x, y) * h
        vy += ay(x, y) * h
        if r > r_limite:
            px.append(x)
            py.append(y)

        re = np.sqrt(xe**2 + ye**2)
        xe += vxe_i * h
        ye += vye * h
        vxe_i += ax(xe, ye) * h
        vye += ay(xe, ye) * h
        if re > r_limite:
            pxe.append(xe)
            pye.append(ye)

        rh = np.sqrt(xh**2 + yh**2)
        xh += vxh_i * h
        yh += vyh * h
        vxh_i += ax(xh, yh) * h
        vyh += ay(xh, yh) * h
        if rh > r_limite:
            pxh.append(xh)
            pyh.append(yh)

        t += h

    plt.plot(px, py, "ro", markersize=0.5)  # parábola
    plt.plot(pxe, pye, "bo", markersize=0.5)  # elipse
    plt.plot(pxh, pyh, "go", markersize=0.5)  # hiperbola

plt.show()
