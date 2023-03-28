import random
import sys

def mini_game():
    computer_number = random.randint(1, 101)
    user_number = int(input('Угадайте число от 1 до 100: '))
    count = 1
    while user_number != computer_number:
        if computer_number > user_number:
            count += 1
            print('Загаданное число больше, попробуйте ещё раз.')
            user_number = int(input('Угадайте число от 1 до 100: '))
        elif computer_number < user_number:
            count += 1
            print('Загаданное число меньше, попробуйте ещё раз.')
            user_number = int(input('Угадайте число от 1 до 100: '))
    print(
        f"Поздравляем вы угадали c {count} попытки, загаданное число: {computer_number} ")


command = sys.argv[1]
if command == 'game':
    mini_game()