# Simple BST


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            root = Node(key)
        else:
            if key < root.data:
                root.left = self.insert(root.left, key)
            elif key > root.data:
                root.right = self.insert(root.right, key)
        return root

    def print_tree(self, root, traverse_order=0):
        if root is not None:
            if traverse_order == 0:
                print(root.data, end=" ")
                self.print_tree(root.left, traverse_order)
                self.print_tree(root.right, traverse_order)
            elif traverse_order == 1:
                self.print_tree(root.left, traverse_order)
                print(root.data, end=" ")
                self.print_tree(root.right, traverse_order)
            elif traverse_order == 2:
                self.print_tree(root.left, traverse_order)
                self.print_tree(root.right, traverse_order)
                print(root.data, end=" ")
            else:
                pass

    def print_level(self, root, level):
        if root is not None:
            print("Node : ",root.data," at level :", level)
            self.print_level(root.left, level + 1)
            self.print_level(root.right, level + 1)

    def get_height(self, root, level):
        if root is None:
            return 0
        else:
            level = max(level, self.get_height(root.left, level + 1), self.get_height(root.right, level + 1))
            return level


t = Tree()
t.root = Node(5)
t.root = t.insert(t.root, 3)
t.root = t.insert(t.root, 2)
t.root = t.insert(t.root, 4)
t.root = t.insert(t.root, 7)
t.root = t.insert(t.root, 6)
t.root = t.insert(t.root, 8)

print("\nPre Order : ")
t.print_tree(t.root, 0)
print("\nIn Order (Increasing Order): ")
t.print_tree(t.root, 1)
print("\nPost Order : ")
t.print_tree(t.root, 2)
print("\n\nPre Order with level : \n")
arr = []
t.print_level(t.root, 0)
print("\nMaximum Height : ", t.get_height(t.root, 0))
