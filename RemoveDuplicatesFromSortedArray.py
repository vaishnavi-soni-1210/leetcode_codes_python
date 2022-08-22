class Solution(object):
    def rotate(self,l, n):
        newList = l[n:] + l[:n]
        return newList
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numOfDuplicates = 0
        
        i = 0
        while (i < len(nums)-1):
            if(nums[i] == nums[i+1]):
                allNextValuesAreSame = True
                numOfDuplicatesForEach = 0  
                #check if all values in list are duplicates
                for m in range(i+1,len(nums)):
                    if(nums[m] == nums[i]):
                        numOfDuplicatesForEach = numOfDuplicatesForEach+1
                    else: #(nums[m] != nums[i]):
                        allNextValuesAreSame = False
                        break
                if(allNextValuesAreSame == True):
                    numOfDuplicates = len(nums) - (i+1)
                    break
                else: #if not all values are duplicate, and 1 value is duplicated 'numOfDuplicatesForEach' times                    numOfDuplicatesForEach = 0   
                    #rotate the list such that all duplicates of a particular number appends to the end, in one go
                    #start from (i+1) till end of list
                    slicedList = nums[i+1:]
                    rotatedSlicedList = self.rotate(slicedList,numOfDuplicatesForEach)
                    # print("rotatedList")
                    # print(rotatedSlicedList)
                    #use loop to relace the last (i+1 to len(num)-1 instances of the nums list with rotatedSlicedList)
                    nums[i+1 : ] = rotatedSlicedList  
                    # print("nums after rotate")
                    # print(nums)
                    numOfDuplicates = numOfDuplicates + numOfDuplicatesForEach    
                  
            else:   #proceed to check next if not duplicate
                i = i+1
            #list is in ascending order, so check if all elements are already checked
            if((i+1 < len(nums)) and (nums[i] > nums[i+1])):  
                break  
        print("number of duplicates: %d"%(numOfDuplicates))
        k = len(nums)-numOfDuplicates
        return k
obj = Solution()
nums = [-4,-4,-3,-3,-2,-2,-1,-1,0,0,1,1,2,2,3,3,4,4]
k = obj.removeDuplicates(nums)
print("Number of non duplicate values: %d" %(k))
print(nums)
for val in range (0,k):
    print(nums[val])