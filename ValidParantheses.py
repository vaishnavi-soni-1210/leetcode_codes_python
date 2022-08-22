class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arrRemainingParantheses = []
        latestOpeneningParantheses = ""
        
        for i in range (0, len(s)):
            #check if there are only closing parantheses in the string or the string has closing paranthesis first & then others
            if(latestOpeneningParantheses == "" and (s[i] == ')' or s[i] == '}' or s[i] == ']' or s[i] == '>')):
                if (s[i] == '>' and (i+1 <len(s)) and s[i+1] == "="):  #check if its closing bracket or greater than sign from >=
                    #its a >= sign
                    continue #ignore
                else:
                    #its a closing parantheses
                    arrRemainingParantheses.append(s[i])
                    break   #string is already invalid
            #check if there is already some opening parantheses found & after that wrong closing parantheses appears in sequence
            if(latestOpeneningParantheses == "(" and (s[i] == ">" or s[i] == "}" or s[i] == "]")):
                break   #string is invalid as sequence is wrong
            if(latestOpeneningParantheses == "{" and (s[i] == ">" or s[i] == ")" or s[i] == "]")):
                break   #string is invalid as sequence is wrong
            if(latestOpeneningParantheses == "[" and (s[i] == ">" or s[i] == "}" or s[i] == ")")):
                break   #string is invalid as sequence is wrong
            if(latestOpeneningParantheses == "<"  and not((i+1 <len(s)) and s[i+1] == "=") and (s[i] == ")" or s[i] == "}" or s[i] == "]")):
                break   #string is invalid as sequence is wrong

            if(s[i] == '(' or s[i] == '{' or s[i] == '[' or s[i] == '<'):
                if not(s[i] == '<' and (i+1 <len(s)) and s[i+1] == "="):  #check if its an opening bracket or less than sign from <=
                    latestOpeneningParantheses = s[i]
                    arrRemainingParantheses.append(s[i])
            if(latestOpeneningParantheses == "(" and s[i] == ")"):
                arrRemainingParantheses.pop()
                if(len(arrRemainingParantheses) > 0):
                    latestOpeneningParantheses = arrRemainingParantheses[len(arrRemainingParantheses)-1]
                else:
                    latestOpeneningParantheses = ""
            if(latestOpeneningParantheses == "{" and s[i] == "}"):
                arrRemainingParantheses.pop()
                if(len(arrRemainingParantheses) > 0):
                    latestOpeneningParantheses = arrRemainingParantheses[len(arrRemainingParantheses)-1]
                else:
                    latestOpeneningParantheses = ""
            if(latestOpeneningParantheses == "[" and s[i] == "]"):
                arrRemainingParantheses.pop()
                if(len(arrRemainingParantheses) > 0):
                    latestOpeneningParantheses = arrRemainingParantheses[len(arrRemainingParantheses)-1]
                else:
                    latestOpeneningParantheses = ""                    
            if(latestOpeneningParantheses == "<" and s[i] == ">"):
                arrRemainingParantheses.pop()
                if(len(arrRemainingParantheses) > 0):
                    latestOpeneningParantheses = arrRemainingParantheses[len(arrRemainingParantheses)-1]
                else:
                    latestOpeneningParantheses = ""
        if(len(arrRemainingParantheses) > 0):
            print(arrRemainingParantheses)
            return False
        else:
            print(arrRemainingParantheses)
            return True

obj = Solution()
s = "[([]])"
isValidString = obj.isValid(s)
print(isValidString)