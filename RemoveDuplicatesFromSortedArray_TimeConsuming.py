class Solution(object):
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
                #check if all values in list are duplicates
                for m in range(i+1,len(nums)):
                    if(nums[m] != nums[i]):
                        allNextValuesAreSame = False
                        break
                if(allNextValuesAreSame == True):
                    numOfDuplicates = len(nums) - (i+1)
                    break
                else: #if not all values are duplicate, then check for each of them           
                    numOfDuplicates = numOfDuplicates+1
                    #if duplicate found, place it at the end
                    for j in range(i+1,len(nums)-1):
                        temp = nums[j]
                        nums[j] = nums[j+1]
                        nums[j+1] = temp 
                    #in in case loop goes till infinity
                    print("found")
                    print("i+1 = %d and len(nums)-1 = %d"%(i+1,len(nums)-1))
                    if(i+1 == len(nums)-1):
                        print("i+1 = %d and len(nums)-1 = %d"%(i+1,len(nums)-1))
                        break
            else:   #proceed to check next if not duplicate
                i = i+1
            #list is in ascending order, so check if all elements are already checked
            if((i+1 < len(nums)) and (nums[i] > nums[i+1])):  
                break  
        k = len(nums)-numOfDuplicates
        return k
obj = Solution()
nums = [1,1,2,3,4,4,4,5,5,6,6,6,7,7,7,7]
k = obj.removeDuplicates(nums)
print("Number of non duplicate values: %d" %(k))
for val in range (0,k):
    print(nums[val])

"""
This approach fails in Leetcode for one of the use cases where input list is very very large and there are more than 200 duplicates

-The time complexity in this code is very high because of loop in line 24
-this loop covers the whole list as many times as the duplicate number occurs
-solution is to count the number of duplicates for each list value at a time and rotate/reassign the list in one go for all duplicates
using python's approach to slice the list, and rotate the list by a number 'n'
See sample program to rotate a list in Basics
"""