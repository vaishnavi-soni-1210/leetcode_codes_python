class Solution(object):
    #approach 1
    def getNewArrayWithProducts1(self,arrNum):
        arrProd = []
        prodOfAll = 1
        #find product
        for num in arrNum:
            prodOfAll = prodOfAll * num
        #create new array
        for i in range(0,len(arrNum)):
            arrProd.append(int(prodOfAll))
        #divide by 1st array
        for i in range(0,len(arrNum)):
            arrProd[i] = int(arrProd[i]/arrNum[i])
        return arrProd
    #approach 2
    def getNewArrayWithProducts2(self,arrNum):
        arrProd = []
        for i in range (0,len(arrNum)):
            prodOfAllExceptOne = 1
            for j in range(0,len(arrNum)):
                if(i == j):
                    continue
                else:
                    prodOfAllExceptOne = prodOfAllExceptOne * arrNum[j]
            arrProd.append(prodOfAllExceptOne)
        #outer loop completed
        return arrProd

obj = Solution()
arrNum = [1,2,3]
prodOfAllExceptCurrentIndex = obj.getNewArrayWithProducts1(arrNum)
print("Solution by Approach 1: ")
print((prodOfAllExceptCurrentIndex))
prodOfAllExceptCurrentIndex = obj.getNewArrayWithProducts2(arrNum)
print("Solution by Approach 2: ")
print((prodOfAllExceptCurrentIndex))
