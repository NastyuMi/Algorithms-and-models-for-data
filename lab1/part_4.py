#За списком 12та , за завданням №3
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# Константи a, b, c
a = 1
b = 2
c = 3

# Параметри гіперболоїда
u = np.linspace(-3, 3, 100)
v = np.linspace(0, 2*np.pi, 100)
U, V = np.meshgrid(u, v)

# Координати X, Y, Z гіперболоїда
X = a * np.cosh(U) * np.cos(V)
Y = b * np.cosh(U) * np.sin(V)
Z = c * np.sinh(U)

# Побудова графіку поверхні
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Налаштування відображення
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Двохполосний гіперболоїд')

plt.show()
