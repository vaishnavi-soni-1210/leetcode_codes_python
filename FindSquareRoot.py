import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x == 0):
            return 0
        if(x == 1):
            return 1
        
        #using binary search, loop from 0 to (x + 1), & sqrRoot * sqrRoot = x
        left = 0
        right = x+1
        mid = 0
        while(left < right):
            mid = int((left + (right-1))/2)

            if(mid*mid > x): #consider left part of mid
                right = mid
            else: #consider right part of mid
                left = mid + 1

        return left -1 #not returning mid because in between 3 & 4 mid will be 3 & square root can't be 3 so returning previous number from it

obj = Solution()
x = 2147395599
#x = 16
#x = 4
sqrRoot = obj.mySqrt(x)
print(sqrRoot)