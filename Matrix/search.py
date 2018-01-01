# Sorted Matrix Search

size = 6

arr = []

q = 1
for i in range(size):
    new = [0]*size
    for j in range(size):
        new[j] = q
        q += 1
    arr.append(new)
    
    
for q in range(1, 37):
    key = q
    print("\nkey : ", key)
    i = 0
    j = size - 1

    if key > arr[i][j]:
        i = size - 1
        j = 0

        print("\ni=", i, "j=", j,"val=", arr[i][j])

        while 1:

            if key < arr[i][j]:
                i -= 1
            else:
                j += 1
            if arr[i][j] == key or i < 0 or j >= size-1:
                break
    else:
        i = 0
        j = 0
        print("\ni=", i, "j=", j, "val=", arr[i][j])

        while j < size:
            if arr[i][j] == key:
                break
            j += 1

    if arr[i][j] == key:
        print("Key : ", arr[i][j], " found at i = ", i, ", j = ", j)
    else:
        print("Key not found")

