class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        #cost = [10, 15, 20] 0
        cost.append(0)

        #loop till last 3rd value because the sum of last two are anyway gonna be same as 2nd last
        n = len(cost)
        for i in range(n-3,-1,-1): #if i take n-2, cost[i+2] i.e. cost[4] will throw array index out of bound
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])

        minimumCost = min(cost[0],cost[1]) #because we can start either from step 0 or 1 i.e. index 0/1
        return minimumCost

        #check what is the difference between: 
        #for i in range(n-1) and for i in rane(n-3,-1,-1)

obj = Solution()
cost = [10, 15, 20]
minimumCost = obj.minCostClimbingStairs(cost)
print(minimumCost)

#time complexity = O(n), space complexity = O(n+1)