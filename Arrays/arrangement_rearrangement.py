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

