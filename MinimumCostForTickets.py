class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        #Input: days = [1,4,6,7,8,20], costs = [2,7,15]
        #Output: 11
        dp = {}   #cache or hashmap

        def dfs(i):
            #base cases
            if(i == len(days)):
                return 0  #if array of days ends
            if(i in dp):
                return dp[i]  #if already calculated

            dp[i] = float("inf")  #initialize the dp to infinity

            #2 for loops parallely in python, this array will run by default untill d/c > 0
            for d,c in zip([1,7,30],costs):
                j = i      #using variable j to determine actual day number, while i is index of days
                while (j<len(days) and days[j] < (days[i]+d)):
                    j=j+1
                #after above while loop, j is having actual 'day' after which we need to purchase pass again
                #while loop will execute 1 time when we use 1 day pass, 7 times when we use 7 day pass 7 30 times when we use a 30 day pass
                #so while loop will execute 38 times i.e. linnear time complexity
                dp[i] = min(dp[i],c+dfs(j))

            return dp[i]

        return dfs(0)

obj = Solution()
days = [1,4,6,7,8,20]
costs = [2,7,15]
minimumCost = obj.mincostTickets(days,costs)

#space complexity = O(1) bcz no extra space
#time complexity = O(n*38) = O(n)