def remove_vowels(string): #defining a remove_vowels function
    vowels = "aeiouAEIOU" #assigning the vowels value
    # "char for char in string" - loops each character in input string and If condition checks if the charcter is not a vowel
    result = ''.join([char for char in string if char not in vowels])
    return result
string = input("Enter a String: ")
output_string = remove_vowels(string)
print("String without vowels:", output_string)