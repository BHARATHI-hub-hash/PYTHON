# defining a "count_unique_characters" function
def count_unique_characters(string):
    #assigning string to varaible
    unique_values = set(string)
    #returning a length of unique characters
    return len(unique_values)
#output
string = input("Enter a string: ")
unique_value_count = count_unique_characters(string)
print("Total number of unique characters:", unique_value_count)