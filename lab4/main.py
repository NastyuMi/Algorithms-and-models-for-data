import random
import graphviz


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, key, node=None):
        if node is None:
            node = self.root
        if self.root is None:
            self.root = Node(key)
        else:
            if key <= node.key:
                if node.left is None:
                    node.left = Node(key)
                    node.left.parent = node
                else:
                    self.add_node(key, node=node.left)
            else:
                if node.right is None:
                    node.right = Node(key)
                    node.right.parent = node
                else:
                    self.add_node(key, node=node.right)

    def search(self, key, node=None):
        if node is None:
            node = self.root
        if node is None:
            return None
        if node.key == key:
            return node
        elif key < node.key and node.left is not None:
            return self.search(key, node=node.left)
        elif key > node.key and node.right is not None:
            return self.search(key, node=node.right)
        else:
            return None

    def delete_node(self, key):
        node_to_delete = self.search(key)
        if node_to_delete is None:
            return

        # Node to be deleted is a leaf node
        if node_to_delete.left is None and node_to_delete.right is None:
            self._replace_node_in_parent(node_to_delete, None)
        # Node to be deleted has one child
        elif node_to_delete.left is None:
            self._replace_node_in_parent(node_to_delete, node_to_delete.right)
        elif node_to_delete.right is None:
            self._replace_node_in_parent(node_to_delete, node_to_delete.left)
        # Node to be deleted has two children
        else:
            successor = self.find_minimum(node_to_delete.right)
            node_to_delete.key = successor.key
            self.delete_node(successor.key)

    def _replace_node_in_parent(self, node, new_node):
        if node.parent is not None:
            if node == node.parent.left:
                node.parent.left = new_node
            else:
                node.parent.right = new_node
        if new_node is not None:
            new_node.parent = node.parent
        if node == self.root:
            self.root = new_node

    def find_minimum(self, node=None):
        if node is None:
            node = self.root
        while node.left is not None:
            node = node.left
        return node

    def visualize(self, filename="tree"):
        dot = graphviz.Digraph(comment="Binary Tree")

        def add_edges(node):
            if node.left:
                dot.edge(str(node.key), str(node.left.key))
                add_edges(node.left)
            if node.right:
                dot.edge(str(node.key), str(node.right.key))
                add_edges(node.right)

        if self.root:
            dot.node(str(self.root.key))
            add_edges(self.root)

        dot.render(filename, view=True)


# Створення дерева зі значеннями від 100 до 200
t = Tree()
values = random.sample(range(100, 201), 15)  # Створюємо список із 15 унікальних значень у діапазоні [100, 200]

for value in values:
    t.add_node(value)

# Візуалізація дерева
t.visualize("binary_tree")
