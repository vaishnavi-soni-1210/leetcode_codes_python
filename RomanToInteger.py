class Solution(object):
    def romanToInt(self,roman):
        """
        roman = string
        """
        num = 0
        i = 0
        #for i in range(0,len(roman)):
        while(i < len(roman)):
            if(roman[i] == 'I'):                
                if(i+1 < len(roman)):  #check if the next character exists or the string already endeds
                    if(roman[i+1] == 'V'): #check if the number is 4 i.e. IV
                        num = num + 4
                        i = i+2            #skip 1 character
                        continue
                    elif(roman[i+1] == 'X'): #check if the number is 9 i.e. IX
                        num = num + 9
                        i = i+2             #skip 1 character
                        continue
                    else:                   #else I represents 1 & next character exists
                        num = num + 1
                else:                       #else I represents 1 & next character doesn't exists
                    num = num + 1
            if(roman[i] == 'V'):
                num = num + 5
            if(roman[i] == 'X'):
                if(i+1 < len(roman)):
                    if(roman[i+1] == 'L'): #40
                        num = num + 40
                        i = i+2
                        continue
                    elif(roman[i+1] == 'C'): #90
                        num = num + 90
                        i = i+2
                        continue
                    else:                  #10 & next character exists
                        num = num + 10
                else:                      #10 & next character doesn't exists
                    num = num + 10
            if(roman[i] == 'L'):
                num = num + 50
            if(roman[i] == 'C'):
                if(i+1 < len(roman)):
                    if(roman[i+1] == 'D'): #400
                        num = num + 400
                        i = i+2
                        continue
                    elif(roman[i+1] == 'M'): #900
                        num = num + 900
                        i = i+2  
                        continue
                    else:
                        num = num + 100     #100 & next character exists
                else:
                        num = num + 100     #100 & next character doesn't exists
            if(roman[i] == 'D'):
                num = num + 500
            if(roman[i] == 'M'):
                num = num + 1000
            i = i+1
            
        #end of loop
        return num
    #end of method
#end of class
obj = Solution()
#roman = (input("Enter roman number: ")).upper()
num = obj.romanToInt("CDXL")
print("Integer conversion of roman number is %d"%(num))
        
        