#Assingning values to Strings

string1 = input("Enter the first String: ")
string2 = input("Enter the second String: ")
longest= ""

for i in range(len(string1)): #start of the substring
    for j in range(i+1, len(string1)+1): #end of the substring
        substring = string1[i:j]  #extract a substring from string1
        if substring in string2 and len(substring) > len(longest): #Check the previous substring
            longest = substring
            if longest:
                print("Longest: ", longest)
            else:
                print("None")






