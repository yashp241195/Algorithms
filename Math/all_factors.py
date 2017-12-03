# finding factors of 36
# 36 = [1,2,3,4,6,9,12,18,36]
# Here we observe the pattern : 1*36 = 2*18 = 3*12 =..6*6 = 36

from math import sqrt
class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        
        L=[]
        for i in range(1,int(sqrt(A))+1):
            if(A%i==0):
                L.append(int(i))
                if(i!=sqrt(A)):
                    L.append(int(A/i))
        L.sort()
        return(L)

    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        # 1 is not a prime number
        if A == 1:
            return 0
    	upperLimit = int(A**0.5)
    	for i in xrange(2, upperLimit + 1):
    		if i < A and A % i == 0:
    			return 0
    	return 1
    
    # Unique pair of prime numbers upto A
    
    def all_primes_with_sum(A):
        ans = []
        if A == 4:
            ans.append(2)
            ans.append(2)
            return ans
        else:
            if A > 4:
                li = []
                for i in range(2, A+1):
                    count = 0
                    sq = int(i ** 0.5) + 1
                    for j in range(2, sq):
                        if i % j == 0:
                            count += 1
                            break
                    if count == 0:
                        li.append(i)

                pair_table = []

                for i in range(len(li)):

                    org = li[i]
                    cmp = A - org
                    ctr = 0

                    for k in range(2, int(cmp**0.5)+1):
                        if cmp % k == 0:
                            ctr += 1

                    if ctr > 0:
                        continue

                    pair = [org, cmp]

                    pair_cmp = [cmp, org]
                    if pair_cmp in pair_table:

                        if org > cmp:
                            ans.append(cmp)
                            ans.append(org)
                        else:
                            ans.append(org)
                            ans.append(cmp)
                    else:
                        pair_table.append(pair)

                return ans

    # Best Solution --
    
    def prime_sum(A):
        for i in range(2, int(A/2)+1):
            a = i
            b = A - a
            if self.isPrime(a) and self.isPrime(b):
                print(a, "", b)




    
