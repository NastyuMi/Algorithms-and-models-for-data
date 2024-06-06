import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.lines import Line2D

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(0, 10), ylim=(0, 10))

# Визначення координат вершин рівностороннього трикутника
triangle_vertices = [(5, 9), (1, 1), (9, 1)]

# Визначення координат проміжних точок по ребрах трикутника
edge_points = [(triangle_vertices[i], triangle_vertices[(i + 1) % 3]) for i in range(3)]

# Визначення початкових координат для полілінії у формі букви "V"
x_coords = [-0.09, 0.0, 0.09]
y_coords = [0.1, -0.1, 0.1]

# Створення ліній для "V"
line1 = Line2D([], [], color='black')
line2 = Line2D([], [], color='black')


def init():
    ax.add_line(line1)
    ax.add_line(line2)
    return line1, line2


def animate(i):
    # Обчислення відстані пройденого кута
    angle = np.radians(i)

    # Знаходимо ребро, по якому рухається фігура
    edge_index = i // 120 % 3
    edge_start, edge_end = edge_points[edge_index]

    # Обчислення нових координат для фігури вздовж ребра
    x_start, y_start = edge_start
    x_end, y_end = edge_end
    x = x_start + (x_end - x_start) * (i % 120) / 120
    y = y_start + (y_end - y_start) * (i % 120) / 120

    # Оновлення координат ліній для букви "V"
    new_x_coords = [x + 2 * x_ for x_ in x_coords]
    new_y_coords = [y + 2 * y_ for y_ in y_coords]

    line1.set_data([new_x_coords[0], new_x_coords[1]], [new_y_coords[0], new_y_coords[1]])
    line2.set_data([new_x_coords[1], new_x_coords[2]], [new_y_coords[1], new_y_coords[2]])

    return line1, line2


anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=360,
                               interval=5,
                               blit=True)


anim.save('animation.gif', writer='imagemagick', fps=30)

plt.show()
