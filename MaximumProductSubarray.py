class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = max(nums)  #if nums has only 1 number or if 1 number is greater than any product
        currMin = currMax = 1 

        for n in nums:
            if(n==0):       #handling edge case
                currMin = currMax = 1 
                continue
            temp = currMax
            currMax = max(currMax * n, currMin * n,n) #3 cases considering +,-,0 values
            currMin = min(temp *n, currMin * n,n) #3 cases considering +,-,0 values
            result = max(result, currMax)
        return result

obj = Solution()
nums = [2,3,-2,4]
maxProduct = obj.maxProduct(nums)
print(maxProduct)

#time complexity = O(n) as we are iterating n times
#space complexity = O(1) as we are using only 2 variables to store values
