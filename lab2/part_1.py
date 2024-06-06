import numpy as np
from matplotlib import pyplot as plt

n = 256

x = np.linspace(-3, 6, n)
y = np.linspace(-3, 6, n)
X, Y = np.meshgrid(x, y)

Z = -2 * np.log(X**2 + 5) - 4 * X * Y

# Візуалізація скалярного поля за допомогою псевдокольорової растрової карти
plt.figure(figsize=(8, 6))
plt.pcolormesh(X, Y, Z, cmap='coolwarm')
plt.colorbar()
plt.title('Scalar Field: u(x, y) = -2 * log(x^2 + 5) - 4 * x * y')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()