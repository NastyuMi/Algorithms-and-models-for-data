import networkx as nx
import matplotlib.pyplot as plt
import os
import sys
import datetime
from matplotlib import cm
from matplotlib.colors import Normalize


def get_tree(tree, G=nx.Graph(), itr=0, max_itr=900):
    while tree and itr <= max_itr:
        point = tree.pop(0)
        itr += 1
        try:
            sub_tree = [
                os.path.join(point, x) for x in os.listdir(point)
                if os.path.isdir(os.path.join(point, x)) and not is_hidden_dir(os.path.join(point, x))
            ]
            if sub_tree:
                tree.extend(sub_tree)
                G.add_edges_from((point, b) for b in sub_tree)
        except FileNotFoundError:
            print(f"FileNotFoundError: {point}")
            continue
        except PermissionError:
            print(f"PermissionError: {point}")
            continue
    return G


def is_hidden_dir(d):
    if sys.platform.startswith("win"):
        return False
    else:
        return os.path.basename(d).startswith('.')


def get_creation_date(path):
    if sys.platform.startswith('win'):
        return datetime.datetime.fromtimestamp(os.path.getctime(path))
    else:
        stat = os.stat(path)
        try:
            return datetime.datetime.fromtimestamp(stat.st_birthtime)
        except AttributeError:
            return datetime.datetime.fromtimestamp(stat.st_mtime)


def main(root_dir: str):
    if not os.path.isdir(root_dir):
        print(f"Error: The directory '{root_dir}' does not exist.")
        return

    print(f"Processing directory: {root_dir}")

    G = get_tree(tree=[root_dir])
    node_colors = []
    creation_dates = []

    for node in G.nodes:
        creation_date = get_creation_date(node)
        creation_dates.append(creation_date)

    if not creation_dates:
        print("No nodes found in the directory.")
        return

    min_date = min(creation_dates)
    max_date = max(creation_dates)
    norm = Normalize(vmin=min_date.timestamp(), vmax=max_date.timestamp())
    colormap = cm.viridis

    for date in creation_dates:
        color = colormap(norm(date.timestamp()))
        node_colors.append(color)

    options = {
        'node_color': node_colors,
        'node_size': 100,
        'width': 0.5,
        'with_labels': True,
        'alpha': 0.6,
        'font_size': 3,
        'font_family': 'Arial'
    }

    plt.figure(figsize=(10, 10))
    plt.title('Directory Tree Visualization by Creation Date')
    pos = nx.spring_layout(G)
    nx.draw(G, pos, **options)

    sm = cm.ScalarMappable(cmap=colormap, norm=norm)
    sm.set_array([])

    cbar = plt.colorbar(sm, ax=plt.gca())
    cbar.set_label('Creation Date')

    plt.savefig('graphs.png', dpi=600)
    plt.show()
    print("Graph has been saved as 'graphs.png'.")


if __name__ == "__main__":
    root_dir = r"N:\универ\Алгоритми та моделі збору, аналізу та візуалізації даних\lab5"
    main(root_dir)
