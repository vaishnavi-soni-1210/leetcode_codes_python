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
        if(x == 2 or x == 3):
            return 1    
        
        g = x/2;
        g2 = g + 1;
        while(g != g2):
            n = x/ g;
            g2 = g;
            g = (g + n)/2;

        return int(g);

obj = Solution()
#x = 2147395599
x = 16
#x = 4
sqrRoot = obj.mySqrt(x)
print(sqrRoot)
        