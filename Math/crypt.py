# Count number of ways to decode the given encoded message,
# if a = 1, b = 2 ... z = 26
# or can be asked as count the number of ways to decode Ceasar Cypher




def decode(array, ctr, i):
    if i < len(array)-1:
        if array[i] == 0:
            ctr += 0
        elif array[i] == 1:
            print(array[i])
            print(array[i], array[i + 1])
            ctr += 2
        elif array[i] == 2:
            if array[i+1] < 7:
                print(array[i])
                print(array[i], array[i + 1])
                ctr += 2
            else:
                print(array[i])
                ctr += 1
        else:
            print(array[i])
            ctr += 1
        ctr = decode(array, ctr, i+1)
    return ctr


c = 0
arr = [2, 0, 4, 1, 0]
# arr = [1,1,1]
c = decode(arr, c, 0)
# do c-1 as to prevent over count 
print("ctr : ", c-1)
