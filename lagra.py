import os

users = {
    "Foo" : "Bar",
    "FooBar" : "Baz" 
}

user_items = []

def check_login(username, password):
    if(len(users) == 0):
        return False

    if (users.get(username) == password):
        return True
    
    return False

def save_user_info(username, user_items):
    path = 'usrs/' + username
    user_file = ""
    fileExists = os.path.exists(path)

    if (not fileExists):
        user_file = open(path, 'x')
        user_file.close()

    user_file = open(path, 'w')

    for item in user_items:
        if (not user_items[len[user_items] - 1] == item):
            user_file.write(item + "\n")
        
        else:
            user_file.write(item)


def add_item(item):
    user_items.append(item)

def fetch_items(username):
    path = 'usrs/' + username
    fileExists = os.path.exists(path)

    if (not fileExists):
        return []
    
    user_file = open(path, "r")
    user_inventory = user_file.read()

    return user_inventory.split("\n")

def check_login(username, password):
    if(len(users) == 0):
        return False

    if (users.get(username) == password):
        return True
    
    return False

def input_loop(options):
    # options is a list of strings
    i = ''
    while i not in options:
        i = input('Option: ')
    return i

def ui_index():
    print('Welcome to Lagra (TM)')
    print('\nl) Log in')
    print('q) Quit\n')
    option = input_loop(['l', 'q'])
    match option:
        case 'l':
            ui_login()
        case 'q':
            pass
    print('Thank you for using Lagra (TM)!')

def ui_login():
    while True:
        username = input('    User: ')
        password = input('Password: ')
        login_ok = check_login(username, password)
        match login_ok:
            case True:
                print('temp')
                # Switch to logged in user
            case False:
                print('Invalid username or password')
                print('\nr) Try again')
                print('q) Quit\n')
                option = input_loop(['r', 'q'])
                match option:
                    case 'r':
                        continue
                    case 'q':
                        break

def ui_user(user):
    print('Welcome' + user)
    list_items()

    while True:
        print('Select an action')
        print('\na) Add item')
        print('l) List items')
        print('q) Log out')
        option = input_loop(['a', 'l', 'q'])
        match option:
            case 'a':
                add_item()
            case 'l':
                list_items()
            case 'q':
                break
