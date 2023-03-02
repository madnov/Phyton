#Century From Year
def main():
    number = int(input('Введите число: '))
    century(number)

def century(year):
    import math
    if year >= 1000 and year <= 10000:
        if year % 100 > 0:
            return math.floor(year / 100) + 1
        else:
            return math.floor(year / 100)    
    elif year >= 100 and year < 1000:
        if year % 100 > 0:
            return math.floor(year / 100) + 1
        else:
            return math.floor(year / 100)
    elif year >= 10 and year < 100:
        return 1

if __name__ == "__main__":
    main()

#Решение попроще)))
    number = int(input("Введите число: "))
if number % 100 == 0:
    print(number // 100)
else:
    print(number // 100 + 1)   