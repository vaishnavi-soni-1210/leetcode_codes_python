from re import L


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if(len(s1)+len(s2) != len(s3)):
            return False         #s3 should be sum of characters in s1 & s2
        
        #use a 2D array for s1 & s2 & set all to false
        dp = [[False] * (len(s2)+1) for i in range(len(s1)+1)]
        dp[len(s1)][len(s2)] = True    #base case i.e. out of bounds of both s1 & s2 position will be true

        for i in range(len(s1),-1,-1):   #start from len(s1), because it will be null & we need to check only s2 last char
            for j in range(len(s2),-1,-1): #start from len(s2) because it will be null & we need to check only s1 last char
                if(i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]):
                    dp[i][j] = True
                #meaning: i is still inbound, character at s1[i] is same as on required on s3
                #also, next character in s1 i.e. i+1, & s2[j] is also true
                if(j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]):
                    dp[i][j] = True
                #same as above for s2[j]

                #if above both conditions are not true then we need to return false, 
                #but we already initialized or dp[][] to false so no need to return false
        #print(dp)
        return dp[0][0] 
        
obj = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
isInterleavingString = obj.isInterleave(s1,s2,s3)
print(isInterleavingString)

#time complexity = O(n*m)
#space complexity = O(n*m)