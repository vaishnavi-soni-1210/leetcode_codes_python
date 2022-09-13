class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sumOfBinary = ""

        if(a == b == "0"): #special case/ corner case
            return "0"

        #get the length of smaller string
        lengthOfSmallerString = 0
        if (len(a) > len(b)): 
            lengthOfSmallerString = len(b) 
        else:
            lengthOfSmallerString = len(a) #even if equal
        #print(lengthOfSmallerString)
            
        #reverse the string a
        revStrA = ""
        for ch in range(len(a)-1,-1,-1): #loop in reverse
            #print(sumString[ch])
            revStrA = revStrA + a[ch]
        #print(revStrA)

        #reverse the string b
        revStrB = ""
        for ch in range(len(b)-1,-1,-1): #loop in reverse
            #print(sumString[ch])
            revStrB = revStrB + b[ch]
        #print(revStrB)
        strSum = ""

        #loop till lengthOfSmallerString times 
        sumOfTwo = 0
        carryForward = 0
        for i in range(0,lengthOfSmallerString):
            sumOfTwo = carryForward + int(revStrA[i]) + int(revStrB[i])
            if(sumOfTwo == 2):
                sumOfTwo = 0
                carryForward = 1
            elif(sumOfTwo == 1):
                sumOfTwo = 1 
                carryForward = 0 
            elif(sumOfTwo == 0):
                sumOfTwo = 0
                carryForward = 0
            else: #eg: sumOfTwo = 3
                sumOfTwo = 1 
                carryForward = 1  
            strSum = strSum + str(sumOfTwo)
            #print(strSum)

        #after loop continue for remanning digits of bigger string or if both strings are equal in length
        if(len(a) == len(b) and carryForward == 1):
            #print('if condition')
            strSum = strSum + str(carryForward) 
            carryForward = 0 #set carryforward = 0 so that it should not enter last if block
        elif(len(a) > len(b)):
            #lengthRemaining = len(a) - lengthOfSmallerString
            for i in range(lengthOfSmallerString, len(a)):
                sumOfTwo = carryForward + int(revStrA[i])
                #print('lengthOfSmallerString %d' %lengthOfSmallerString)
                #print(carryForward)
                if(sumOfTwo == 2):
                    sumOfTwo = 0
                    carryForward = 1
                elif(sumOfTwo == 1):
                    sumOfTwo = 1 
                    carryForward = 0 
                elif(sumOfTwo == 0):
                    sumOfTwo = 0
                    carryForward = 0
                else: #eg: sumOfTwo = 3
                    sumOfTwo = 1 
                    carryForward = 1            
                strSum = strSum + str(sumOfTwo)
        elif(len(b) > len(a)):
            for i in range(lengthOfSmallerString, len(b)):
                sumOfTwo = carryForward + int(revStrB[i])
                if(sumOfTwo == 2):
                    sumOfTwo = 0
                    carryForward = 1
                elif(sumOfTwo == 1):
                    sumOfTwo = 1 
                    carryForward = 0 
                elif(sumOfTwo == 0):
                    sumOfTwo = 0
                    carryForward = 0
                else: #eg: sumOfTwo = 3
                    sumOfTwo = 1 
                    carryForward = 1  
                strSum = strSum + str(sumOfTwo)
        
        #if carryForward is still 1 at last
        if(carryForward == 1):
            #print('if carryForward is still 1 at last')
            strSum = strSum + str(carryForward)

        #for final result reverse the strSum also
        for i in range(len(strSum)-1, -1,-1):
            sumOfBinary = sumOfBinary + strSum[i]
        return sumOfBinary

obj = Solution()
#a = "11"
#b = "1"
#a = "1010"
#b = "1011"
#a = "1111"
#b = "1111"
a = "100"
b = "110010"
sum = obj.addBinary(a,b)
print(sum)