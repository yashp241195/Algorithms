# Segment tree


class Node:
    def __init__(self, data, le, ri):
        self.data = data

        self.leftIndex = le
        self.left = None

        self.rightIndex = ri
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, root, le, ri, key):
        if root is None:
            root = Node(key, le, ri)
        else:
            if le <= ri:
                mid = int((le + ri) / 2)
                root.left = self.insert(root.left, le, mid, key)
                root.right = self.insert(root.right, mid + 1, ri, key)
        return root

    def print_tree(self, root):
        if root is not None:
            print("Left ", root.leftIndex, " Right ", root.rightIndex)
            self.print_tree(root.left)
            self.print_tree(root.right)


t = Tree()
t.root = Node(15, 0, 9)
t.root = t.insert(t.root, 0, 9, 15)
t.print_tree(t.root)
