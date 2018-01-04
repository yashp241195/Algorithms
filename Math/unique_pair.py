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
