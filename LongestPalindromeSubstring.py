from cgitb import reset


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        palindromeString = ""
        resultLength = 0 

        for i in range(0,len(s)):
            #print(s[i])

            #condition for odd palindrome
            left,right = i,i
            while(left >= 0 and right < len(s) and s[left] == s[right]): #check equal condition at the end else error out of bound index
                if((right-left+1) > resultLength):
                    resultLength = right-left+1
                    palindromeString = s[left:right+1]
                left = left-1
                right = right+1

            #condition for even palindrome
            left,right = i,i+1
            while(left >= 0 and right < len(s) and s[left] == s[right]): #check equal condition at the end else error out of bound index
                if((right-left+1) > resultLength):
                    resultLength = right-left+1
                    palindromeString = s[left:right+1]
                left = left-1
                right = right+1
        
        print(resultLength)
        return palindromeString

obj = Solution()
s="babad"
result = obj.longestPalindrome(s)
print(result)

#space complexity = O(1) & time complexity = O(n^2)