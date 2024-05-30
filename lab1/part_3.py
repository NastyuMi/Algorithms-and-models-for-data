import numpy as np
import matplotlib.pyplot as plt

# Параметри спіралі Галілея
theta = np.linspace(0, 10*np.pi, 1000)
r = theta**2

# Побудова графіку у полярних координатах
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r, color='b')
ax.set_title('Спіраль Галілея', va='bottom')
plt.show()
