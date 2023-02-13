# Задача № 3

def main():
    numbers = get_numbers()
    maxIndex = get_maxIndex(numbers)
    minIndex = get_minIndex(numbers)
    total = get_total(numbers, maxIndex, minIndex)
    print(total)

def get_numbers():
    numbers = []
    count = int(input('Введите количество цифр которые хотите ввести: '))
    for x in range(count):
        x = int(input('Введите число: '))
        numbers.append(x)
    return numbers

def get_maxIndex(numbers):
    index = 0
    maxIndex = 0
    maxNum = numbers[index]
    while index < len(numbers):
         if numbers[index] > maxNum:
            maxIndex = index
            maxNum = numbers[index]
            index += 1
         else:
            index += 1
    return  maxIndex

def get_minIndex(numbers):
    index = 0
    minIndex = 0
    minNum = numbers[index]
    while index < len(numbers):
        if numbers[index] < minNum:
            minIndex = index
            minNum = numbers[index]
            index += 1
        else:
            index += 1
    return minIndex

def get_total(numbers, maxIndex, minIndex):
    total = 0
    if maxIndex > minIndex:
        while minIndex  < maxIndex - 1:
            total += numbers[minIndex + 1]
            minIndex += 1   
    else:
        while maxIndex < minIndex - 1:
            total += numbers[maxIndex + 1]
            maxIndex += 1        
    return total    
    
if __name__ == '__main__':
    main()
