class Solution(object):    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #corner case: if there is only 1 house i.e. only 1 element in array [2] 
        # then for soln1 & soln 2 we are sending empty arrays, thus result = 0
        if(len(nums) == 1):
            return nums[0]

        #list = [2,3,4], consider 0,0,[2,3,4]
        soln1,soln2 = 0,0
        soln1 = self.calcMaxRob(nums[1:]) #skip 1st element
        soln2 = self.calcMaxRob(nums[:-1]) #skip last element       

        return(max(soln1,soln2))

    def calcMaxRob(self, nums):
        rob1,rob2 = 0,0
        for n in nums:
            temp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

obj = Solution()
nums = [2,3,4]
maxRob = obj.rob(nums)
print(maxRob)        

#here time complexity = O(n) as we are looping n times or time depends on n items
#& space complexity is O(1) as no extra space used