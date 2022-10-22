# Домашнее задание «Декораторы»
from my_decorator import my_decor_decorator

my_path = "C:/TEMP_Decorator_logs/"


@my_decor_decorator(my_path)
def concat_string(str_list):
    """
    Функция для суммирования строк
    Функционал выбран произвольно для демонстрации работы декоратора
    :param str_list: список строк для суммирования
    :return: строка - сумма всех строк входного списка
    """
    s = ''
    for i in str_list:
        s += i
    return s


@my_decor_decorator(my_path)
def is_arithm_progression(num_list):
    """
    Функция для определения того, является ли последовательность
    арифметической прогрессией
    Функционал выбран произвольно для демонстрации работы декоратора
    :param num_list: список с последовательностю чиисел
    :return: строка с ответом является ли входной список арифм прогрессией
    """
    step = 0
    for i in range((len(num_list) - 1)):
        if num_list[i+1] - num_list[i] == 0:
            return 'Not an arithmetic progression'
        elif step == 0:
            step = num_list[i+1] - num_list[i]
        elif num_list[i+1] - num_list[i] != step:
            return 'Not an arithmetic progression'
    return 'An arithmetic progression'


@my_decor_decorator(my_path)
def is_geometric_progression(num_list):
    """
        Функция для определения того, является ли последовательность
        геометрической прогрессией
        Функционал выбран произвольно для демонстрации работы декоратора
        :param num_list: список с последовательностю чиисел
        :return: строка с ответом является ли входной список геометрической
         прогрессией
        """
    factor = 1
    for i in range((len(num_list) - 1)):
        if num_list[i+1] / num_list[i] == 1:
            return 'Not a geometric progression'
        elif factor == 1:
            factor = num_list[i+1] / num_list[i]
        elif num_list[i+1] / num_list[i] != factor:
            return 'Not a geometric progression'
    return 'A geometric progression'


my_favorit_funcs = {
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10): is_arithm_progression,
    ('"Фифти-фифти"', ' = ', '"так-сяк"', ' = ', '"туда-сюда"', ' = ',
     '"середина на половину"'): concat_string,
    (1, 2, 4, 8, 16, 32, 64, 128, 256, 513): is_geometric_progression,
    ('Слава ', 'труду!'): concat_string
}

if __name__ == '__main__':

    for key, value in my_favorit_funcs.items():
        value(key)

    print()
    print('Работа программы завершена, результат см. в лог-файле по адресу:')
    print(my_path)
