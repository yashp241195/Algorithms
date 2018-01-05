# Binary Search Tree

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

    def rotate_left(self, root):
        if root.right is not None:
            old_root = root  # y -> current root
            new_root = root.left  # x -> root after rotate

            old_root.left = new_root.right  # y.left (earlier -> x) = x.right (should be assigned as beta)
            new_root.right = old_root  # x.right = y

            root = new_root  # x is the new current root

        return root

    def rotate_right(self, root):
        if root.left is not None:
            old_root = root  # x -> current root
            new_root = root.right  # y -> root after rotate

            old_root.right = new_root.left  # x.right (earlier -> y) = y.left (should be assigned as beta)
            new_root.left = old_root  # y.left = x

            root = new_root  # x is the new current root

        return root

    def find_minimum(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            print(key, " does not exist in tree ")
            return root
        elif key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            # value is found
            # print(key, " exist in tree")
            # No child
            if root.left is None and root.right is None:
                del root
                root = None
            # Single child case
            elif root.left is None:
                temp = root
                root = root.right
                del temp

            elif root.right is None:
                temp = root
                root = root.left
                del temp
            #  Two children case
            else:
                # Find in order successor (minimum)
                next_min = self.find_minimum(root.right)
                root.data = next_min.data
                root.right = self.delete(root.right, next_min.data)

        return root


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
t.print_level(t.root, 0)
print("\nMaximum Height : ", t.get_height(t.root, 0))

print("\nAfter Left Rotation : ")
t.root = t.rotate_left(t.root)
t.print_level(t.root, 0)
print("\nIn Order (Increasing Order): ")
t.print_tree(t.root, 1)
print("\nAfter Right Rotation : ")
t.root = t.rotate_right(t.root)
t.print_level(t.root, 0)
print("\nIn Order (Increasing Order): ")
t.print_tree(t.root, 1)
print("\nNote : In-order traversal will remain same ")

t.root = t.delete(t.root, 0)
t.root = t.delete(t.root, 8)
t.print_level(t.root, 0)
