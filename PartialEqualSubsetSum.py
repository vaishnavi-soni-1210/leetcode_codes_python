class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if(sum(nums)%2 !=0):  #sum is odd so partition not possible
            return False
        
        DP = set()
        DP.add(0)  #base case 
        target = sum(nums)/2

        for i in range(len(nums)-1,-1,-1):
            DPNew = set()
            for total in DP:  #for every sum we already have in DP
                #DP.add(total + nums[i]) - not possible because we can't update DP set while iterating through it
                #so use another set to store updated values from this loop   
                DPNew.add(total)             #store previous values also in new set
                DPNew.add(total+nums[i])
            DP = DPNew        #reassign to get old + new values in DP
        
        if(target in DP):  #if target is present in the set
            return True
        else:
            return False

obj = Solution()
nums = [1,5,11,5]
result = obj.canPartition(nums)
print(result)
