class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #loop through i in List[]
        #if buy i = i+1
        #if sell i = i+2 because there is compulsory cooldown after sell, so profit that day = 0
        DP = {}  #store key value pairs here, key = i & value = true or false i.e. buy or sell

        def DFS(i, buying):  #define a recursive function
            if(i >= len(prices)):
                return 0
            if(i, buying) in DP:
                return DP[i,buying]

            if(buying):  #buy = true
                buy = DFS(i+1, not buying) - prices[i]
                #calculating profit, changing state to opposite of whatever value is of buying
                cooldown = DFS(i+1, buying)  #state won't change                
                DP[i,buying] = max(buy,cooldown)  #wichever decision gives max profit
            else:        #sell
                sell = DFS(i+2, not buying) + prices[i]  
                #calculating profit, changing state to opposite of whatever value is of buying
                #+2 is for compulsory cooldown day
                cooldown = DFS(i+1, buying)  #state won't change  
                DP[i,buying] = max(sell,cooldown)  #wichever decision gives max profit

            #print(DP) #have a look how DP will be stored
            return DP[i,buying]            

        #call the recursive function
        return DFS(0,True)

obj = Solution()
prices = [1,2,3,0,2]
maxPossibleProfit = obj.maxProfit(prices)
print(maxPossibleProfit)

#time and complexity = O(n) because iterating t times & caching n values