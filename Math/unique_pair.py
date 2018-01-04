# Find all unique pairs with given sum k

pair_sum = 5
arr = [1, 2, 3, 4, 5]
size = len(arr)

# Using Hash

all_pairs = dict()

for i in range(size):
    all_pairs[arr[i]] = pair_sum - arr[i]

print("All Pairs : ", all_pairs)
ans = dict()

for i in range(size):
    x = all_pairs[arr[i]]
    if all_pairs.get(x):
        y = all_pairs[x]
        if all_pairs.get(y):
            # Arrange in ascending to make order unique
            if x < y:
                ans[x] = y
            else:
                ans[y] = x

print("Unique pairs : ", ans)


# Finding pairs in sorted array

lo = 0
hi = size - 1

ans = dict()

while lo < hi:
    if arr[lo] + arr[hi] == pair_sum:
        ans[arr[lo]] = arr[hi]
        lo += 1
        hi -= 1
    elif arr[lo] + arr[hi] > pair_sum:
        hi -= 1
    else:
        lo += 1

print("Unique pairs (in sorted array) : ", ans)

# number expressed as prime sum


def is_prime(n):
    s = int(n**0.5)+1
    for k in range(2, s):
        if n % k == 0:
            return False
    return True


num = 36
ans = dict()

for i in range(num):
    if is_prime(i) and is_prime(num - i):
        if i < num - i:
            ans[i] = num - i
        else:
            ans[num - i] = i

print(num, " can be expressed as prime sum", ans)

