class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #adding 1 in the beginning & end
        nums = [1]+nums+[1]

        dp = {}  #cache to store results i.e. hashmap (L,R)

        def dfs(l,r):
            #base cases
            #if(l == r): #only 1 value left in nums or only 1 balloon left to pop #need not to consider here
            
            if(l > r):  #out of bounds
                return 0  
            if (l,r) in dp:      #already calculated earlier & return
                return dp[(l,r)]

            dp[(l,r)] = 0     #initialize with 0 i.e. no of coins = 0
            for i in range(l,r+1):
                coins = nums[l-1]*nums[i]*nums[r+1]
                coins = coins + dfs(l,i-1) + dfs(i+1,r)  #new left and right will be updated
                dp[(l,r)] = max(dp[(l,r)], coins)
            
            return dp[(l,r)]
        
        return dfs(1,len(nums)-2)   #excluding the 1,1 appended to consider left and right

obj = Solution()
nums = [3,1,5,8]
maxNoOfCoins = obj.maxCoins(nums)
print(maxNoOfCoins)

#Space complexity = O(n^2) because we are storing for every value in nums & in 2D array i.e. DP[L][R]
#Time complexity = O(n^3) 
#because the total no of sub problems will be O(n^2), & in each subproblem, we'll look for n values
#Therefore, O(n^2 * n) = O(n^3)