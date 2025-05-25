import numpy as np
import matplotlib.pyplot as plt

r = 3
theta = np.linspace(0, 2 * np.pi, 100)
x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x, y)
plt.grid(True)
plt.axis("equal")
plt.show()
