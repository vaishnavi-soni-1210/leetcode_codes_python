class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        #recursion - top down
        #dynamic programming - bottomup
        Rows, Cols = len(matrix), len(matrix[0])
        cache = {}  #DS = hashmap to store for each (r,c) -> MaxLength of the square

        def helper(r,c):
            #out of bounds
            if r >= Rows or c >= Cols:
                return 0

            #if already in cache
            if(r,c) in cache:
                return cache[(r,c)]

            #if not in cache, then calculate down, right & bottom
            down = helper(r+1,c)
            right = helper(r,c+1)
            diagonal = helper(r+1,c+1)

            cache[(r,c)] = 0   #if in case there is 0 in that position already
            if(matrix[r][c] == "1"):
                cache[(r,c)] = 1 + min(down,right,diagonal)  #if its a 0 then 0,if its a 1 then 1 & so on

            return cache[(r,c)]

        #calling the helper function
        helper(0,0)   #with recursion going top to bottom

        #atlast the cache will have list of all possible LENGTHS of squares
        maxLength = max(cache.values())
        resultArea = maxLength **2

        return resultArea

obj = Solution()
matrix = [["1","0","1","1"],["1","1","0","1"],["1","1","1","1"]]
result = obj.maximalSquare(matrix)
print(result)

#time complexity = space complexity = O(m*n)
#this is the recursive approach.
#to use dynamic programming memoization, use nested for loops