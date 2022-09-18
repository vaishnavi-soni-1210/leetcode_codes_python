class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #[rob1,rob2,n,n+1,n+2...]
        rob1 = 0
        rob2 = 0

        #loop through all the houses
        for n in nums:
            temp = max((rob1+n),rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

obj = Solution()
nums = [1,2,3,1]
maxRob = obj.rob(nums)
print(maxRob)

#here time complexity = O(n) as we are looping n times or time depends on n items
#& space complexity is O(1) as no extra space used