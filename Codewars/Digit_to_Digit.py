number = 9119
number = str(number)
result = 0
string = ""
for i in range(len(number)):
    result += int(number[i]) * int(number[i])
    string += str(result)
    result = 0
print(string)


#num = input("Введите число: ")
#string = ""
#for i in num:
    #string += str(int(i)**2)    
#print(string)    