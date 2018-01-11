
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
    
# Making Dynamic Programming approach

cache = [-1] * (num + 1)


def fib_dp(n, cache):
    if n == 0 or n == 1:
        cache[n] = n
        return n
    elif cache[n] != -1:
        return cache[n]
    else:
        cache[n] = fib_dp(n-1, cache) + fib_dp(n-2, cache)
        return cache[n]


seq = fib_dp(num, cache)
print("\nValue of ", num+1, " th sequence or fibonacci(", num, ")  of fibonacci is ", seq, "\n")
print(cache)


# Turn the solution around :
# previously, we were building the solution
# from fib 6 -> fib 5 -> fib 4 -> fib 3 .... fib 0
# but now we will build it from bottom up
# fib 0 -> fib 1 -> fib 2 ... fib 6..

cache = [1] * (num + 1)


def fib_turn_around(n, cache):
    cache[0] = 0
    cache[1] = 1

    for i in range(2, n+1):
        cache[i] = cache[i-1] + cache[i-2]

    return cache[n]


seq = fib_turn_around(num, cache)
print("\nValue of ", num+1, " th sequence or fibonacci(", num, ")  of fibonacci is ", seq, "\n")
print(cache)


# Fibonacci Sequence

def fib(n):

    first = 0
    second = 1
    print(first, end=", ")
    print(second, end=", ")

    third = 0
    for i in range(2, n+1):
        third = first + second
        first = second
        second = third

        print(third, end=", ")

    return third


fib(num)
