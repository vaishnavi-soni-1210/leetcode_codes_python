class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        strs = ['flower','flyer','flow','floor','flu']
        :rtype: str
        """
        totalStrings = len(strs) #5
        strLongestCommonPrefix = ""

        #find the length of smallest string
        smallestStringLength = len(strs[0])
        for i in range (1,len(strs)):
            if(len(strs[i]) < smallestStringLength):
                smallestStringLength = len(strs[i])
        #smallestStringLenth = 3

        i = 0
        while i < smallestStringLength:
            characterToCompare = strs[0][i]  #always get a character from 1st string
            ifCharacterMatches = True
            for j in range (1,totalStrings): #start comparing the character with 2nd string
                #print(strs[j][i] + characterToCompare)
                if(strs[j][i] != characterToCompare):
                    ifCharacterMatches = False
                    break
            if(ifCharacterMatches == True):
                #print(ifCharacterMatches)
                strLongestCommonPrefix = strLongestCommonPrefix + characterToCompare
                i = i+1
            else:
                break
        
        return strLongestCommonPrefix

obj = Solution()
strs = ['flower','flyer','flow','floor','flu']
strLongestCommonPrefix = obj.longestCommonPrefix(strs)
#print(strLongestCommonPrefix)
if(len(strLongestCommonPrefix) > 0):
    print("Longest common prefix is %s" %(strLongestCommonPrefix))
else:
    print("There is no common prefix among the input")