#password checker

def passwcheck():
    password = str(input("enter a password: "))

    if len(password) < 8:
        print("Password is too short")
    elif not any(char.isdigit() for char in password):
        print("Password must contain a number")
    elif not any(char.isupper() for char in password):
        print("Password must contain an uppercase letter")
    elif not any(char.islower() for char in password):
        print("Password must contain a lowercase letter")
    else:
        print("Password is valid")


print("password checker, please follow the instructions:\n- at least 8 characters\n- at least one number\n- at least one uppercase letter\n- at least one lowercase letter")

passwcheck()