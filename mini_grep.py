import argparse


def get_value():
    """функция ввода с консоли выбора файла для
    поиска в нем строки содержащей нужное слово"""

    global rand_num_range_from,rand_num_range_to
    parser = argparse.ArgumentParser(description='Параметрами нужно указывать имя файла и искомое слово ')
    parser.add_argument("-f", default='', type=str, help="аргумент 'f' имя файла , или путь к нему")
    parser.add_argument("-s", default='', type=str, help="аргумент 'ы' искомое слово")
    args = parser.parse_args()
    name_file = args.f
    word = args.s
    return name_file, word


def open_file(name_file,word):
    """Функция поиска слова в тексте
    принимает в ввиде аргументов:
    name_file   - имя файла
    word        - искомое выражение
    результат функции :
     -список list() строк имеющие в себе искомое выражение
    """
    rezult = list()
    with open(name_file, "r") as file_txt:
        for line in file_txt:
            if word in line:
                rezult.append(str(line))
        if not rezult:
            print(f"текста {word} нет в файле{name_file}")
    return rezult

def main():
    if __name__ == '__main__':
        name_file, word = get_value()
        rezult = open_file(name_file,word)
        for line in rezult:
            print(line ,end="")
main()