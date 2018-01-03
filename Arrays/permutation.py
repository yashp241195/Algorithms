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
