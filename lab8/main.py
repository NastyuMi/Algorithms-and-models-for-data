import pandas as pd
from sklearn import manifold
import matplotlib.pyplot as plt

# Завантажуємо набір даних iris
iris = pd.read_csv('db/iris.data', header=None)
X = iris.iloc[:, :-1].values
y = iris.iloc[:, -1].values

# Перетворюємо рядкові мітки класів на числові значення
labels = list(set(y))
y_num = [labels.index(label) for label in y]

# Розмірність вихідних даних
print("Розмірність вихідних даних: ", X.shape)

# Isomap
iso = manifold.Isomap(n_components=2)
X_iso = iso.fit_transform(X)
print("Розмірність даних після Isomap: ", X_iso.shape)

# LLE
lle = manifold.LocallyLinearEmbedding(n_components=2)
X_lle = lle.fit_transform(X)
print("Розмірність даних після LLE: ", X_lle.shape)

# MDS
mds = manifold.MDS(n_components=2)
X_mds = mds.fit_transform(X)
print("Розмірність даних після MDS: ", X_mds.shape)

# t-SNE
tsne = manifold.TSNE(n_components=2)
X_tsne = tsne.fit_transform(X)
print("Розмірність даних після t-SNE: ", X_tsne.shape)

# Візуалізація результатів
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.scatter(X_iso[:, 0], X_iso[:, 1], c=y_num)
plt.title("Isomap")

plt.subplot(2, 2, 2)
plt.scatter(X_lle[:, 0], X_lle[:, 1], c=y_num)
plt.title("LLE")

plt.subplot(2, 2, 3)
plt.scatter(X_mds[:, 0], X_mds[:, 1], c=y_num)
plt.title("MDS")

plt.subplot(2, 2, 4)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y_num)
plt.title("t-SNE")

plt.savefig('reduction_Iris.png', dpi=1080)
plt.show()