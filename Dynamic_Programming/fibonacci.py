# Dynamic Programming FAST method
# Fibonacci Problem


num = 7

#  First solution :
#  Using the following recurrence relation :
#  fib(0) = 0, fib(1) = 1
#  fib(n) = fib(n-1) + fib(n-2) , n > 1


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Analysing the first solution

# Using counting array finding occurrences


counting = [0] * num


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        print("fib", n-1, " + fib", n-2)
        counting[n-1] += 1
        counting[n-2] += 1
        return fibonacci(n-1) + fibonacci(n-2)


seq = fibonacci(num)
print("\nvalue of ", num, " th sequence of fibonacci is ", seq, "\n")

for i in range(num):
    print(i, " is repeated / overlapped ", counting[i], " times")

