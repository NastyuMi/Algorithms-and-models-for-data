import matplotlib.pyplot as plt
import networkx as nx
from instagrapi import Client
from instagrapi.exceptions import TwoFactorRequired

MAX_FOLLOWINGS_COUNT = 20  # Максимальна кількість фоловерів

# Вхід до Instagram
instagram_client = Client()

# Налаштування затримки за рекомендаціями
instagram_client.delay_range = [1, 5]

# Введіть ваші дані для входу
USERNAME = input("Введіть ім'я користувача: ")
PASSWORD = input("Введіть пароль: ")

# Перевірка на порожні логін та пароль
assert USERNAME, 'Логін повинен бути введений'
assert PASSWORD, 'Пароль повинен бути введений'

# Вхід до системи з перевіркою двофакторної автентифікації
try:
    instagram_client.login(USERNAME, PASSWORD)
    print("Успішний вхід")
except TwoFactorRequired:
    print("Потрібна двофакторна автентифікація. Будь ласка, вимкніть її в налаштуваннях Instagram.")
    raise

# Завантаження фоловерів
my_followings = instagram_client.user_following(user_id=instagram_client.user_id, amount=MAX_FOLLOWINGS_COUNT)
my_followings_names = [user.username for user in my_followings.values()]

G = nx.Graph()
G.add_node(instagram_client.username, label=instagram_client.username)

# Додавання вузлів та ребер для фоловерів
for following in my_followings.values():
    G.add_node(following.username, label=following.full_name)
    G.add_edge(instagram_client.username, following.username)

# Завантаження фоловерів фоловерів
for person in my_followings.values():
    try:
        following_followings = instagram_client.user_following(person.pk)
        for following in following_followings.values():
            if following.username in my_followings_names:
                G.add_node(following.username, label=following.full_name)
                G.add_edge(person.username, following.username)
    except Exception as e:
        print(f"Помилка при завантаженні даних для {person.username}: {e}")

# Збереження графу у форматі gexf
nx.write_gexf(G, "InstaFriends.gexf")

# Візуалізація графу
nx.draw_spring(G, with_labels=True, font_weight='bold', font_size=5)
plt.savefig('InstaGraf.png', dpi=600)
plt.show()

# Обчислення середнього ступеня вершин
avg_degree = sum(dict(G.degree()).values()) / nx.number_of_nodes(G)
print(f"Середній ступінь вершин: {avg_degree}")
