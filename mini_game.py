import random


def mini_game():
    comp_number = random.randint(1, 101)
    user_number = int(input('Угадайте число от 1 до 100: '))
    count = 1
    while user_number != comp_number:
        if comp_number > user_number:
            count += 1
            print('Загаданное число больше, попробуйте ещё раз.')
            user_number = int(input('Угадайте число от 1 до 100: '))
        elif comp_number < user_number:
            count += 1
            print('Загаданное число меньше, попробуйте ещё раз.')
            user_number = int(input('Угадайте число от 1 до 100: '))
    print(
        f"Поздравляем вы угадали c {count} попытки, загаданное число: {comp_number} ")
