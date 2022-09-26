class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        cache = {}  #using hashmap

        def dfs(i,j):  #i is index in s and j is index in t
            #cover edge cases
            if(j == len(t)):   #if t is ""
                return 1
            if(i == len(s)):   #if s is ""
                return 0
            if (i,j) in cache:  #if result is already cached
                return cache[(i,j)]
            
            if(s[i] == t[j]):   #if character matches consider 2 cases i.e. increment both i,j and only i
                cache[(i,j)] = dfs(i+1,j+1) + dfs(i+1,j)
            else:   #if characters doesn't match, increment only i & not j
                cache[(i,j)] = dfs(i+1,j)

            return cache[(i,j)]

        return dfs(0,0)   #start from beginning of both strings

obj = Solution()
s = "rabbbit"
t = "rabbit"
noOfDistSubsequences = obj.numDistinct(s,t)
print(noOfDistSubsequences)