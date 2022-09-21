class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #eg: m = 3, n = 7

        #initialize last row
        row = [1] * n #with n number of columns
        #print(row)

        for i in range(m-1):  #2 times for each row
            #print(i)
            newRow = [1]*n #initialixe new row with 1, this '1' will overright
            for j in range(n-2,-1,-1):   #column/cell
                # using -2, to avoid overflow as there is no right from last column & no down from last row
                newRow[j] = newRow[j+1] + row[j]  #sum of right + bottom
            row = newRow
        
        return row[0]  #returning 0th column from last generated row i.e. 0th row        


obj = Solution()
m , n = 3, 7 #3 rows and 7 columns
result = obj.uniquePaths(3,7)
print(result)

#time complexity = O(m*n)