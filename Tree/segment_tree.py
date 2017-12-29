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
        mid = int((le + ri) / 2)

        if root is None:
            root = Node(key, le, ri)
        else:
            if le <= ri:
                root.left = self.insert(root.left, le, mid, key)
                root.right = self.insert(root.right, mid + 1, ri, key)
        return root

    def print_tree(self, root):
        if root is not None:
            print("Left ", root.leftIndex, " Right ", root.rightIndex)
            self.print_tree(root.left)

            self.print_tree(root.right)


t = Tree()
size = 9
t.root = Node(15, 0, size)
temp = size
depth = -2
visited = [1]*size
while temp >= 1:
    temp = int(temp/2)
    depth += 1

t.root = t.insert(t.root, 0, size, 15)


for i in range(depth):
    if t.root.left.leftIndex < t.root.left.rightIndex:
        t.root.left = t.insert(t.root.left, t.root.left.leftIndex, t.root.left.rightIndex, 15)
    if t.root.right.leftIndex < t.root.right.rightIndex:
        t.root.right = t.insert(t.root.right, t.root.right.leftIndex, t.root.right.rightIndex, 15)

t.print_tree(t.root)
