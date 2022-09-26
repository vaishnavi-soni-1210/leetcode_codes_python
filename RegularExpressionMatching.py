from math import fabs


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #top down memoization solution
        cache = {}   #memoization i.e. to avoid all repeated work

        def dfs(i,j):   #i is index in s & j is index in p
            if(i,j) in cache:
                return cache[(i,j)]
            #check edge cases or out of bounds conditions
            if(i >= len(s) and j >= len(p)):    #match
                return True
            if(j >= len(p)):    #j is out of bounds & i is not i.e s is longer than pattern
                return False
        
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if(j+1 < len(p) and p[j+1] == "*"): #1st char will never be a * so checking j+1
                cache[(i,j)] = dfs(i,j+2) or (match and dfs(i+1,j))                 
                #don't use the * or #use the * only if there is a match = true
                return cache[(i,j)]

            if(match):   #if there is no * then we only need to match the characters
                cache[(i,j)] = dfs(i+1,j+1)
                return cache[(i,j)]

            cache[(i,j)] = False  #if non of the condition is true, i.e. there is no * nd the chas doesn't match
            return cache[(i,j)]

        return dfs(0,0)  #start from beginning of both string and pattern

obj = Solution()
s="aa"
p="a*b*"
matching = obj.isMatch(s,p)
print(matching)