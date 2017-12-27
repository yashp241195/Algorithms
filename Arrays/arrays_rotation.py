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


def pair_sum(array, add, left, right):
    if left < right:
        total = arr[left] + arr[right]
        if add == total:
            return arr[left], arr[right]
        elif add < total:
            return pair_sum(array, add, left, right - 1)
        else:
            return pair_sum(array, add, left + 1, right)
    return False


addition = 16
last = len(arr)-1
pivot = find_pivot(arr,0,last)
result1 = pair_sum(arr, addition, 0, pivot-1)
result2 = pair_sum(arr, addition, pivot, last)
print("\nFinding pair with sum ", addition)
if result1 is False and result2 is False:
    print("Pair does not exist")
else:
    if result1 is not False:
        print(result1)
    if result2 is not False:
        print(result2)


# Maximum value of sum(i*arr[i])
#   R_0 =0*arr[0] + 1*arr[1] + ... (n-1)*arr[n-1]
#   R_1 =0*arr[n-1] + (1+1)*arr[1] + ... (n-1)*arr[n-2]
#   R_2 =0*arr[n-2] + (1+1)*arr[n-1] + ... (n-1)*arr[n-3]
#   R_3 =0*arr[n-3] + (1+1)*arr[n-2] + ... (n-1)*arr[n-4]
#   R_3 - R_2 = array_sum - (n-1)*arr[n-4]
#   R_j - R_j-1 = array_sum - (n)*arr[n-j]

# returns max possible value of Sum(i*arr[i])
def maxSum(arr):
    # stores sum of arr[i]
    arrSum = 0

    # stores sum of i*arr[i]
    currVal = 0

    n = len(arr)

    for i in range(0, n):
        arrSum = arrSum + arr[i]
        currVal = currVal + (i * arr[i])

    # initialize result
    maxVal = currVal

    # try all rotations one by one and find the maximum
    # rotation sum
    for j in range(1, n):
        currVal = currVal + arrSum - n * arr[n - j]
        if currVal > maxVal:
            maxVal = currVal

    # return result
    return maxVal


# test maxsum(arr) function
arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Max sum is: ", maxSum(arr))





