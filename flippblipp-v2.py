#input desired n
n = int(input("Choose a length of the game: "))

def isDivisibleByThree(number):
    return number % 3 == 0

def isDivisibleByFive(number):
    return number % 5 == 0

def flippblipp (n):
    
        nPlus = n + 1
        output = ""

        if (isDivisibleByThree(nPlus)):
            output += ("flipp ")  

        if (isDivisibleByFive(nPlus)):
            output += ("blipp")
        
        if output == "":
            output += (str(nPlus))

        return str(output)

for x in range(n):
    print(flippblipp(x))