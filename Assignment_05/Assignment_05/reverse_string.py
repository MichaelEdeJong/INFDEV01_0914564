input = raw_input("Type a string: ")

#print(input[::-1])

output = "";
for char in reversed(input):
    output += char
print(output)