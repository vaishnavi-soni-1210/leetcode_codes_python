class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        DP = [False] * (len(s)+1) 
        DP[len(s)] = True  #BASE CASE: after completion of string it will be true
        #to DP array take length = len(s)+1, and assign each to false
        #eg: len(s) = 7, so DP = [False,False,False,False,False,False,False,True]
        
        #USING BOTTOM UP DP technique
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if(i+len(word) <= len(s) and s[i: i+len(word)] == word): #if s has enough characters to check
                    #first time for i = 4, then for i = 0 it will be called
                    DP[i] = DP[i+len(word)] #whole word is matched sp
                if(DP[i] == True):
                    break #need not to check for other words if one word matches
        
        return DP[0]

obj = Solution()
s = "neetcode" # s = "goodluck"
wordDict = ["neet", "leet", "code"]
result = obj.wordBreak(s,wordDict)
print(result)
