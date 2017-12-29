# Range Query (Using Segment Tree)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
size = len(arr)
sum = 0
arr_sum = [0]*size

for i in range(size):
    sum += arr[i]
    arr_sum[i] = sum

print("Array : ", arr)
print("Sum Array : ", arr_sum)

# To find the sum from index 1 to 4

left = 2
right = 4

answer = arr_sum[right]
if left > 0:
    answer -= arr_sum[left - 1]

print("The sum from index ", left," to ", right," is ",answer)

# update index

index = 5
updated_value = 9
print("Value at index ", index," is ", arr[index], ", Updated Value : ", updated_value)
delta = updated_value - arr[index]
print("Difference : ", delta)

for i in range(index, size):
    arr_sum[i] += delta

print("Updated Array : ", arr_sum)

# Segment tree


class Node:
    def __init__(self, le, ri):
        data = arr_sum[ri]
        if le > 0:
            data -= arr_sum[le - 1]
        self.data = data

        self.leftIndex = le
        self.left = None

        self.rightIndex = ri
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, root, le, ri):
        mid = int((le + ri) / 2)

        if root is None:
            root = Node(le, ri)
        else:
            if le <= ri:
                root.left = self.insert(root.left, le, mid)
                root.right = self.insert(root.right, mid + 1, ri)
        return root

    def print_tree(self, root):
        if root is not None:
            print("Left ", root.leftIndex, " Right ", root.rightIndex, " sum = ", root.data)
            self.print_tree(root.left)
            self.print_tree(root.right)


final = size - 1
t = Tree()
t.root = Node(0, final)
temp = final
depth = 2
if final > 7:
    depth = -2
# Finding depth
while temp >= 1:
    temp = int(temp/2)
    depth += 1

t.root = t.insert(t.root, 0, final)


for i in range(depth):
    if t.root.left.leftIndex < t.root.left.rightIndex:
        t.root.left = t.insert(t.root.left, t.root.left.leftIndex, t.root.left.rightIndex)
    if t.root.right.leftIndex < t.root.right.rightIndex:
        t.root.right = t.insert(t.root.right, t.root.right.leftIndex, t.root.right.rightIndex)

t.print_tree(t.root)
