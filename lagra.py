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
        i = input('\nOption: ')
    return i

def ui_index():
    print('Welcome to Lagra (TM)')
    print('\nl) Log in')
    print('q) Quit')
    option = input_loop(['l', 'q'])
    match option:
        case 'l':
            ui_login()
        case 'q':
            pass
    print('Thank you for using Lagra (TM)!')

def ui_login():
    while True:
        username = input('\n    User: ')
        password = input('Password: ')
        login_ok = check_login(username, password)
        match login_ok:
            case True:
                ui_user(username)
                break
            case False:
                print('Invalid username or password')
                print('\nr) Try again')
                print('q) Quit')
                option = input_loop(['r', 'q'])
                match option:
                    case 'r':
                        continue
                    case 'q':
                        break

def ui_user(user):
    print('\nWelcome ' + user)
    #ui_list_items(user)

    while True:
        print('\nSelect an action')
        print('a) Add item')
        print('l) List items')
        print('q) Log out')
        option = input_loop(['a', 'l', 'q'])
        match option:
            case 'a':
                ui_add_item()
            case 'l':
                ui_list_items(user)
            case 'q':
                break

def ui_list_items(user):
    items = fetch_items(user)
    for n in items:
        print(n + ') ' + items[n])

def ui_add_item():
    item = input('Add item: ')
    add_item(item)
    save_user_info()