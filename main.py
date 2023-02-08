from functions import *
from Metods import *
from rand import *


def start(update, context):
    update.message.reply_text(
        'Привет! Я справочник по языку Python.\n /help')


def help(update, context):
    update.message.reply_text('Вот, что я умею:\n' + '\n'.join([j + exp[ind1][ind2] for ind1, i in enumerate(board)
                                                                for ind2, j in enumerate(i)]), reply_markup=markup)


def themes(update, context):
    update.message.reply_text('Темы:\n'
                              '/func - встроенные функции\n'
                              '/listi - методы списков\n'
                              '/stri - методы строк\n'
                              '/lamb - лямбда-функции\n'
                              '/math - модуль math\n'
                              '/rando - модуль random\n'
                              '/date - модуль datetime\n'
                              '/osi - модуль os\n'
                              '/syss - модуль sys\n')


def bugs(update, context):
    pass


def techsupport(update, context):
    update.message.reply_text('Если у вас возникла какая-то ошибка,'
                              ' вы можете описать её в нашем официальном телеграмм канале'
                              'https://t.me/+nu9ccH0eIVw3MzYy')


def DONATE(update, context):
    pass


def stop(update, context):
    pass


def func(update, context):
    update.message.reply_html(text='<u><b>abs()</b></u> - абсолютное значение числа \n(/func_abs)\n'
                                   '<u><b>chr()</b></u> - перевод Unicode в строку \n(/func_chr)\n'
                                   '<u><b>callable()</b></u> - является ли объект вызываемым \n(/func_callable)\n'
                                   '<u><b>dict()</b></u> - создание словарей \n(/func_dict)\n'
                                   '<u><b>dir()</b></u> - выводит список вех атрибутов и методов объекта '
                                   '\n(/func_dir)\n'
                                   '<u><b>enumerate()</b></u> - нумерует последовательность \n(/func_enumerate)\n'
                                   '<u><b>eval()</b></u> - обработка математических выражений \n(/func_eval)\n'
                                   '<u><b>filter()</b></u> - фильтрует итерируемые объекты \n(/func_filter)\n'
                                   '<u><b>float()</b></u> - создаёт число с плавающей точкой \n('
                                   '/func_filter)\n '
                                   '<u><b>input()</b></u> - ввод данных \n(/func_input)\n'
                                   '<u><b>print()</b></u> - вывода данных \n(/func_print)\n'
                                   '<u><b>int()</b></u> - создаёт целое число \n(/func_int)\n'
                                   '<u><b>iter()</b></u> - привращает объект в итерируемый \n(/func_iter)\n'
                                   '<u><b>max()</b></u> - максимальное значение последовательности \n(/func_max)\n'
                                   '<u><b>min()</b></u> - минимальное значение последовательности \n(/func_min)\n'
                                   '<u><b>len()</b></u> - длинна последовательности \n(/func_len)\n'
                                   '<u><b>list()</b></u> - создание списков \n(/func_list)\n'
                                   '<u><b>map()</b></u> - применение функций к итерируемому объекту \n(/func_map)\n'
                                   '<u><b>next()</b></u> - перебирает итерируемые объекты \n(/func_next)\n'
                                   '<u><b>ord()</b></u> - перевод строки в Unicode \n(/func_ord)\n'
                                   '<u><b>reversed()</b></u> - разворачивает последовательность \n(/func_reversed)\n'
                                   '<u><b>range()</b></u> - создания последовательности с заданными значениями '
                                   '\n(/func_range)\n '
                                   '<u><b>sorted()</b></u> - сортирует последовательность \n(/func_sorted)\n'
                                   '<u><b>str()</b></u> - создание строки \n(/func_str)\n'
                                   '<u><b>set()</b></u> - создание множества \n(/func_set)\n'
                                   '<u><b>sum()</b></u> - суммирует все элементы множества \n(/func_sum)\n'
                                   '<u><b>tuple()</b></u> - создание кортежей \n(/func_tuple)\n'
                                   '<u><b>type()</b></u> - возвращает тип объекта либо создает новый объект '
                                   '\n(/func_type)\n')


def DEBUG(update, context):
    pass


def listi(update, context):
    operations_list(update, context)


def stri(update, context):
    operations_str(update, context)


def lamb(update, context):
    pass


def math(update, context):
    pass


def rando(update, context):
    update.message.reply_html("""/rand_random - число от 0.0 до 1.0
/rand_seed - семя генератора чисел
/rand_uniform - вещественное число в диапазоне
/rand_randint - целое число в диапазоне
/rand_choince - элемент из любой последовательности
/rand_randrange - число из последовательности range
/rand_shuffle - перемешивает последовательность""")


def date(update, context):
    update.message.reply_html("""Модуль datetime предназначен для работы с датами и временем и предоставляет, кроме функций, несколько новых типов данных.
    """)


def osi(update, context):
    update.message.reply_html("""Модуль os в Python — это библиотека функций для работы с операционной системой.
        """)


def syss(update, context):
    pass


def main():
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("themes", themes))
    dp.add_handler(CommandHandler("bugs", bugs))
    dp.add_handler(CommandHandler("techsupport", techsupport))
    dp.add_handler(CommandHandler("DONATE", DONATE))
    dp.add_handler(CommandHandler("stop", stop))
    dp.add_handler(CommandHandler("func", func))
    dp.add_handler(CommandHandler("listi", listi))
    dp.add_handler(CommandHandler("stri", stri))
    dp.add_handler(CommandHandler("lamb", lamb))
    dp.add_handler(CommandHandler("math", math))
    dp.add_handler(CommandHandler("rando", rando))
    dp.add_handler(CommandHandler("date", date))
    dp.add_handler(CommandHandler("osi", osi))
    dp.add_handler(CommandHandler("syss", syss))
    add_function_handler()
    add_random_handler()
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
