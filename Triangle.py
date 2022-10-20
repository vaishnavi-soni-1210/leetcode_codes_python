class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        #bottom to up 
        #dp array is gonna keep the track of current row
        dp = [0] * (len(triangle)+1) #initialize the dp, and add an extra 1 bcz each row has 1 more than prev
        #print(dp)

        #iterate through triangle in reverse
        for row in triangle[::-1]:
            #to get the index and value at the same time in python, use enumerate
            for i,n in enumerate(row):
                #dp contains the row below current 'row', where we will store results
                dp[i] = n + min(dp[i],dp[i+1])

        return dp[0]  #first element of dp will contain ans

obj = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
result = obj.minimumTotal(triangle)
print(result)