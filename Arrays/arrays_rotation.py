# Array

arr = [1, 2, 3, 4, 5]

print("Original Array")
size = len(arr)
for i in range(size):
    print(arr[i], end=" ")

# Array Rotation

# Using temp array ,
# Linear time O(n) and Linear space O(n)

temp = [0] * size
print("\nRotated Array")

# if k is positive, shift left
# if k is negative, shift right

k = 2

for i in range(size):
    index = abs((i + k) % size)
    temp[i] = arr[index]
    print(temp[i], end=" ")

# By Rotating one by one
# constant space and O(n.k) time
print("\nRotated one by one")
k = 2
for i in range(abs(k)):
    x = arr[0]
    for j in range(size - 1):
        arr[j] = arr[j + 1]
    arr[size - 1] = x
    for j in range(size):
        print(arr[j], end=" ")
    print("")

# Juggling algorithm

size = len(arr)
k = 3


def gcd_ext(a, b):
    if a == 0:
        return b
    return gcd_ext(b % a, a)


step = gcd_ext(size, k)

for i in range(step):
    temp = arr[i]
    j = i
    while 1:
        d = (j + k) % size
        if d == i:
            # stop when you reached the initial position
            break
        arr[j] = arr[d]
        j += step

    arr[j] = temp


# Rotate by reversal
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def reverse(array, start, final):
    mid = int((final - start) / 2) + 1
    for i in range(mid):
        array[start + i], array[final - i] = array[final - i], array[start + i]
    return array


def rotate(array, k):
    last = len(arr) - 1
    array = reverse(array, 0, k - 1)
    array = reverse(array, k, last)
    array = reverse(array, 0, last)

    return array


print("Array : ", arr)
arr = rotate(arr, 3)
print("After Rotation by ", 3, " Array : ", arr)
