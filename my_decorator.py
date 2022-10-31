import datetime
import os


def my_decor_decorator(log_path):

    def my_decorator(some_function):
        """
        Функция-декоратор
        Он записывает в файл дату и время вызова функции, имя функции,
        аргументы, с которыми она вызывалась и возвращаемое значение.
        :param some_function: декорируемая функция
        :return:
        """

        def arrange_function(*args, **kwargs):

            if not os.path.isdir(log_path):
                os.mkdir(log_path)

            with open(log_path + 'decorator_log.txt', 'a', encoding='cp1251'
                      ) as f:
                f.write(str(datetime.datetime.now().strftime('%y-%b-%d '
                                                             '%H:%M:%S'))
                        + ' | ')
                f.write('Function: ' + some_function.__name__ + ' | ')
                f.write('Arguments: ' + str(args[0]) + ' | ')
                result = some_function(*args)
                f.write('Result: ' + result + '\n')
            return result

        return arrange_function

    return my_decorator
