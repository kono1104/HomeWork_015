# Задача №1. Настроить в ней запуск скрипта с параметрами. (используем Пайчарм и модуль argparse).
import argparse
import logging

logging.basicConfig(filename='Log/log_1.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{levelname} - {asctime} в строке {lineno} '
                           'функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.ERROR)
logger = logging.getLogger(__name__)


def division(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        logger.error(
            f'Ошибка деления на ноль! Число {a} нельзя поделить на число {b}')
        return float('inf')
    return res


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Пример использования argparse в PyCharm')
    parser.add_argument('numerator', type=float, help='Числитель')
    parser.add_argument('denominator', type=float, help='Знаменатель')
    args = parser.parse_args()

    result = division(args.numerator, args.denominator)
    print(f'Результат деления: {result}')