# Min max array (Using modulo arithmetic)

arr = [1, 2, 3, 4, 5, 9]
size = len(arr)

minIndex = 0
maxIndex = size - 1

maxim = max(arr) + 1
print(arr)

for i in range(size):
    if i % 2 == 0:
        arr[i] += (arr[maxIndex] % maxim) * maxim
        maxIndex -= 1
    else:
        arr[i] += (arr[minIndex] % maxim) * maxim
        minIndex += 1

# Reforming the array
for i in range(size):
    arr[i] = int(arr[i]/maxim)

print(arr)
