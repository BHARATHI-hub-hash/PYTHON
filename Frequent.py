#Input the string
string = input("Enter a String: ")

#Dictionary to store the character frequency
fre ={}

for char in string:
    if char in fre:
        fre[char] += 1
    else:
        fre[char] = 1
        most_freq = None
        max_count = 0
        for char, count in fre.items():
            if count > max_count:
                most_freq = char
                max_count = count
print("The most frequent character: ", most_freq)
