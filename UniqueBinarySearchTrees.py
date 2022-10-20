class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        #eg: numTrees[4] = numTrees[0]*numTrees[3]  #considering 1 as root
        #                  + numTrees[1]*numTrees[2]  #considering 2 as root
        #                  + numTrees[2]*numTrees[4]  #considering 3 as root
        #                  + numTrees[3]*numTrees[0]  #considering 4 as root
        # numTrees[4] = 14

        numTree = [1]*(n+1)   #initialize array till n+1 bcz result will be calculated at last

        #initializing with 1 bcz, for 0 nodes = 1 tree & 1 node4 = 1 tree, so we can start from 2
        for node in range(2,n+1):        #loop through all the nodes
            total = 0
            for root in range(1,node+1):   #consider every node as root node
                left = root-1   #current node-1
                right = node-root #total nodes-root
                total = total + numTree[left]*numTree[right]
            
            #take this total & store in cache i.e numTree array
            numTree[node] = total

        #result is in the end of numTree cache
        return numTree[n]

obj = Solution()
n = 4
numberOfPossibleBST = obj.numTrees(n)
print(numberOfPossibleBST)

# time complexity = O(n^2) 
# {bcz we are calculating for each number in n & iterate consider all other numbers each time}
# space complexity = O(n) 
# {bcz storing result of each subproblem}