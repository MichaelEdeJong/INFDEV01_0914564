string = raw_input("Cryptography\nEnter a string: ")
shift = raw_input("Enter a number: ")
unicode = []
result = "";

for char in string:
    if ord(char) + int(shift) in range (65, 124):
        unicode.append( ord(char) + int(shift) )
    else:
        unicode.append(ord(char))

for i in unicode:
   result += chr(i)

print(result)
