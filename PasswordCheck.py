password = input("Enter eight digit password: ")
print(password)
print("Checking if password is valid or not")
listOfAlphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
listOfNumbers = "1234567890"
noOfConsecutiveAlphabets = 0
noOfConsecutiveDigits = 0
isPasswordStrong = True

for val in password:
    if listOfAlphabets.find(val) > -1:                #if alphabet
        noOfConsecutiveAlphabets = noOfConsecutiveAlphabets + 1
        noOfConsecutiveDigits = 0
    elif listOfNumbers.find(val) > -1:                #if digit
        noOfConsecutiveDigits = noOfConsecutiveAlphabets + 1
        noOfConsecutiveAlphabets = 0
    else:                                       #if special symbol
        noOfConsecutiveAlphabets = 0
        noOfConsecutiveDigits = 0

    #another if-else block to check if no of consecutive alphabets or digits raised to 3 
    if noOfConsecutiveAlphabets >=3 | noOfConsecutiveDigits >=3:
        isPasswordStrong = False
        break
if isPasswordStrong == True:
    print('Entered password is Strong')
else:
    print('Entered password is Weak')