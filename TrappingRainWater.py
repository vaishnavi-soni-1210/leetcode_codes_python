class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #edge case
        if not height: return 0    #if input is empty

        l,r = 0, len(height)-1
        leftMax,rightMax = height[l],height[r]
        result = 0

        while(l<r):    #before l++ & r-- meet each other
            if(leftMax <= rightMax):     #if leftMax is smaller then shift left pointer
                l=l+1
                leftMax = max(leftMax,height[l])
                result = result + (leftMax - height[l]) #leftMax - height[l] is never gonna be -ve 
                #bcz we calculated max if leftMax already in above line
            else:
                r=r-1
                rightMax = max(rightMax,height[r])
                result = result + (rightMax - height[r]) #same way rightMax is never gonna be -ve 

        return result

obj = Solution()
height = [4,2,0,3,2,5]
maxUnitsOfWaterTrapped = obj.trap(height)
print(maxUnitsOfWaterTrapped)

#time complexity = O(n)
#space complexity = O(1)