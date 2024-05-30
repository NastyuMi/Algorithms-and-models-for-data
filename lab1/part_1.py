# За списком 12я завдання №12
import numpy as np
import matplotlib.pyplot as plt

# Визначення функцій y(x) і z(x)
def y(x):
    return (1 + np.cos(x)) / (1 + np.exp(4 * x)) * np.power(1 + np.exp(6 * x), 1 / 4)
#    if x < 0:
#        return (1 + np.cos(x)) / (1 + np.exp(4*x)) * np.power(1 + np.exp(6*x), 1/4)
#    elif 0 <= x <= 1:
#        return 2 * np.power(np.sin(x), 3)
#    else:
#        return np.sqrt(1 + np.power(2 * np.abs(np.cos(6*x)), 1/3))

def z(x):
    if x < 0:
        return np.sqrt(1 + x**2 / (1 + x**4))
    elif 0 <= x <= 1:
        return 2 * np.power(np.sin(x), 3)
    else:
        return np.sqrt(1 + np.abs(2 * np.cos(6*x))**(1/3))

# Побудова графіків
x = np.linspace(-2, 2, 400)
y_values = np.array([y(xi) for xi in x])
z_values = np.array([z(xi) for xi in x])

plt.figure(figsize=(10, 5))

plt.plot(x, y_values, label='$y(x)$')
plt.plot(x, z_values, label='$z(x)$')

# Позначення областей, де функції приймають різні визначення
plt.fill_between(x, z_values, where=(x < 0), color='gray', alpha=0.3, label='$x < 0$')
plt.fill_between(x, z_values, where=((x >= 0) & (x <= 1)), color='blue', alpha=0.3, label='$0 \leq x \leq 1$')
plt.fill_between(x, z_values, where=(x > 1), color='green', alpha=0.3, label='$x > 1$')

# Анотації зі значеннями функції на кожній області
plt.annotate(r'$y = \frac{1 + \cos(x)}{1 + e^{4x}} \sqrt[4]{1 + e^{6x}}$', xy=(x[100], y_values[100]), xytext=(-20, 20), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'), fontsize=8)
plt.annotate(r'$z = \sqrt{1 + {x^{2} \ 1 + x^{4}}}$ при $x < 0$', xy=(x[100], z_values[100]), xytext=(-20, 20), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'), fontsize=8)
plt.annotate(r'$z = 2 \sin^3(x)$ при $0 \leq x \leq 1$', xy=(x[265], y_values[250]), xytext=(-20, -20), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'), fontsize=8)
plt.annotate(r'$z = \sqrt{1 + |2 \cos(6x)|^{1/3}}$ при $x > 1$', xy=(x[350], z_values[350]), xytext=(-20, 20), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'), fontsize=8)

plt.xlabel('$x$')
plt.ylabel('$y(x), z(x)$')

plt.grid(True)
plt.legend()

plt.title('Графіки функцій $y(x)$ і $z(x)$')

plt.show()
