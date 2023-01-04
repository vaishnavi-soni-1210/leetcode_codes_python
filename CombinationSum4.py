class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #eg: target = 4, input = [1,2,3]
        dp = {0 : 1}  #hashmap for caching and base case dp[0] = 1
        for total in range(1,target+1):
            dp[total] = 0   #there might be 0 ways to reach to target initially
            for n in nums:
                dp[total] += dp.get(total-n,0)
                #above stmt is like ternary operator in python which says:
                #if dp has value = (total-n), then use (total-n) else 0
                #this condition is added because there is a chance that (total-n) is a -ve number, 
                # hence not present in dp
        
        return dp[target]

obj = Solution()
nums = [1,2,3]
target = 4
numberOfWaysToGetTargetSum = obj.combinationSum4(nums,target)
print(numberOfWaysToGetTargetSum)

#time complexity = O(n*m)
#where n is the target & m is the size of input array bcz we need to loop for each value from array