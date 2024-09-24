#input desired n
n = int(input("Choose a length of the game: "))

def isDivisibleByThree(number):
    return number % 3 == 0

def isDivisibleByFive(number):
    return number % 5 == 0

def flippblipp (n):
    
        xPlus = x + 1
        output = ""

        if (isDivisibleByThree(xPlus)):
            output += ("flipp ")  

        if (isDivisibleByFive(xPlus)):
            output += ("blipp")
        
        if output == "":
            output += (str(xPlus))

        return str(output)

for x in range(n):
    print(flippblipp(x))