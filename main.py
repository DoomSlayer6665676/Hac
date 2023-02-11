from functions import *
from Metods import *
from rand import *
from mat import *
from osi import *
from lam import *


def start(update, context):
    update.message.reply_text(
        'Привет! Я справочник по языку Python.\nНАЖМИ---> /help')


def help(update, context):
    update.message.reply_text('Вот, что я умею:\n' + '\n'.join([j + exp[ind1][ind2] for ind1, i in enumerate(board)
                                                                for ind2, j in enumerate(i)]), reply_markup=markup)


def themes(update, context):
    update.message.reply_text('Темы:\n'
                              '/func - встроенные функции\n'
                              '/listi - изменение списков\n'
                              '/stri - изменение строк\n'
                              '/lamb - лямбда-функции\n'
                              '/math - модуль math\n'
                              '/rando - модуль random\n'
                              '/date - модуль datetime\n'
                              '/osi - модуль os\n'
                              '/syss - модуль sys\n', reply_markup=markup)


def techsupport(update, context):
    update.message.reply_text('Если у вас возникла какая-то ошибка,'
                              ' вы можете описать её в нашем официальном телеграмм канале'
                              'https://t.me/+nu9ccH0eIVw3MzYy')


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
                                   '\n(/func_type)\n', reply_markup=create_markup([['/themes', '/func']]))


def listi(update, context):
    update.message.reply_html("""В этом блоке рассказывается о таком типе данных, как списки, операциях над ними и методах, о генераторах списков и о применении списков.
    Операции над списками - /operations_list
    Методы списков - /methods_list""", reply_markup=create_markup([['/themes', '/listi']]))


def stri(update, context):
    update.message.reply_html("""В этом блоке рассказывается о таком типе данных, как строки, операциях над ними и методах, о генераторах строк и о применении списков.
        Операции над списками - /operations_str
        Методы списков - /methods_str""", reply_markup=create_markup([['/themes', '/stri']]))


def lamb(update, context):
    update.message.reply_html("""Лямбда-функция в Python — это просто функция Python. Но это некий особенный тип с ограниченными возможностями.\n
        Базовый синтаксис лямбда-функции в Python - lambda arguments: expression\n
        Возникает вопрос: а зачем нужны лямбда-функции, если их можно объявлять традиционным образом? 
        Но на самом деле, они полезны лишь в том случае, когда нужна одноразовая функция. Такие функции еще называют анонимными.\n
        Определить лямбда-функцию с одним аргументом не составляет труда.\n(/lam_1arg)\n
        А если их должно быть несколько, то достаточно лишь разделить значения запятыми.\n(/lam_narg)\n
        Допустим, нужно создать функцию без аргументов, которая бы возвращала True.\n(/lam_farg)\n
        В определенный момент возникнет вопрос: а можно ли иметь лямбда-функцию из нескольких строк.\n
        Ответ однозначен: <b>нет</b>.\n
        Лямбда-функции в Python всегда принимают только одно выражение. Если же их несколько, то лучше создать обычную функцию.\n
        Теперь рассмотрим самые распространенные примеры использования лямбда-функций.\n
        Распространенная операция со списками в Python — применение операции к каждому элементу.\n
        <u><b>map()</b></u> — это встроенная функция Python, принимающая в качестве аргумента функцию и последовательность. 
        Она работает так, что применяет переданную функцию к каждому элементу.\n(/lam_map)\n
        <u><b>filter()</b></u> — это еще одна встроенная функция, которая фильтрует последовательность итерируемого объекта.\n(/lam_fil)\n
        Другими словами, функция filter отфильтровывает некоторые элементы итерируемого объекта (например, списка) на основе какого-то критерия. 
        Критерий определяется за счет передачи функции в качестве аргумента. Она же применяется к каждому элементу объекта.\n
        Сортировка списка — базовая операция в Python. Если речь идет о списке чисел или строк, то процесс максимально простой. Подойдут встроенные функции sort и sorted.\n
        Но иногда имеется список кастомных объектов, сортировать которые нужно на основе значений одного из полей. В таком случае можно передать параметр key в sort или sorted. Он и будет являться функцией.\n
        Функция применяется ко всем элементам объекта, а возвращаемое значение — то, на основе чего выполнится сортировка.\n(/lam_sort)\n
        Как уже упоминалось, лямбда могут иметь только одно выражение (expression) в теле.\n
        Обратите внимание, что речь идет не об инструкции (statement).\n
        Выражение и инструкции — две разные вещи, в которых часто путаются. В программировании инструкцией является строка кода, выполняющая что-то, но не генерирующая значение.\n
        Например, инструкция if или циклы for и while являются примерами инструкций. Заменить инструкцию на значение попросту невозможно.\n
        А вот выражения — это значения. Запросто можно заменить все выражения в программе на значения, и программа продолжит работать корректно.\n
        Тело лямбда-функции должно являться выражением, поскольку его значение будет тем, что она вернет. Обязательно запомните это для работы с лямбда-функциями в будущем.\n
        """, reply_markup=create_markup([['/themes', '/lamb']]))


def math(update, context):
    update.message.reply_html("""Модуль math – один из наиважнейших в Python. Этот модуль предоставляет обширный функционал для работы с числами.\n
<u><b>math.ceil(X)</b></u> – округление до ближайшего большего числа.\n(/math_seil)\n
<u><b>math.fabs(X)</b></u> - модуль X.\n(/math_fabs)\n
<u><b>math.factorial(X)</b></u> - факториал числа X.\n(/math_factorial)\n
<u><b>math.floor(X)</b></u> - округление вниз.\n(/math_floor)\n
<u><b>math.isfinite(X)</b></u> - является ли X числом.\n(/math_isfinite)\n
<u><b>math.isinf(X)</b></u> - является ли X бесконечностью.\n(/math_isinf)\n
<u><b>math.isnan(X)</b></u> - является ли X NaN (Not a Number - не число).\n(/math_isnan)\n
<u><b>math.sqrt(X)</b></u> - квадратный корень из X.\n(/math_sqrt)\n
<u><b>math.acos(X)</b></u> - арккосинус X. В радианах.\n(/math_acos)\n
<u><b>math.asin(X)</b></u> - арксинус X. В радианах.\n(/math_asin)\n
<u><b>math.atan(X)</b></u> - арктангенс X. В радианах.\n(/math_atan)\n
<u><b>math.cos(X)</b></u> - косинус X (X указывается в радианах).\n(/math_cos)\n
<u><b>math.sin(X)</b></u> - синус X (X указывается в радианах).\n(/math_sin)\n
<u><b>math.tan(X)</b></u> - тангенс X (X указывается в радианах).\n(/math_tan)\n
<u><b>math.degrees(X)</b></u> - конвертирует радианы в градусы.\n(/math_degrees)\n
<u><b>math.radians(X)</b></u> - конвертирует градусы в радианы.\n(/math_radians)\n
    """, reply_markup=create_markup([['/themes', '/math']]))


def rando(update, context):
    update.message.reply_html("""Этот модуль реализует генераторы псевдослучайных чисел для различных дистрибутивов.\n
<u><b>random.random</b></u> - число от 0.0 до 1.0\n(/rand_random)
<u><b>random.seed</b></u> - семя генератора чисел\n(/rand_seed)
<u><b>random.uniform</b></u> - вещественное число в диапазоне\n(/rand_uniform)
<u><b>random.randint</b></u> - целое число в диапазоне\n(/rand_randint)
<u><b>random.choince</b></u> - элемент из любой последовательности\n(/rand_choince)
<u><b>random.randrange</b></u> - число из последовательности range\n(/rand_randrange)
<u><b>random.shuffle</b></u> - перемешивает последовательность\n(/rand_shuffle)""", reply_markup=create_markup([['/themes', '/rando']]))


def date(update, context):
    update.message.reply_html("""Модуль datetime предназначен для работы с датами и временем и предоставляет, кроме функций, несколько новых типов данных.
    """, reply_markup=create_markup([['/themes', '/date']]))


def osi(update, context):
    update.message.reply_html("""Модуль os в Python — это библиотека функций для работы с операционной системой.\n
<u><b>/os_info</b></u> - Получение информации об ОС\n
<u><b>/working_directory</b></u> - Изменение рабочей директории\n
<u><b>/path_existence</b></u> - Проверка существования пути\n
<u><b>/creating_directories</b></u> - Создание директорий\n
<u><b>/deleting_files_directories</b></u> - Удаление файлов и директорий\n
<u><b>/start_</b></u> - Запуск на исполнение\n
<u><b>/directory_file_name</b></u> - Получение имени файла и директории\n
<u><b>/size</b></u> - Вычисление размера\n
<u><b>/renaming</b></u> - Переименование\n
<u><b>/content</b></u> - Содержимое директорий\n
<u><b>/info</b></u> - Информация о файлах и директориях\n
<u><b>/path_handling</b></u> - Обработка путей\n""", reply_markup=create_markup([['/themes', '/osi']]))


def syss(update, context):
    pass


def main():
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("themes", themes))
    dp.add_handler(CommandHandler("techsupport", techsupport))
    dp.add_handler(CommandHandler("func", func))
    dp.add_handler(CommandHandler("listi", listi))
    dp.add_handler(CommandHandler("stri", stri))
    dp.add_handler(CommandHandler("lamb", lamb))
    dp.add_handler(CommandHandler("math", math))
    dp.add_handler(CommandHandler("rando", rando))
    dp.add_handler(CommandHandler("date", date))
    dp.add_handler(CommandHandler("osi", osi))
    dp.add_handler(CommandHandler("syss", syss))
    add_metods_handler()
    add_function_handler()
    add_random_handler()
    add_mat_handler()
    add_os_handler()
    add_lam_handler()
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
