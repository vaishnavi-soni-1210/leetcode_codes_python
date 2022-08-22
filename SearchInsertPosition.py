class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        #if needs to be appended at the end
        if(nums[len(nums)-1]) < target:
            index = len(nums)
        if(index > 0):
            return index
        for i in range(0,len(nums)):
            if(nums[i] >= target):
                index = i
                break
        return index
obj = Solution()
nums = [1,3,5,6]
indexToInsert = obj.searchInsert(nums,7)
print(indexToInsert)
            
