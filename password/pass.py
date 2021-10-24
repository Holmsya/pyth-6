userPass = ''
while len(userPass) > 8:
    userPass = input("Input password: ")
    if len(userPass) <= 8:
        print("Password must be 8 lenght")

repeatPass = input("Repeat the password: ")
if userPass == repeatPass:
    print("Congratulations, you won!")
else:
    print("Error")
