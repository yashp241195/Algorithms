# print binary combinations

def binary(answer, i):
    if i == len(answer):
        print(answer)
    else:
        answer[i] = 0
        binary(answer, i + 1)
        answer[i] = 1
        binary(answer, i + 1)


ans = [0] * 3
binary(ans, 0)

# Permutation with repetition

arr = [1, 2, 3]
size = len(arr)

# max index is number of places you want to place stuff
maxIndex = 2


def permute(answer, i):
    if i > maxIndex:
        print(answer)
    else:
        for j in range(size):
            answer[i] = arr[j]
            permute(answer, i+1)


ans = [0] * size
permute(ans, 0)

# without repetition

arr = [1, 2, 3]
size = len(arr)


def permute(answer, i):
    if i == size:
        print(answer)
    else:
        for j in range(i, size):
            answer[i], answer[j] = answer[j], answer[i]
            permute(answer, i+1)
            answer[i], answer[j] = answer[j], answer[i]


permute(arr, 0)

# repeat count

arr = [1, 1, 2, 1, 1, 2, 1, 1, 3, 1, 4, 1]

size = len(arr)

for i in range(size):
    v = abs(arr[i])

    if arr[v] < 0:
        arr[v] -= 1
        continue
    arr[v] = -1

print(arr)

for i in range(size):
    if arr[i] < 0:
        print(i, " is repeated ", abs(arr[i]), "times")
