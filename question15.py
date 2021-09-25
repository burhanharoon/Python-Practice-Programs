import re
password = input("Please enter your password: ")
loop = True
while loop:
    if (len(password) < 6 or len(password) > 12):
        break
    elif not re.search("[a-z]", password):
        break
    elif not re.search("[0-9]", password):
        break
    elif not re.search("[A-Z]", password):
        break
    elif not re.search("[$#@]", password):
        break
    elif re.search("\s", password):
        break
    else:
        print("Valid Password")
        loop = False
        break

if loop:
    print("Not a Valid Password")
