#Defining a function
def are_anagrams(str1, str2):
    #Sort both strings and check if they are same
    return sorted(str1) == sorted(str2)
#Getting input for both string
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if are_anagrams(str1,str2):
    print("True")
else:
    print("False")
