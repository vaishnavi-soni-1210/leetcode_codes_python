class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #true = [2,3,1,1,4]
        #false = [3,2,1,0,4]
        goal = len(nums)-1
        for i in range(len(nums)-1,-1,-1):  #reverse loop
            if(i+nums[i] >= goal):    #if we can reach to the goal from i
                goal = i     #reset the goal one step closer
        return True if(goal == 0) else False   #if we reach to the 0th index, goal is reachable
           
obj = Solution()
nums = [2,3,1,1,4]
#nums = [3,2,1,0,4]
result = obj.canJump(nums)
print(result)

# -time complexity = O(n)
# -space complexity = O(1)