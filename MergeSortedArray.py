class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        #get last index if num1 i.e. (m+n-1)
        last = m+n-1
        
        #loop while there are elements present in both arrays
        while(m > 0 and n > 0):
            if(nums1[m-1] >= nums2[n-1]):  #-1 because indexes start from 0
                nums1[last] = nums1[m-1]
                m=m-1
            else:
                nums1[last] = nums2[n-1]
                n=n-1
            last = last-1

        #if there are any more elements left in nums1 then they are already in sorted order after merge
        #but if there are more elements left in nums 2 after merge, then move them in rev seq in nums1
        #that will only happen there are smaller elements in nums2 than the 0th element of nums1

        #fill nums1 with all remaining elements in nums2
        while(n > 0):
            nums1[last] = nums2[n-1]
            last, n = last-1, n-1

        print(nums1)

obj = Solution()
nums1 = [3,5,7,9,11,0,0,0,0,0,0,0]
nums2 = [1,2,3,4,5,10,21]
m = 5
n = 7
obj.merge(nums1,m,nums2,n)