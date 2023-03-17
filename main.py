import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir_name, change_directory, mini_game 

#save_info('Старт')

command = sys.argv[1]

if command == 'list':
    get_list()
elif command == 'create_file':
    try:
        name = sys.argv[2]    
    except IndexError:
        print('Отсутсвует название файла')
    else:
         create_file(name)       
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутсвует название файла')
    else:
        create_folder(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутсвует название файла')
    else:
        delete_file(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print('Отсутсвует название файла')
    else:
        copy_file(name, new_name)

elif command == 'change_name':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print('Отсутствует название файла')
    else:
        change_dir_name(name, new_name)    

elif command == 'change_dir':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутсвует название файла')
    else:
        change_directory(name)        

elif command == 'game':
    result = mini_game()

elif command == 'help':
    print('list - список файлов и папок')
    print('create_file - создание файла')
    print('create_folder - создание папки')
    print('delete - удаление файла или папки')
    print('copy - копирование файла или папки')    
    print('change_name - поменять название папки')
    print('change_dir - сменить директорию')
    print('game - поиграть в мини игру')

#save_info('Конец')    