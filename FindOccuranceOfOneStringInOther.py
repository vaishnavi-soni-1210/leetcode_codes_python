class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        found = -1
        #use python predefined method or define a custom logic
        for i in range(0,len(haystack)):
            if(haystack[i] == needle[0]): #if first index matches
                #check condition if remaining string in haystack is equal to needle
                if(len(needle) > len(haystack) - i):
                    #print('this is called')
                    found = -1
                    break
                found = i
                k = i
                for j in range(1,len(needle)):                    
                    k = k+1
                    #print(k,j)
                    if (haystack[k] != needle[j]):
                        #print(k,j)
                        #print('this is called')
                        found = -1
                        break
                if(found != -1):
                    break
        return found
        
obj = Solution()
#index = obj.strStr("Hello World","ll")
index = obj.strStr("mississippi","mississippi")
print(index)