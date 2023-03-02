#Sum of Numbers

def get_sum(a,b):
    total = 0
    if b >= a:
        for x in range(a, b + 1):
            total += x
        return total    
    else:
        for x in range(b, a + 1):
            total += x
        return total
     
# Решение попроще))
     
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if b > a:
    print(sum(range(a, b + 1)))
else:
    print(sum(range(b, a + 1)))     