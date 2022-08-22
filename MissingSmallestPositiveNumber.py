class Solution(object):
    def missingPositiveNumber(self,numArr):
        missingNumber = 1

        #first sort the array in ascending order, so that we can get the missing number in least time
        for i in range (0, len(numArr)): 
            for j in range (i+1, len(numArr)):
                if(numArr[j] < numArr[i]):
                    #swap the smaller number with previous
                    smallest = numArr[j]
                    numArr[j] = numArr[i]
                    numArr[i] = smallest 
        #sorted array is numArr
        # print(numArr)

        #find smallest positive number
        lastPositiveNum = 0
        for i in range(0, len(numArr)):
            if(lastPositiveNum == 0 and numArr[i] > 0):
                lastPositiveNum = numArr[i]
            elif (lastPositiveNum > 0):   #after finding the smallest positive number
                #check if all next numbers are in sequence
                if not(numArr[i] == lastPositiveNum + 1):
                    missingNumber = lastPositiveNum + 1   #if sequqnce breaks
                    break
                else:
                    lastPositiveNum = numArr[i]  #if sequqnce doesnt break
            
        if(lastPositiveNum > 0): #there is/are positive number(s) present in the array & sequence is maintained till end
            missingNumber = lastPositiveNum + 1
        else:
            missingNumber = 1
        return missingNumber

obj = Solution()
#missingNumber = obj.missingPositiveNumber([8,4,6,2,1,3,7])
missingNumber = obj.missingPositiveNumber([8,-1,0,2,1,3,7])
#missingNumber = obj.missingPositiveNumber([-1,3,0,4,1,2,5])
print("Missing smallest positive number is %d" %(missingNumber))