# prime factorization
# write the given number in it's prime factors

num = 91
j = 2
print(num,end=" = ")
while num != 1:
    if num % j == 0:
        num /= j
        print(j,end="*")
    else:
        j += 1
        pass
print(1)
    

# finding all factors of a given numbers

num = 36
arr = []

for i in range(1, num+1):
    if num % i == 0:
        arr.append(i)
print(arr)

arr2 =[]
for i in range(len(arr)):
    arr2.append(int(num/arr[i]))

print(arr2)


# finding all factors of 36
# 36 = [1,2,3,4,6,9,12,18,36]
# Here we observe the pattern : 1*36 = 2*18 = 3*12 =..6*6 = 36

# By this observation we have learned that
# only by going up to square_root(num)
# we can find all factors

maxItr = int(num ** 0.5) + 1
arr3 = []

num = 36

for i in range(1, maxItr):
    if num % i == 0:
        arr3.append(int(i))
        arr3.append(int(num/i))

print(arr3)
