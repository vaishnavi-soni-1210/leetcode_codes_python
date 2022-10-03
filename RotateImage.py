class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        left,right = 0, len(matrix)-1    #bcz no of rows = columns else len(matrix[0]) would be the length of 1st row
        
        while left < right:    #base case
            for i in range(right-left):  #thats bcz last cell will already be replaced in each row/column
                top,bottom = left,right

                #i pointer is used to switch to the next rotation here

                #save top-left in temp
                tempTopLeft = matrix[top][left + i]

                #rotate in reverse, save bottom-left in top-left
                matrix[top][left + i] = matrix[bottom - i][left]

                #rotate in reverse, save bottom-right in bottom-left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                #rotate in reverse, save top-right in bottom-right
                matrix[bottom][right - i] = matrix[top + i][right]

                #rotate in reverse, save top-left(temp) in top-right
                matrix[top + i][right] = tempTopLeft

            left = left + 1    #after one complete layer, switch to the subproblem i.e. internal matrix
            right = right - 1  #after one complete layer, switch to the subproblem i.e. internal matrix

        return matrix

obj = Solution()
image2DMatrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotatedImage = obj.rotate(image2DMatrix)
print(rotatedImage)

#time complexity = O(n*n) = O(n^2)
#space complecity = O(1)