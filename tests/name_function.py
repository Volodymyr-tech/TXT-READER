import os
import re

pattern_eng = r"[a-zA-Z]+"
pattern_rus = r"[а-яА-Я]+"
data_path = r"C:\Users\Владимир\PycharmProjects\Open-change-txt\data"


def name_function(name_list: str) -> str:
    '''Функция разделения списка на английские и русские имена'''
    file_path = os.path.join(data_path, name_list)

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()  # Используем read() для получения всей строки

    eng_names = re.findall(pattern_eng, content)  # Ищем все английские слова
    rus_names = re.findall(pattern_rus, content)  # Ищем все русские слова

    eng_file_path = os.path.join(data_path, "eng_name.txt")  # Путь для файла с английскими именами
    rus_file_path = os.path.join(data_path, "rus_name.txt")  # Путь для файла с русскими именами

    with open(eng_file_path, "w", encoding="utf-8") as file:
        file.write("\n".join(eng_names))  # Записываем английские слова по одному

    with open(rus_file_path, "w", encoding="utf-8") as file:
        file.write("\n".join(rus_names))  # Записываем русские слова по одному

    return eng_names, rus_names


mixed_names = "names.txt"
result = name_function(mixed_names)
print(result)
