# Count number of ways to decode the given encoded message,
# if a = 1, b = 2 ... z = 26
# or can be asked as count the number of ways to decode Ceasar Cypher
# basically, for eg 111 we can decode it as 1,1,1 or 11,1 or 1,11
# for a given particular index, we have two options atmost either take it as i+1 or i+2 
# means this functions seems like f(x) = f(x+1)+f(x+2) .. with some conditions
# so it seems similar to fibonacci for the worst case and also be done with dynamic programming
# due to overlaping sub structures


def decode(array, i):
    if i < len(array)-1:
        ctr = 1
        if array[i] == 0:
            return 0
        elif array[i] == 2:
            if array[i+1] < 7:
                ctr += 1
                ctr = decode(array, i + 1) + decode(array, i + 2)
        elif array[i] == 1:
            ctr += 1
            ctr = decode(array, i + 1) + decode(array, i + 2)
        else:
            ctr = decode(array, i + 1)
        return ctr
    return 1


# arr = [1,1,1]
arr = [1, 2, 1, 2, 3]
c = decode(arr, 0)
print("Count : ", c)

