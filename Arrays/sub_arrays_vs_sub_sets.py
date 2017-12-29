
# Find all sub arrays of size k within the array
# Don't confuse sub arrays with subset
# total possible subsets = 1+2+3+..n = n*(n+1)/2
# sub arrays are always contiguous

arr = [1, 2, 3, 4, 5]
size = len(arr)

for k in range(1, size):
    for i in range(size-k+1):
        for j in range(i, i+k):
            print(arr[j], end=" ")
        print("")

# Find all subsets
# hint: for each level/depth of tree make sure i value is same

SET = [1, 2, 3]
size = len(SET)
answer = [None]*size


def subsets(subset, i):
    if i == size:
        print(subset)
    else:
        subset[i] = 0
        subsets(subset, i+1)
        subset[i] = SET[i]
        subsets(subset, i+1)


subsets(answer, 0)
