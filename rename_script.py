import os
import re

def file_rename(dir, symbol_1, symbol_2) -> None:
    for old_file in os.listdir(dir):
        new_file = re.sub(symbol_1, symbol_2, old_file, count=0, flags=0)
        os.rename(f'{dir}/{old_file}', f'{dir}/{new_file}')
    print('Все переименовано, проверяй!')

dir = str(input('Введите полный путь до папки с фалами (без / на конце): '))
symbol_1 = str(input('Введите символ который хотите заменить: '))
symbol_2 = str(input('Введите символ на который хотите заменить: '))

if __name__ == '__main__':
    file_rename(dir, symbol_1, symbol_2)
