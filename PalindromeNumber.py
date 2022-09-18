class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        strX = str(x)
        #print(len(strX))
        revStrX = ""
        for ch in range(len(strX)-1,-1,-1): #loop in reverse
            #print(strX[ch])
            revStrX = revStrX + strX[ch]

        #print(strX)
        #print(revStrX)
        if strX == revStrX:
            return True
        else:
            return False

obj = Solution()
result = obj.isPalindrome(121)
print(result)

#space & time complexity are O(n)
#instead we can exclude the space complexity by just using the same string 
# & using each character as middle character & comparing left & right sides, 
# like what is done in LongestPalindromeSubstring.py
