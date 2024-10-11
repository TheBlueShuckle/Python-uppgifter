import os

users = {
    "Foo" : "Bar",
    "FooBar" : "Baz" 
}

user_items = ["Pen", "Laptop", "Eraser"]

def save_user_info(username, user_items):
    path = 'usrs/' + username
    user_file = ""
    fileExists = os.path.exists(path)

    if (not fileExists):
        user_file = open(path, 'x')
        user_file.close()

    user_file = open(path, 'w')

    for item in user_items:
        user_file.write(item + "\n")


# def check_login(username, password):
#     if(len(users) == 0):
#         return False

#     if (users.get(username) == password):
#         return True
    
#     return False

# # test - delete later
# username = input("Input Username: ")
# password = input("Input Password: ")

# if (check_login(username, password)):
#     print("Logging in")

# else:
#     print("Incorrect username or password")

# save_user_info("Foo", user_items)
# save_user_info("FooBar", user_items)