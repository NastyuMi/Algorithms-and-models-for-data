from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-3, 6, 10)
y = np.linspace(-3, 6, 10)
z = np.linspace(-3, 6, 10)
X, Y, Z = np.meshgrid(x, y, z)

u = Y - (Z / (X**2))
v = X + 1 / (Z)
w = 1 / X - (Y / (Z**2))

ax.quiver(X, Y, Z, u, v, w, length=0.1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Vector Field: F(x, y, z) = (y - (z / x^2), x + 1/z, 1/x - (y / z^2))')

plt.show()