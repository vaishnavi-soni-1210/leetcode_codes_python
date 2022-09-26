class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        #declare a 2d array
        #cache = [[float("inf")] * (len(word2)+1) for i in range(len(word1)+1)]   
        #print(cache)
        #initialize the 2d array with float(infinity) at each position
        cache = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        #initialize the 2d array with 0 at each position
        #print(cache)
        
        #corner cases
        for j in range(len(word2)+1):    #if word1 = "" & word2 = "abc", fill last row with 3,2,1,0
            cache[len(word1)][j] = len(word2)-j
        for i in range(len(word1)+1):    #if word1 = "abc" & word2 = "", fill the last column with 3,2,1,0
            cache[i][len(word2)] = len(word1)-i
        
        #print(cache)

        #loop through all remaining cells in the grid
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if(word1[i] == word2[j]):   #go diagonally & operation = 0
                    cache[i][j] = 0 + cache[i+1][j+1]
                else:    #operations = 1 & min(right(insert), bottom(delete), diagonal(replace))
                    cache[i][j] = 1 + min(cache[i][j+1], cache[i+1][j], cache[i+1][j+1])
        
        #print(cache)
        return cache[0][0]

obj = Solution()
word1 = "abd"
word2 = "acd"
minNoOfOperations = obj.minDistance(word1,word2)
print(minNoOfOperations)

#time complexity = O(m*n) (m is length of word1 & n is length of word 2)
#space complexity = O(m*n) (m is length of word1 & n is length of word 2)