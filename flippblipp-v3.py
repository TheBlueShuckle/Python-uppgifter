def isDivisibleByThree(number):
    return number % 3 == 0

def isDivisibleByFive(number):
    return number % 5 == 0

def flippblipp(number):
        output = ""

        if (isDivisibleByThree(number)):
            output += ("flipp")  

        if (isDivisibleByFive(number)):
            
            if(output != ""):
                 output += " "

            output += ("blipp")
        
        if output == "":
            output += (str(number))

        return str(output)

x = 1

print(x)

while(True):
     x += 1
     guess = input("Nästa: ")

     if(guess != flippblipp(x)):
          print("Fel - " + flippblipp(x))
          break
