class Solution():
    def rotate(self,l, n):
        newList = l[n:] + l[:n]
        return newList
    def slicedList(self,l, n):
        newList = l[2:]
        return newList


obj = Solution()
l = [1,2,3,4,5,6,7,8,9]
newList1 = obj.rotate(l,1)
print(newList1)
newList2 = obj.slicedList(l,1)
print(newList2)

# obj = Solution()
# l = [1,2,3,4,5,6,7,8,9]
# newList = obj.rotate(l,1)
# print(newList)
# #[2, 3, 4, 1]
# newList = obj.rotate(l,2)
# print(newList)
# #[3, 4, 1, 2]
# newList = obj.rotate(l,0)
# print(newList)
# #[1, 2, 3, 4]
# newList = obj.rotate(l,-1)
# print(newList)
# #[4, 1, 2, 3]