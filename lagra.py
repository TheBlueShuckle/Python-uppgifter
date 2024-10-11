def index():
    print('Welcome to Lagra (TM)\n')
    print('l) Log in')
    print('q) Quit\n')
    option = input_loop(['l', 'q'])
    match i:
        case 'l':
            login()
        case 'q':
            print('Thank you for using Lagra (TM)!')

def input_loop(options):
    # options is a list of strings
    i = ''
    while i not in options:
        i = input('\nOption: ')
    return i

index()