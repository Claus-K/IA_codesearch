import json

mylist_repo = []
mylist_func = []
mylist_original_string = []
mylist_language = []


def open_file(file: str):
    with open(file, 'r') as json_file:
        json_array = list(json_file)
    return json_array


def read_obj(json_array):
    for x in json_array:
        obj = json.loads(x)
        if obj['repo'] != "":
            mylist_repo.append(obj['repo'])
        if obj['func_name'] != "":
            mylist_func.append(obj['func_name'])


def _count_(list):
    return len(list)


def _remove_duplicates_(mylist):
    array = mylist
    array = list(dict.fromkeys(array))
    return array


def __str__(mylist):
    for x in mylist:
        print(x)


n = 0
__size__ = 1
while n != __size__:
    print("Documento: {}".format(n))
    file_name = "java_train_n.jsonl"
    file_name = (file_name[:11] + n.__str__() + file_name[12:])
    json_list = open_file(file_name)
    n += 1
    read_obj(json_list)
    read_obj(json_list)
    if n == __size__:
        print("Quantidade de Repositorios: {}".format(_count_(mylist_repo)))
        print("Quantidade de Funcoes: {}".format(_count_(mylist_func)))
        mylist_repo = _remove_duplicates_(mylist_repo)
        print("N de Repositorios dict: {}".format(_count_(mylist_repo)))
        mylist_func = _remove_duplicates_(mylist_func)
        print("N de Funcoes dict: {}".format(_count_(mylist_func)))

__str__(mylist_repo)
__str__(mylist_func)
