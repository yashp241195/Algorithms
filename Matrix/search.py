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
