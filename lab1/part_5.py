#За списком 12та , за завданням №2
import numpy as np
import matplotlib.pyplot as plt

# Дані для 2D стовпчикової діаграми
countries = ['Germany', 'France', 'UK', 'Italy']
years = ['1900', '1913', '1929', '1938', '1950', '1960', '1970', '1980', '1990', '2000']
data = np.array([
    [18.5, 20, 16.5, 15],
    [23.5, 20, 18.5, 16.5],
    [25, 20, 20, 17],
    [26.5, 19.5, 20.5, 18],
    [29, 19, 22.5, 18.5],
    [31, 21, 24, 20],
    [34, 23, 25, 22],
    [35, 25, 25.5, 24],
    [37, 26.5, 26, 24.5],
    [38.5, 27.5, 26.5, 25]
])

bar_width = 0.2
fig, ax = plt.subplots(figsize=(10, 6))

for i, country in enumerate(countries):
    x_pos = np.arange(len(years)) + i * bar_width
    ax.bar(x_pos, data[:, i], bar_width, label=country)

ax.set_xlabel('Year')
ax.set_ylabel('Number of people (million)')
ax.set_title('Number of people in World Economy')
ax.set_xticks(np.arange(len(years)) + bar_width * (len(countries) - 1) / 2)
ax.set_xticklabels(years)
ax.legend()

plt.tight_layout()
plt.show()

# Дані для 3D стовпчикової діаграми
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xpos = np.arange(len(years))
ypos = np.arange(len(countries))
xpos, ypos = np.meshgrid(xpos, ypos, indexing='ij')
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = np.zeros_like(xpos)

dx = dy = 0.8
dz = data.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, shade=True)

ax.set_xlabel('Year')
ax.set_ylabel('Country')
ax.set_zlabel('Number of people (million)')
ax.set_title('Number of people in World Economy')

ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years)
ax.set_yticks(np.arange(len(countries)))
ax.set_yticklabels(countries)

plt.show()
