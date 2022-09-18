class Solution(object):
    
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if(len(s) == 0 or s[0] == "0"):
            return 0
        
        if(len(s) == 1):
            return 1

        resultDictionary = { len(s) : 1}

        # #if first character is 0
        # #if there is a 0 before a digit, then invalid
        # if(s[0] == "0"):
        #     return 0

        # #if there is only 1 character in string
        # if(len(s) == 1 and s[0] != "0"):
        #     return 1       

        for i in range (len(s)-1, -1, -1):  
            #if there is a 0 before a digit, then invalid
            if(s[i] == "0"):
                resultDictionary[i] = 0
            else:
                resultDictionary[i] = resultDictionary[i+1] #if considering single digit at a time

            #condition to check if 2 digit number exists i.e between 10 to 26
            if(i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
                resultDictionary[i] = resultDictionary[i] + resultDictionary[i+2]

        #when we exit the loop, the 0th index in dictionary will have sum of all subproblems
        return resultDictionary[0]
            
obj = Solution()
s = "10"
result = obj.numDecodings(s)
print(result)
