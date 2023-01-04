class Solution(object):
    def rearrangeSticks(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        #eg: n=3, k=2 -------- [1,2,3]
        dp = {}  #using hashmap as cache

        #recursive function
        def DFS(N,K):
            #base cases
            if(N == K):
                return 1
            if(N==0 or K==0):
                return 0
            if(N,K) in dp:
                return dp[(N,K)]
                
            dp[(N,K)] = (DFS(N-1,K-1) + (N-1)*DFS(N-1,K))
            return dp[(N,K)]
        
        return DFS(n,k) % (10**9 + 7) #% (10**9 + 7) is added because the result could be a really large value
        
obj = Solution()
n,k = 3,2
noOfWaysToRearrangeCandles = obj.rearrangeSticks(n,k)
#result = 3 i.e. [1,3,2], [2,3,1], and [2,1,3]
print(noOfWaysToRearrangeCandles)
