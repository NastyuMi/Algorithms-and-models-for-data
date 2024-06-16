import networkx as nx
import matplotlib.pyplot as plt

# Вкажіть правильний шлях до вашого файлу
file_path = 'N:/универ/Алгоритми та моделі збору, аналізу та візуалізації даних/lab6/karate_1.gml'

# Завантаження вашого графу
G = nx.read_gml(file_path, label='id')

# Отримання степеня кожного вузла
degrees = dict(G.degree())

# Встановлення параметрів для ранжування
node_sizes = [degrees[node] * 100 for node in G.nodes()]
node_colors = [degrees[node] for node in G.nodes()]

# Візуалізація графу
pos = nx.spring_layout(G)  # Використовуйте алгоритм розташування
plt.figure(figsize=(12, 12))

# Створення осей для графіку
ax = plt.gca()

# Відображення графу з налаштуванням розмірів та кольорів вузлів
nodes = nx.draw(
    G, pos, with_labels=True,
    node_size=node_sizes,
    node_color=node_colors,
    cmap=plt.cm.viridis,
    font_size=10,
    font_weight="bold",
    edge_color="gray",
    ax=ax
)

# Додавання кольорової шкали
sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=plt.Normalize(vmin=min(node_colors), vmax=max(node_colors)))
sm.set_array([])
plt.colorbar(sm, ax=ax)

plt.title('Graph Visualization with NetworkX - Nodes Ranked by Degree')
plt.savefig('NetworkX_karate.png', dpi=600)
plt.show()
