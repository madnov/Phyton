import random 

n = []
for i in range(10):
    i = random.randint(1,11)
    n.append(i)    

def get_summ(n):
    if n == []:
        return 0
    else: 
        return n[0] + get_summ(n[1:])    

print(n)
print(f'Сумма списка равна: {get_summ(n)}')

