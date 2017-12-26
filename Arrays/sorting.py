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
