# Spiral Matrix 2D

size = 6

arr = []

q = 1
for i in range(size):
    new = [0]*size
    for j in range(size):
        new[j] = 0
    arr.append(new)

fc = 0
lc = size - 1

fr = 0
lr = size - 1

for k in range(int(size/2)):
    i = fr
    j = fc

    while j < lc:
        arr[i][j] = q
        q += 1
        print(i,j,end=", ")
        j += 1
    arr[i][j] = q
    q += 1
    print(i, j, end=", ")
    lc = j
    i += 1

    fr = k

    print("")
    while i < lr:
        arr[i][j] = q
        q += 1
        print(i, j, end=", ")
        i += 1
    arr[i][j] = q
    q += 1
    print(i, j, end=", ")
    j -= 1

    print("")
    while j > fc:
        arr[i][j] = q
        q += 1
        print(i, j, end=", ")
        j -= 1
    arr[i][j] = q
    q += 1
    print(i, j, end=", ")
    i -= 1

    print("")
    while i > fc:
        arr[i][j] = q
        q += 1
        print(i, j, end=", ")
        i -= 1

    lr -= 1
    fr += 1
    fc += 1
    lc -= 1
    print("")


print("\n\nSpiral 2D Array")
for i in range(size):
    for j in range(size):
        if arr[i][j] < 10:
            print("", end=" ")
        print(arr[i][j], end="  ")
    print("")
    
