class Solution(object):
    def climbStairs(self,n):
        """
        :type n: int
        :rtype: int
        """
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        
        return one

    #check what is the difference between: 
    #for i in range(n-1) and for i in rane(n-3,-1,-1)

    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n == 1 or n == 2 or n == 3):
            return n

        #using the concept of fibonacci series where "no of ways" = fibonacci(n+1)
        #and for (n+1)th stair = fibonacci(n-1) + fibonacci(n-2)
        numberOfWays = self.fib(n+1)
        return numberOfWays    

    def fib(self,n):
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)  

# approach is explained in txt, i.e. brute force recursive approach (fibbonaci series formula [n = (n-1)+(n-2)])   
obj = Solution()
n = 39
#n = 5
numberOfWays = obj.climbStairs(n)
print(numberOfWays)

#time complexity = O(n) bcz each result(n times) depends on previous subproblem, 
#space complexity = O(1), because we r only using 2-3 variables