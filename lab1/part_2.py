from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

# Функція, яка обчислює значення згідно з умовами
def z_func(x, y):
    if x**2 + y**2 <= 1:
        return x**5 - 3*y**3
    else:
        return 3*x**2 - y**3

# Створення даних для графіку
X = np.arange(-1.5, 1.5, 0.1)
Y = np.arange(-1.5, 1.5, 0.1)
X, Y = np.meshgrid(X, Y)
Z = np.array([[z_func(x, y) for x, y in zip(x_row, y_row)] for x_row, y_row in zip(X, Y)])

# Побудова графіку поверхні
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Налаштування осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Додавання колірної смуги
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
