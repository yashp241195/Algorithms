# Array

arr = [1, 2, 3, 4, 5]

print("Original Array")
size = len(arr)
for i in range(size):
    print(arr[i], end=" ")

# Array Rotation

# Using temp array ,
# Linear time O(n) and Linear space O(n)

temp = [0]*size
print("\nRotated Array")

# if k is positive, shift left
# if k is negative, shift right

k = 2

for i in range(size):
    index = abs((i+k) % size)
    temp[i] = arr[index]
    print(temp[i], end=" ")


# By Rotating one by one
# constant space and O(n.k) time
print("\nRotated one by one")
k = 2
for i in range(abs(k)):
    x = arr[0]
    for j in range(size-1):
        arr[j] = arr[j+1]
    arr[size - 1] = x
    for j in range(size):
        print(arr[j], end=" ")
    print("")

# Detect if array is sorted in increasing order or not

arr = [1, 2, 3, 4, 5]
size = len(arr)

isPerfect = True

for i in range(size-1):
    if arr[i+1] > arr[i]:
        pass
    else:
        isPerfect = False

if isPerfect:
    print("Array is Ascending")
else:
    print("Not in Ascending")


# Find all sub arrays of size k within the array
# Don't confuse sub arrays with subset
# total possible subsets = 1+2+3+..n = n*(n-1)/2
# sub arrays are always contiguous

arr = [1, 2, 3, 4, 5]
size = len(arr)

for k in range(1, size):
    for i in range(size-k+1):
        for j in range(i, i+k):
            print(arr[j], end=" ")
        print("")


