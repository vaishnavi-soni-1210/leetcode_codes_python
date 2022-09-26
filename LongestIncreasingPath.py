class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows,columns = len(matrix), len(matrix[0])
        dp = {} #cache -> HASH MAP in this case with (row,col) = largest increating path from that index

        def dfs(r,c,prevVal):

            #check out of bounds condition for left/right/up/down & also if its not increasing order
            if(r < 0 or r == rows or c < 0 or c == columns or matrix[r][c] <= prevVal):
                return 0

            #if we already calculated result of this r,c & is present in our hash map
            if(r,c) in dp:
                return dp[(r,c)]

            #actual calculation for & find the max of (up,down,left,right results)
            #prev value everytime will be matrix[r][c]
            res = 1 
            res = max(res, 1 + dfs(r+1,c,matrix[r][c]))
            res = max(res, 1 + dfs(r-1,c,matrix[r][c]))
            res = max(res, 1 + dfs(r,c+1,matrix[r][c]))
            res = max(res, 1 + dfs(r,c-1,matrix[r][c]))
            dp[(r,c)] = res
            return res        #return result because this method is called consecutively

        #loop through the matrix & calculate res or dp[(r,c)]     
        for i in range(rows):
            for j in range(columns):
                dfs(i,j,-1)  
                #taking -1 as initial previous value because matrix can have 0 val too & in that case
                #the dfs will return 0, checking 1st if condition only, which is wrong

        #atlast - most imp is to return the max of values from hash map dp
        #print(dp)
        return max(dp.values())        
        
obj = Solution()
matrix = [[9,9,4],[6,6,8],[2,1,1]]
lenOfLongestIncreasingPath = obj.longestIncreasingPath(matrix)
print(lenOfLongestIncreasingPath)

#time complexity = space complexity = O(m*n)