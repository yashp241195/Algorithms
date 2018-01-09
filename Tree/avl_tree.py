# AVL tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class Tree:
    def __init__(self):
        self.root = None

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
            print("Node : ",root.data," at level :", level," height ", root.height)
            self.print_level(root.left, level + 1)
            self.print_level(root.right, level + 1)

    def compute_height(self, root, level):
        if root is None:
            return 0
        else:
            level = max(level, self.compute_height(root.left, level + 1), self.compute_height(root.right, level + 1))
            return level

    def rotate_left(self, root):
        if root.right is not None:
            old_root = root  # y -> current root
            new_root = root.right  # x -> root after rotate

            old_root.right = new_root.left  # changing beta
            new_root.left = old_root

            # Updating Heights
            old_root.height = 1 + max(self.get_height(old_root.left),
                                      self.get_height(old_root.right))

            new_root.height = 1 + max(self.get_height(new_root.left),
                                      self.get_height(new_root.right))

            root = new_root  # x is the new current root

        return root

    def rotate_right(self, root):
        if root.left is not None:
            old_root = root  # x -> current root
            new_root = root.left  # y -> root after rotate

            old_root.left = new_root.right  # changing beta
            new_root.right = old_root

            # Updating Heights
            old_root.height = 1 + max(self.get_height(old_root.left),
                                  self.get_height(old_root.right))

            new_root.height = 1 + max(self.get_height(new_root.left),
                                  self.get_height(new_root.right))

            root = new_root  # y is the new current root

        return root
    
    def get_height(self, root):
        if root is not None:
            return root.height
        else:
            return 0

    def get_balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def insert(self, root, key):
        if root is None:
            root = Node(key)
        else:
            if key < root.data:
                root.left = self.insert(root.left, key)
            elif key > root.data:
                root.right = self.insert(root.right, key)
            else:
                pass

            root.height = 1 + max(self.get_height(root.left),
                                  self.get_height(root.right))

            balance = self.get_balance(root)

            # right tree grown more
            if balance < -1:
                # Right Right Case
                if key > root.right.data:
                    return self.rotate_left(root)
                # Right Left Case
                else:
                    root.right = self.rotate_right(root.right)
                    return self.rotate_left(root)
            # left tree grown more
            elif balance > 1:
                # Left Left case
                if key < root.left.data:
                    return self.rotate_right(root)
                # Left Right case
                else:
                    root.left = self.rotate_left(root.left)
                    return self.rotate_right(root)

            else:
                # already balanced
                pass

        return root


t = Tree()
t.root = Node(1)
t.root = t.insert(t.root, 2)
t.root = t.insert(t.root, 3)
t.root = t.insert(t.root, 4)
t.root = t.insert(t.root, 5)
t.root = t.insert(t.root, 6)
t.root = t.insert(t.root, 7)


print("\nIn Order (Increasing Order): ")
t.print_tree(t.root, 1)
print("\n\nPre Order with level : \n")
t.print_level(t.root, 0)
print("\nMaximum Height : ", t.compute_height(t.root, 0))
