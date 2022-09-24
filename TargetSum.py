class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = {} #cache -> HASH MAP in this case with (index,total) equal to the no of ways starting from index

        def backtrack(i,total):

            if(i == len(nums)):                      #base case: if we reach end of nums
                return 1 if total == target else 0   #1 means this is a way to reach to target else 0 = not
            
            if((i,total) in dp):       #result of this (index,total) is already present in cache
                return dp[(i,total)]

            dp[(i,total)] = (backtrack(i+1,total + nums[i])+
                            backtrack(i+1,total - nums[i]))
            #two choices i.e. either to add next value in nums or subtract it & move to next index

            return dp[(i,total)]

        return backtrack(0,0)         #calling backtrack at 0th index and initially total also equal to 0

obj = Solution()
nums = [1,1,1,1,1]
target = 3
numOfWaysToReachTarget = obj.findTargetSumWays(nums,target)       
print(numOfWaysToReachTarget)