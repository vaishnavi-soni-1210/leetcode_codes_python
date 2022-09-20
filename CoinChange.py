class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [(amount+1)] * (amount + 1)      
        dp[amount] = amount + 1  
        #print(dp)    
        #digit after * in array represents array size in python, i.e. 0,1....amount
        #and value inside [] is the max value to store in dp array

        #base case, how many coints to get sum 0
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:  #for each coin
                if(a-c >= 0):     #if the amount is greater than or equal to the current coin
                    dp[a] = min(dp[a], 1 + dp[a-c])
                    # 1 + dp[a-c] is referring to eg: a = 7, c = 3, => 1 + dp [7-3] i.e. 1 + dp[4]

        if(dp[amount] != amount+1): #default value that we have stored in dp, if the coins doesn't sum up to amount
            return dp[amount]
        else:
            return -1

obj = Solution()
#amount = 7
#coins = [1,3,4,5]
coins = [2147483647]
amount = 2
noOfCoins = obj.coinChange(coins,amount)
print(noOfCoins)

#time complexity: O(amount * len(coins)) bcz using 2 for loop each of amount & len(coins) respectively
#space complexity: O(amount) bcz using array of size amount
