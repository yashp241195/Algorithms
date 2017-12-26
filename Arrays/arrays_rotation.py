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

# Binary Search in rotated Array

arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]


def binary_search(array, key, left, right):
    if left < right:
        mid = int((right + left)/2)
        if key == array[mid]:
            return mid
        elif key < array[mid]:
            return binary_search(array, key, left, mid)
        elif key > array[mid]:
            return binary_search(array, key, mid+1, right)


def rotated_binary_search(array, key, left, right, pivot):
    if key == array[pivot]:
        return pivot
    elif key == array[pivot - 1]:
        return pivot - 1
    elif key == array[left]:
        return left
    elif key == array[right]:
        return right
    else:
        if key > array[left]:
            return binary_search(array, key, left, pivot-1)
        else:
            return binary_search(array, key, pivot, right)


def find_pivot(array, left, right):
    mid = int((right + left)/2)
    if array[mid] > array[mid+1]:
        return mid + 1
    else:
        if array[left] > array[mid]:
            return find_pivot(array, left, mid - 1)
        else:
            return find_pivot(array, mid + 1, right)


print(arr)
last = len(arr)-1
pivot = find_pivot(arr, 0, last)

print("Pivot Index : ", pivot, "Pivot Element : ", arr[pivot])
# for verification :
for i in range(last+1):
    key2 = arr[i]
    index = rotated_binary_search(arr, key2, 0, last, pivot)
    print("key : ",key2," Verified Key : ",arr[index])













