#input desired n
n = int(input("Choose a length of the game: "))

def isDivisibleByThree(number):
    return number % 3 == 0

def isDivisibleByFive(number):
    return number % 5 == 0


for x in range(n):
    number = x + 1
    
    if (isDivisibleByThree(number) and isDivisibleByFive(number)):
        print("flipp blipp")
        
    elif (isDivisibleByFive(number)):
        print("blipp")
        
    elif (isDivisibleByThree(number)):
        print("flipp")
    
    else:
        print(number)