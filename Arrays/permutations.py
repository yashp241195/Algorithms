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
