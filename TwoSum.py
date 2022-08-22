#https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        resultIndices = []

        #write your logic here 
        for i in range (0,len(nums)-1):
            #print(nums[i])
            for j in range(i+1,len(nums)):
                #print("Sum of %d + %d = %d"%(nums[i],nums[j],nums[i] + nums[j]))
                sum = nums[i] + nums[j]
                if sum == target:
                    resultIndices.append(i)
                    resultIndices.append(j)
                    break       
            if len(resultIndices) > 0:
                break 
        return resultIndices

nums = list(map(int,(input('Enter elements of a list separated by space ').split())))
print(nums)
target = int(input("Enter target: "))
resultIndices = []

obj=Solution()
resultIndices = obj.twoSum(nums,target)

if(len(resultIndices) == 2):
    #print("true")
    print("The indices of two numbers such that the sum of two numbers is equal to given target are: %d, %d" %(resultIndices[0],resultIndices[1]))
else:
    #print("false")
    print("There are no such indices such that the sum of two numbers is equal to given target")
