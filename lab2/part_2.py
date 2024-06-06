import numpy as np
import matplotlib.pyplot as plt

def u(x, y):
    return x + 2 * y**2

def v(x, y):
    return y + 2 * x**2

xx, yy = np.meshgrid(np.linspace(-3, 6, 10),
                     np.linspace(-3, 6, 10))
u_val = u(xx, yy)
v_val = v(xx, yy)

# Візуалізація векторного поля за допомогою векторів
plt.figure(figsize=(8, 6))
plt.quiver(xx, yy, u_val, v_val)
plt.title('Vector Field: F(x, y) = (x + 2y^2, y + 2x^2)')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Візуалізація векторного поля за допомогою ліній струму
plt.figure(figsize=(8, 6))
plt.streamplot(xx, yy, u_val, v_val)
plt.title('Stream Lines: F(x, y) = (x + 2y^2, y + 2x^2)')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()