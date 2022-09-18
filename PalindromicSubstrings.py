class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(0,len(s)):
            #for odd palindrome strings
            left = right = i
            while(left >=0 and right < len(s) and s[left] == s[right]):
                result = result+1 #increament every time because each substring including single characters can also be palindromes
                
                #we can also check length of this substring/palindrome = (right - left + 1)
                #we can also print each substring using s[left:right+1] BUT BEFORE INCRE/DECRE
                #print(s[left:right+1])

                left = left-1
                right = right+1
                            
            #for even palindrome strings
            left = i
            right = i + 1
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                result = result+1
                #print(s[left:right+1])
                left = left-1
                right = right+1

        return result

    def countPalindromeCommon(self,left,right,s):
        result = 0
        while(left >=0 and right < len(s) and s[left] == s[right]):
                result = result+1 #increament every time because each substring including single characters can also be palindromes
                #print(s[left:right+1])
                left = left-1
                right = right+1
        return result

    def countSubstringsOptimized(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(0,len(s)):
            #for odd palindrome strings
            result = result + self.countPalindromeCommon(i,i,s)
                            
            #for even palindrome strings
            result = result + self.countPalindromeCommon(i,i+1,s)

        return result

obj = Solution()
s = "baaab"
#result = obj.countSubstrings(s)
result = obj.countSubstringsOptimized(s)
print(result)

#space complexity = O(1) & time complexity = O(n^2)
#other optimization: put all the repeated code i.e. while loops in a seperate function 
# and return result from it, pass left right & s parameters to it
