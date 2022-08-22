listOfNames = ['Vaishnavi','Jahnavi','Yash','Bobby'] #mutable #ordered #mixed
tupleOfNames = ('Vaishnavi','Jahnavi','Yash','Bobby') #immutable #ordered #mixed
setOfNames = {'Vaishnavi','Jahnavi','Yash','Bobby','Vaishnavi',500} #mutable #on-ordered #mixed

for nm in listOfNames:
    print(nm)
print('-'*50)

for nm in tupleOfNames:
    print(nm)
print('-'*50)

for nm in setOfNames:
    print(nm)
print('-'*50)