import re


FIRSTNAME = input("First name : ")
LASTNAME = input("Last name : ")


while True:
    emailid = input("Email id : ")
    pat = "[^0-9]+[a-z0-9]+@[a-z]+\.[a-z]"
    if not re.match(pat, emailid):
        print("Invalid mail id")
    else:
        break

while True:
    password = input("Enter a password : ")
    if len(password) < 5 and len(password) > 16:
        print("Password must be at least 6 characters to 16 characters")
        continue
    elif not re.search("[A-Z]", password):
        print("Password should contain one upper character")
        continue
    elif not re.search("[a-z]", password):
        print("Password should contain one lower character")
        continue
    elif not re.search("[0-9]", password):
        print("Password should contain one digit")
        continue
    elif not re.search("[~!@#$%^&*]", password):
        print("Password should contain one special character")
        continue
    elif re.search("[\s]", password):
        print("Password should not contain any spaces")
        continue
    else:
        break
while True:
    d = input("Confirm password : ")
    if password != d:
        print("Password doesn't match")
    else:
        break


def register():
    db = open("database.txt", "r")
    db1 = open("database.txt","a")
    db1.write("First name : "+FIRSTNAME+"\n")
    db1.write("Last name : "+LASTNAME+"\n")
    db1.write("Email id : "+emailid+"\n")
    db1.write("Password : "+password+"\n")

register()


