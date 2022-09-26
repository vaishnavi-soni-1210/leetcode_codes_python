class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        #define a 2d grid/matrix in python VERY IMP
        #2d matrix of size i+1,j+1 initialized with 0 at every position
        DP = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]   #plus 1 for out of bounds
        #print(DP)
        
        for i in range(len(text1)-1,-1,-1):   #bottom up - starting from last
            for j in range(len(text2)-1,-1,-1):   #bottom up - starting from last
                if(text1[i] == text2[j]):               #either characters match
                    DP[i][j] = 1 + DP[i+1][j+1]             #1 + diagonal value
                else:                                       #or they don't match
                    DP[i][j] = max(DP[i][j+1], DP[i+1][j])  #0 + max(right, bottom value)

        return DP[0][0]

obj = Solution()
text1 = "abcde"
text2 = "ace"
lenOfLongestCommonSubSeq = obj.longestCommonSubsequence(text1,text2)
print(lenOfLongestCommonSubSeq)

#time complexity = O(m*n)
#space complexity = O(m*n) because calculating each each cell 
#SIMILAR PROBLEM: EditDistance