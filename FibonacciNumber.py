class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        #base cases
        if(n==0): return 0
        if(n==1): return 1
        
        #approach 1 - recursion
        #return self.fib(n-1) + self.fib(n-2)

        previous1, previous2 = 1,0
        output = 0

        for i in range(2,n+1):
            output = previous1+previous2
            previous2 = previous1
            previous1 = output

        return output

obj = Solution()
output = obj.fib(4)
print(output)

#time complexity = O(n)
#space complexity = O(1) because we are simply using variables to store latest value & not previous