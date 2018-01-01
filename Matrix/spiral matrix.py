size = 6

arr = []

q = 1
for i in range(size):
    new = [0]*size
    for j in range(size):
        new[j] = q
    arr.append(new)


for k in range(size):
    if k % 2 == 0:
        i = k
        j = 0

        while j <= k:
            arr[i][j] = q
            q += 1
            print(i,j,end=", ")
            j += 1

        i -= 1
        j -= 1

        while i >= 0:
            arr[i][j] = q
            q += 1
            print(i, j, end=", ")
            i -= 1

    else:
        i = 0
        j = k

        while i <= k:
            arr[i][j] = q
            q += 1

            print(i,j,end=", ")
            i += 1

        i -= 1
        j -= 1

        print(i, j, end=", ")

        while j >= 0:
            arr[i][j] = q
            q += 1

            print(i, j, end=", ")
            j -= 1
    print("")


print("Array")
for i in range(size):
    print(arr[i])
