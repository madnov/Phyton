# Does my number look big in this?

number = str(number)
result = 0
for i in range(len(number)):
    result += int(number[i])**len(number)
   
#if result == number:
    #return True
#else:
    #return False    
