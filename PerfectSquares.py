class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        #say n = 12
        dp = [n]* (n+1)    #storing the results from root branch 0 till it reaches target
        dp[0] = 0   #very imp step, code will messup without this

        for target in range(1,n+1):  #outer loop for the height of the tree till it reaches target
            for sqrt in range(1,target+1):  #target is the subproblem here, and sqrt is not the actual square
                square = sqrt * sqrt   #we have already used a square at this position so count it below
                if(target-square < 0):  #we have reached till the target
                    break
                dp[target] = min(dp[target], 1 + dp[target-square])  #1+ here because we have used a square already

        return dp[n]

obj = Solution()
n = 12  # 4+4+4
leastNumOfPerfectSqToGetSumN = obj.numSquares(n)
print(leastNumOfPerfectSqToGetSumN)

#time complexity = O(n*sqrt(n)) 
#space complexity => O(n+1)

#note: time limit exceeded for n=5254