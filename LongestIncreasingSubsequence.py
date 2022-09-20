class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        DP = [1] * len(nums) #set every value to 1 => DP = [1 1 1 1]
        #DP[len(nums)-1] = 1 #base case, for last index its always gonna be 1

        for i in range(len(nums)-1,-1,-1): #start from i = 3
            #print('i=%d'%(i))
            for j in range(i+1,len(nums)): #this one will not execute for the first time whne i = 3
                #print('j=%d'%(j))
                if(nums[i] < nums[j]):
                    DP[i] = max(DP[i], 1+DP[j])

        return max(DP)

obj= Solution()
nums = [1,2,4,3]
result = obj.lengthOfLIS(nums)
print(result)
