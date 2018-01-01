# Matrix Diagonal print

size = 6

arr = []

q = 1
for i in range(size):
    new = [0]*size
    for j in range(size):
        new[j] = q
        q += 1
    arr.append(new)


print("Array")
for i in range(size):
    print(arr[i])

for i in range(size):
    k = i
    j = 0
    while j <= i and k >= 0:
        print(arr[k][j], end=" ")
        k -= 1
        j += 1
    print("")


for j in range(1, size):
    i = size - 1
    k = j
    while k < size and i >= 0:
        print(arr[i][k], end=" ")
        k += 1
        i -= 1

    print("")


