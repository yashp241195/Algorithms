# Range Query

arr = [1,2,3,4,5,6,7,8]
size = len(arr)
sum = 0
arr2 = [0]*size

for i in range(size):
    sum += arr[i]
    arr2[i] = sum

print(arr)
print(arr2)

# To find the sum from index 1 to 4

left = 0
right = 4

answer = arr2[right]
if left > 0:
    answer -= arr2[left - 1]

print(answer)

# update index

index = 5
updated_value = 9
print("Value at index ", index," is ", arr[index], ", Updated Value : ", updated_value)
delta = updated_value - arr[index]
print("Difference : ", delta)

for i in range(index, size):
    arr2[i] += delta

print(arr2)
