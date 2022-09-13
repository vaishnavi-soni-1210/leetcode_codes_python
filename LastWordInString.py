class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lengthOfLastWordInString = 0
        listOfAlphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(0,len(s)):           
            #check if space occurs
            if s[i] == ' ':
                if(i == len(s)-1): #last character is space
                    #do nothing & keep the length as it is
                    break
                elif(i != len(s)-1): #not the last character
                    #do nothing
                    for j in range(i+1,len(s)): #check all remaining characters if there is anything else but space
                        if(s[j] != ' '):
                            lengthOfLastWordInString = 0 #set length to 0 as there is another word present in string
                            break
            else:
                lengthOfLastWordInString = lengthOfLastWordInString + 1
        return lengthOfLastWordInString

obj = Solution()
#s = "I can do this"
s = "   fly me   to   the moon  "
lengthOfLastWordInString = obj.lengthOfLastWord(s)
print(lengthOfLastWordInString)