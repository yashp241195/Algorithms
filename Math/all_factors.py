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
