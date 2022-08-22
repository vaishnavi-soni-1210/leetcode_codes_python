#print squares of numbers using for loop
#in range, first parameter says the start index/value, second says the end index(always as i-1), third says the increment

for i in range(1,11):
    print(i*i)
print('-'*50)

for i in range(11):
    print(i*i)
print('-'*50)

for i in range(1,11,2):
    print(i*i)
print('-'*50)

listOfNames = ['Vaishnavi','Jahnavi','Yash','Bobby']
listOfNamesInTuple = ('Vaishnavi','Jahnavi','Yash','Bobby')
for nm in listOfNames:
    print(nm)
print('-'*50)

for nm in listOfNamesInTuple:
    print(nm)
print('-'*50)

flag = 1
while(flag != -1):
    name = input('Enter name: ')
    flag = int(input('Hi %s, Enter -1 to stop and 1 to continue ' %name))
    



