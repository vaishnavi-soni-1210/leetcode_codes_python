input_string1 = input('Enter elements of 1st list separated by space ')
print("\n")
user_list1 = input_string1.split()

input_string2 = input('Enter elements of 2nd list separated by space ')
print("\n")
user_list2 = input_string2.split()

list1_as_set = set(user_list1)
lstMix = []
union = list1_as_set.union(user_list2)
lstMix = list(union)

print("Common numbers: \n")
intersection = list1_as_set.intersection(user_list2)
intersectionOfLists = list(intersection)
print(intersectionOfLists)

print("Odd Numbers: \n")
for num in lstMix:      
    # checking condition for odd
    if int(num) % 2 != 0:
       print(num, end = " ")
print("\nEven Numbers: \n")
for num in lstMix:      
    # checking condition for odd
    if int(num) % 2 == 0:
       print(num, end = " ")