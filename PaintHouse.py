class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def min_cost(self, costs):
        # costs[i][j] i = house number & j = color
        #eg: costs = [[17,2,17],[16,16,5],[14,3,19]]
        dp = [0,0,0]

        for i in range(len(costs)):  #for every house
            dp0 = costs[i][0] + min(dp[1],dp[2])
            dp1 = costs[i][1] + min(dp[0],dp[2])
            dp2 = costs[i][2] + min(dp[0],dp[1])

            #atlast update the whole row/cache
            dp = [dp0, dp1, dp2]

        #final result is the minimum of last row i.e. dp cache/array
        #print(dp)
        return min(dp)

obj = Solution()
costs = [[17,2,17],[16,16,5],[14,3,19]]
minimumCostOfPainting = obj.min_cost(costs)
print(minimumCostOfPainting)

#TIME COMPLEXITY = O(n) [looping for n houses]
#SPACE COMPLEXITY = O(3) = O(1) [size of cache]
