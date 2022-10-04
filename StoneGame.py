class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        dp = {}  #subarray using (l,r) each time & Max Alice's total for each subarray

        #return Max of Alice's total
        def DFS(l,r):

            #base cases
            if(l>r):
                return 0
            if(l,r) in dp:
                return dp[(l,r)]

            #consider Bob's choices as well
            #IMP: how to determine if its Alice's turn or Bob's?
            #if remaining num of elements is even then Alice's turn else Bob's, bcz total elements are even
            even = True if (r-l)%2 == 0 else False  #total by 2 is 0 or not

            #use above variable to determine whose turn is this & set l,r if its Alice's turn else l,r=0
            left = piles[l] if even else 0
            right = piles[r] if even else 0

            #Alice has 2 choices either to choose l or r index everytime, so subproblems will be remaining arrays
            #DFS(l+1,r)  #remaining subarray, if chosen left by Alice
            #DFS(l,r-1)  #remaining subarray, if chosen right by Alice

            dp[(l,r)] = max((DFS(l+1,r)+left),(DFS(l,r-1)+right))

            return dp[(l,r)]

        return (DFS(0,len(piles)-1) > (sum(piles)-DFS(0,len(piles)-1)))
        #return (maxTotalOfAlice > maxTotalOfBob)

obj = Solution()
piles = [5,1,100,6]
ifAliceWins = obj.stoneGame(piles)
print(ifAliceWins)

#left and right can be any values from 0 to n, so time complexity = O(n*n) = O(n^2)