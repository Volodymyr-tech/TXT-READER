import os
import re

pattern = r"[.,/\\ 0-9]"
replacement = ""


def clear_names(file_path: str):
    # Создаём путь к файлу
    full_path = os.path.join('data', file_path)

    # Читаем содержимое файла с указанием кодировки
    with open(full_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Заменяем все совпадения на replacement
    new_content = re.sub(pattern, replacement, content)

    # Удаляем пустые строки с использованием регулярных выражений
    new_content = re.sub(r'\n\s*\n', '\n', new_content)

    # Записываем новое содержимое в файл с указанием кодировки
    with open(full_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

    # Выводим сообщение о завершении обработки
    print(f"Файл {file_path} успешно обработан.")


# Пример использования
bad_data = "names.txt"  # Имя файла, который нужно изменить
clear_names(bad_data)
