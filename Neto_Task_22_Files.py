import os

def get_list_file():
    return [file for file in os.listdir(os.getcwd()) if file.endswith(".txt")]

def sort_files_by_len():
    list_file = get_list_file()
    list_file_sorted = []
    for file in list_file:
        with open(file, encoding='utf-8') as f:
            len_f = len(f.readlines())
            list_file_sorted.append([file, len_f])
    list_file_sorted.sort(key=lambda x: x[1])
    return list_file_sorted

def write_file():
    list_file_sorted = sort_files_by_len()
    f_to = open('result_file.txt', 'a', encoding='utf-8')
    for elem in list_file_sorted:
        with open(elem[0], encoding='utf-8') as f_from:
            tmp = f_from.read()
        f_to.write(f'{elem[0]}\n{elem[1]}\n')
        f_to.write(f'{tmp}\n')
    print("<Данные добавлены в 'result_file.txt'>")
    f_to.close()

write_file()







