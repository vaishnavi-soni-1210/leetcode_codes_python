class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        DP = [[0] * (len(coins)+1) for i in range(amount+1)]
        #2d matrix of size amount+1 * len(coins)+1 initialized with 0 at every position
        #i.e. for 5 Rs & 3 coins its an array with 6 rows and 4 columns each
        #imp: amount will go in reverse i.e. 5,4,3,2,1,0.. so, final ans = DP[5,0] 

        DP[0] = [1] * (len(coins) + 1)      #base case
        #fill last row with all ones i.e. to amount 0, no. of ways possible with each coin
        #print(DP)

        for a in range(1,amount+1):
            for i in range (len(coins)-1,-1,-1):
                DP[a][i] = DP[a][i+1]  #result of remaining coins i.e. bottom
                if(a - coins[i] >= 0):  #amount is greater than coin 
                    DP[a][i] = DP[a][i] + DP[a-coins[i]][i]  #sum of bottom result and amount + coin value

        return DP[amount][0]  #last result is the 0th column & topmost row of amount

obj = Solution()
coins = [1,2,5]
amount = 5
noOfWaysChangeCoinsToAmount = obj.change(amount,coins)
print(noOfWaysChangeCoinsToAmount)

#time complexity: O(amount * len(coins)) bcz using loop for each of amount & len(coins) respectively
#space complexity: O(amount * len(coins)) bcz caching all cells

#say amount = 5 = n, no of coins = 3 = m, then:
#time complexity = O(n*m), and space complexity = O(n*m) all cells are stored