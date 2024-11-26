#Defining a function
def count_words(text):
    #spliting the string into words using spaces and count the no of words
    words = text.split()
    return len(words)

text = input("Enter a stirng: ")
print("Number of words:", count_words(text))
