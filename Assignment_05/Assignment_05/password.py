password = raw_input("Password strength check\nEnter your password: ")
strength = 0
characters = "!@#$%^&*()_+<>?,./-=[]{}\|"
numbers = "1234567890"
uppercase = "QWERTYUIOPASDFGHJKLZXCVNM"

if len(password) > 7:
    strength = strength + len(password) * 20

if any((key in uppercase) for key in password):
    strength = strength + 30

if any((key in characters) for key in password):
    strength = strength + 40

if any((key in numbers) for key in password):
    strength = strength + 30

if strength < 150: 
    print("Your password is weak.")
elif strength < 250:
    print("Your password is medium.")
elif strength < 400:
    print("Your password is strong.")
else:
    print("Your password is excellent!")
print(strength)