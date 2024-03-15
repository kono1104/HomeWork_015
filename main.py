# Для выполнения этой задачи понадобится использовать модули os, logging и collections.namedtuple. 
# Вот пример кода, который решает задание:

import logging
from collections import namedtuple

# Настройка логирования
logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Создание namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent_directory'])

def collect_directory_info(directory_path):
    """
# Функция для сбора информации о содержимом директории
# и записи ее в текстовый файл через логирование.
    """
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        is_dir = os.path.isdir(item_path)

        if is_dir:
            name = item
            extension = None
        else:
            name, extension = os.path.splitext(item)

        parent_directory = os.path.basename(directory_path)

        file_info = FileInfo(name=name, extension=extension, is_dir=is_dir, parent_directory=parent_directory)

        # Запись информации в файл через логирование
        logging.info(f"Name: {file_info.name}, Extension: {file_info.extension}, is_dir: {file_info.is_dir}, Parent Directory: {file_info.parent_directory}")

if __name__ == "__main__":
    import sys

    # Проверка аргументов командной строки
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    # Проверка существования директории
    if not os.path.isdir(directory_path):
        print("Directory does not exist.")
        sys.exit(1)

    # Сбор информации о содержимом директории и запись в файл
    collect_directory_info(directory_path)
    print("Directory info collected and logged successfully.")
# Сохраним этот код в файле с расширением .py, например, directory_info_collector.py. 
# Запустим его из командной строки, указав путь до директории в качестве аргумента. Например:


python directory_info_collector.py /path/to/directory
# Затем найдем информацию о содержимом указанной директории в файле directory_info.log, который будет создан в том же каталоге, откуда был запущен скрипт.
