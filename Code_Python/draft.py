import math

number = int(input("Введите число: "))
input(number)
def input(number):
    try:
        if number != 13:
            return math.sqrt(number)
        
    except:
        return "Value Error"
    
   