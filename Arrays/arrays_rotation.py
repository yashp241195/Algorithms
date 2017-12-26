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

print(arr)

# By Reversal

    
    