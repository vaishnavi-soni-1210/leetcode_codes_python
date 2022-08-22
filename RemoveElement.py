class Solution(object):
    def rotateListToRightByK(self,nums,k):
        rotatedNums = nums[k:] + nums[:k]
        return rotatedNums
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #first converting list into sorted order
        nums.sort()
        #loop through the list & append any appearance of val to the end
        i = 0
        numOfAppearances = 0
        while(i < len(nums)):
            #list is in ascending order, so check if all elements are already checked
            if(nums[i] > val):  
                break
            if(nums[i] == val):
                numOfAppearances = numOfAppearances + 1
                allNextNumbersAreSame = True
                for j in range (i+1,len(nums)):
                    if(nums[j] != val):
                        allNextNumbersAreSame = False
                        break
                    else:
                        numOfAppearances = numOfAppearances + 1
                #print(allNextNumbersAreSame)
                #print(numOfAppearances)
                if(allNextNumbersAreSame == True):
                    #print("allNextNumbersAreSame == True")
                    #print(numOfAppearances)
                    break
                else: #all next numbers are not same
                    #take sliced list starting from ith index
                    slicedList = nums[i:]                
                    #rotate to shift it to the end
                    rotatedNums = self.rotateListToRightByK(slicedList,numOfAppearances)
                    #not doing increment to i in this case, if the next number is also same   
                    nums[i:] = rotatedNums
            else:
               i = i + 1
        return len(nums) - numOfAppearances
        
obj = Solution()
#nums = [2,3,3,5,7,4,3,6,2,3]
nums = [0,1,2,2,3,0,4,2]
#nums = [3,2,2,3]
#print(nums)
val = 2
nonRepeatedNums = obj.removeElement(nums,val)
#print(nums)
#print(numOfAppearances)
newList = nums[0:nonRepeatedNums]
print(newList)