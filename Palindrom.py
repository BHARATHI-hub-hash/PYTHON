def is_palindrome(input_string):
    return input_string == input_string[::-1]
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The String is Palindrom - True.")
else:
    print("The String is not a Palindrom - False.")