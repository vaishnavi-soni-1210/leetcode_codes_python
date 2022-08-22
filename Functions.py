def showMessage():
    print('Hello World!')
    print('-'*50)

def showMessageWithName(nm):
    print('Hello %s, Welcome to the real world! It sucks,, you are gonna love it!' %nm)
    print('-'*50)

def calculateSum(a,b):
    c=a+b
    print('Sum is ', c)
    print('-'*50)

def calculateSquare(num):
    sq = num*num
    return sq

def printTupleValues(*tup):
    print(type(tup))
    for nm in tup:
        print(nm)
    print('-'*50)
    
showMessage()
showMessageWithName('Rachel')
calculateSum(10,20)
calculateSum(100.22,200.44)
calculateSum('Vaishnavi ', 'Soni')
calculateSum(['Yash', 'Bobby'], ['Nain', 'Jahnavi'])
#number = int(input('Enter a number: '))
#square = calculateSquare(number)
square = calculateSquare(50)
print('Square of number is ', square)
print('-'*50)
printTupleValues('Vaishnavi',50000,True,7.7777,['Friends','Tripling'])
