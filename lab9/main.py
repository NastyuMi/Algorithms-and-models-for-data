import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Завантажуємо набір даних iris
iris = pd.read_csv('db/iris.data', header=None)
X = iris.iloc[:, :-1].values

# Перетворюємо рядкові мітки класів на числові значення
labels = list(set(iris.iloc[:, -1]))
y = [labels.index(label) for label in iris.iloc[:, -1]]

# 1. Візуалізація даних за допомогою PCA
pca_2d = PCA(n_components=2)
X_pca_2d = pca_2d.fit_transform(X)

pca_3d = PCA(n_components=3)
X_pca_3d = pca_3d.fit_transform(X)

# Візуалізація у 2D
plt.figure(figsize=(8, 6))
plt.scatter(X_pca_2d[:, 0], X_pca_2d[:, 1], c=y)
plt.title("PCA 2D")
plt.savefig('pca_2d.png')  # Збереження графіку
plt.show()

# Візуалізація у 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_pca_3d[:, 0], X_pca_3d[:, 1], X_pca_3d[:, 2], c=y)
ax.set_title("PCA 3D")
plt.savefig('pca_3d.png')  # Збереження графіку
plt.show()

# 2. Обчислення SVD та візуалізація власних значень
U, Sigma, VT = np.linalg.svd(X, full_matrices=False)
eigenvalues = Sigma ** 2

# Сортуємо власні значення за спаданням
sorted_eigenvalues = np.sort(eigenvalues)[::-1]

plt.figure(figsize=(8, 6))
plt.plot(range(len(sorted_eigenvalues)), sorted_eigenvalues)
plt.title("Власні значення матриці")
plt.xlabel("Номер власного значення")
plt.ylabel("Значення")
plt.savefig('eigenvalues.png')  # Збереження графіку
plt.show()

# 3. Визначення мінімального розміру простору
total_variance = np.sum(sorted_eigenvalues)
cumulative_variance = np.cumsum(sorted_eigenvalues)
d = np.argmax(cumulative_variance / total_variance >= 0.8) + 1
print(f"Мінімальний розмір простору: {d}")

# 4. Зменшення розмірності за допомогою SVD
Sigma_reduced = np.diag(Sigma[:d])
X_reduced = U[:, :d] @ Sigma_reduced @ VT[:d, :]

# Порівняння з вихідними даними
print("Середня квадратична похибка:", np.sqrt(np.mean((X - X_reduced) ** 2)))

# 5. Візуалізація відновлених даних у 2D та 3D
X_reduced_2d = X_reduced[:, :2]
X_reduced_3d = X_reduced[:, :3]

plt.figure(figsize=(8, 6))
plt.scatter(X_reduced_2d[:, 0], X_reduced_2d[:, 1], c=y)
plt.title("Відновлені дані у 2D")
plt.savefig('reduced_2d.png')  # Збереження графіку
plt.show()

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_reduced_3d[:, 0], X_reduced_3d[:, 1], X_reduced_3d[:, 2], c=y)
ax.set_title("Відновлені дані у 3D")
plt.savefig('reduced_3d.png')  # Збереження графіку
plt.show()
