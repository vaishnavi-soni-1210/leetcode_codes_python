class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #BFS greedy - breadth first search
        #eg: nums = [2,3,1,1,4], o/p = 2
        result = 0 #initially 0 steps
        l = r = 0  #set the left and right boundary of the positions/indexes that we can reach at every step

        #loop while right boundary is still inbound
        while(r < len(nums)-1):
            farthest = 0   #variable to see how farthest we can reach from a given index
            for i in range(l,r+1):
                farthest = max(farthest,i + nums[i])
            #update left & right boundaries for the next step
            l = r+1               
            r = farthest
            result = result + 1   #imp
        
        return result

obj = Solution()
nums = [2,3,1,1,4]
minNumOfSteps = obj.jump(nums)
print(minNumOfSteps)

#time complexity = O(n)
#space complexity = O(1)
