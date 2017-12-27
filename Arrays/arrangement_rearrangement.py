# Array : Arrangement - Rearrangement

# Segregate positive and negative

arr = [1, -2, -3, -5, -6, 7, 5, 2, 3]
size = len(arr)
low = 0
high = size - 1

for i in range(size):
    if arr[i] < 0:
        arr[i], arr[low] = arr[low], arr[i]
        low += 1
    else:
        arr[i], arr[high] = arr[high], arr[i]
        high -= 1


print(arr)

# Reverse of array and string

for i in range(int(size/2)):
    arr[i], arr[(size-1) - i] = arr[(size-1) - i], arr[i]

print(arr)
# Zig Zag sorted array 
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nArray : ", arr)
size = len(arr)

for i in range(0, size-1, 2):
    arr[i], arr[i+1] = arr[i+1], arr[i]

print("Zig-Zag Array : ", arr)

# Partition algorithm

arr = [10, 80, 30, 90, 40, 50, 70]


def partition(array):
    lo = 0
    last = len(array) - 1
    pivot = arr[last]
    hi = last - 1

    while lo <= hi:
        if pivot >= array[lo]:
            lo += 1
        else:
            array[lo], array[hi] = array[hi], array[lo]
            hi -= 1
        # print("Low ", lo, "High ", hi)
        # print(array)

    array[lo], array[last] = array[last], array[lo]
    return array


print("Partition : ", partition(arr))

#  Dutch National Flag Algorithm, or 3-way Partitioning


arr = [0, 0, 1, 1, 1, 2, 1, 2, 0, 0, 0, 1]
size = len(arr)

lo = 0
hi = size - 1
mid = 0


while mid <= hi:
    hashed = arr[mid]
    if hashed == 0:
        arr[lo], arr[mid] = arr[mid], arr[lo]

        lo += 1
        mid += 1

    elif hashed == 1:
        mid += 1
    else:
        arr[hi], arr[mid] = arr[mid], arr[hi]
        hi -= 1

print("Array : ", arr)

#  Dutch National Flag Algorithm, or 3-way Partitioning
#  utilized in partitioning algorithm

arr = [10, 80, 30, 55, 60, 65, 20, 25, 67, 50, 70]
size = len(arr)

lo = 0
last = hi = size - 1
mid = 0
p1 = arr[hi-1]
p2 = arr[hi]


while mid <= hi:

    hashed = arr[mid]
    # print("h prev", hashed, end=" ")
    if hashed < p1:
        hashed = 0
    else:
        if hashed < p2:
            hashed = 1
        else:
            hashed = 2
    # print("h new", hashed)
    if hashed == 0:
        arr[lo], arr[mid] = arr[mid], arr[lo]

        lo += 1
        mid += 1

    elif hashed == 1:
        mid += 1
    else:
        arr[hi], arr[mid] = arr[mid], arr[hi]
        hi -= 1

# print("lo", lo, "mid", mid, "hi", hi)

print("Array : ", arr)


# Min - Max Sort

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
size = len(arr)
hi = size - 1
# Using auxiliary Array
aux = [0]*size

for i in range(int(size/2)):
    aux[2*i] = arr[i]
    aux[2*i + 1] = arr[hi - i]

if hi % 2 == 0:
    aux[hi] = arr[int(size/2)]

print(arr)
print(aux)



