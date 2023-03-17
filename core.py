import os
import shutil
import datetime
import random

def create_file(name, text=None):
    with open(name, 'w', encoding='utf=8') as f:
        if text:
            f.write(text)

def create_folder(name):
    try:
        os.mkdir(name)            
    except FileExistsError:
        print('Такая папка уже есть')

def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)        

def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)

def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть')    

def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    print(result)
    with open('log.txt', 'a', encoding='utf=8') as f:
        f.write(result + '\n')

def change_directory(name):
    result = os.chdir(name)

def change_dir_name(name, new_name):
    result = os.rename(name, new_name)

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
            print('Загадонное число меньше, попробуйте ещё раз.')
            user_number = int(input('Угадайте число от 1 до 100: ')) 
    print(f"Поздравляем вы угадали c {count} попытки, загаданное число: {comp_number} ")

if __name__ == '__main__':  
    change_directory()
   