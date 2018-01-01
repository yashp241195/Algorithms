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


# Matrix Search

for q in range(7,37):
    key = q
    print("\nkey", key)
    i = 0
    j = size - 1

    if key > arr[i][j]:
        i = size - 1
        j = 0

    print("\ni=", i, "j=", j,"val=", arr[i][j])

    k = 0

    while k < 100:
        # print(arr[i][j])

        if key < arr[i][j]:
            i -= 1
        else:
            j += 1
        if arr[i][j] == key or i < 0 or j >= size - 1:
            break

        k += 1
    if arr[i][j] == key:
        print("Key : ", arr[i][j]," found at i = ", i,", j = ",j)
    else:
        print("Key not found")
