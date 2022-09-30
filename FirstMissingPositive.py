class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        #first loop to replace -ves with 0
        for i in range(len(nums)):
            if(nums[i]<0):
                nums[i] = 0
        
        #second loop to mark the existance of every value from range 1 to len(nums)
        for i in range(len(nums)):
            value = abs(nums[i])  #making it positive, if in case its already marked negative
            if(1 <= value <= len(nums)):  #only if nums[i] is inbound eg: in below eg if nums[i] is +-77, then should not be considered
                if(nums[value-1] > 0):
                    nums[value-1] = nums[value-1]*-1
                elif(nums[value-1] == 0):  #edge case
                    nums[value-1] = -1*(len(nums)+1)  #mark it -ve & out of bounds
        
        #third loop, to check which INDEX is left positive
        for i in range(1,len(nums)+1):
            if(nums[i-1] >= 0):
                return i    #i is the missing +ve int as index corresponding to it has no mark or not 0
        
        return (len(nums)+1)  #else return len(nums)+1 as missing +ve
            
obj = Solution()
nums = [1,2,0]
missing = obj.firstMissingPositive(nums)
print(missing)