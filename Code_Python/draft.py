a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if b > a:
    print(sum(range(a, b + 1)))
else:
    print(sum(range(b, a + 1)))    