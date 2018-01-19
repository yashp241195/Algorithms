# Knapsack

weight = [2, 2, 3]
profit = [6, 10, 12]

last_Index = len(weight) - 1
max_weight = 5


def knapsack(max_w, w, p, i):
    if i == last_Index:
        return 0
    if max_w - w[i] > 0:
        return max(knapsack(max_w, w, p, i+1) + profit[i+1], knapsack(max_w, w, p, i+1))
    else:
        return knapsack(max_w, w, p, i+1)


y = knapsack(max_weight, weight, profit, 0)
print(y)

