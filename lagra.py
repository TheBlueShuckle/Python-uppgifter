users = {
    "Foo" : "Bar"
}

def check_login(username, password):
    if(len(users) == 0):
        return False

    if (users.get(username) == password):
        return True
    
    return False


# test - delete later
username = input("Input Username: ")
password = input("Input Password: ")

if (check_login(username, password)):
    print("Logging in")

else:
    print("Incorrect username or password")