from CONST import *


def add_function_handler():
    dp.add_handler(CommandHandler("func_abs", func_abs))
    dp.add_handler(CommandHandler("func_chr", func_chr))
    dp.add_handler(CommandHandler("func_callable", func_callable))
    dp.add_handler(CommandHandler("func_dict", func_dict))
    dp.add_handler(CommandHandler("func_dir", func_dir))
    dp.add_handler(CommandHandler("func_enumerate", func_enumerate))
    dp.add_handler(CommandHandler("func_eval", func_eval))
    dp.add_handler(CommandHandler("func_filter", func_filter))
    dp.add_handler(CommandHandler("func_float", func_float))
    dp.add_handler(CommandHandler("func_input", func_input))
    dp.add_handler(CommandHandler("func_int", func_int))
    dp.add_handler(CommandHandler("func_iter", func_iter))
    dp.add_handler(CommandHandler("func_max", func_max))
    dp.add_handler(CommandHandler("func_min", func_min))
    dp.add_handler(CommandHandler("func_len", func_len))
    dp.add_handler(CommandHandler("func_list", func_list))
    dp.add_handler(CommandHandler("func_map", func_map))
    dp.add_handler(CommandHandler("func_next", func_next))
    dp.add_handler(CommandHandler("func_ord", func_ord))
    dp.add_handler(CommandHandler("func_reversed", func_reversed))
    dp.add_handler(CommandHandler("func_range", func_range))
    dp.add_handler(CommandHandler("func_sorted", func_sorted))
    dp.add_handler(CommandHandler("func_str", func_str))
    dp.add_handler(CommandHandler("func_set", func_set))
    dp.add_handler(CommandHandler("func_sum", func_sum))
    dp.add_handler(CommandHandler("func_tuple", func_tuple))
    dp.add_handler(CommandHandler("func_type", func_type))
    dp.add_handler(CommandHandler("special_print", special_print))
    dp.add_handler(CommandHandler("Special_symbols", Special_symbols))
    dp.add_handler(CommandHandler("func_print", func_print))


def func_abs(update, context):
    send_photo_file('x = -42\n'
                    'abs_x = abs(x)\n'
                    'print(f"Абсолютное значение {x} это {abs_x}")\n'
                    '# Вывод: Абсолютное значение -42 это 42\n',
                    update.message.chat_id, context,
                    name='func_abs')
    update.message.reply_html(text='Встроенная функция <u><b>abs(x)</b></u> в Python возвращает абсолютное значение '
                                   'аргумента x, '
                                   'который может быть целым или числом с плавающей точкой, или же объектом, '
                                   'реализующим '
                                   'функцию __abs__(). Для комплексных чисел функция возвращает их величину. '
                                   'Абсолютное '
                                   'значение любого числового значения -x или +x — это всегда соответствующее '
                                   'положительное +x.')


def func_chr(update, context):
    send_photo_file('>>> chr(97)\n'
                    "'a'\n", update.message.chat_id, context,
                    name='func_chr')
    update.message.reply_html(text='Функция <u><b>chr()</b></u> возвращает строку, представляющую символ Unicode для '
                                   'переданного числа. Она является противоположностью <u><b>ord()</b></u> ('
                                   '/func_ord), '
                                   'которая принимает символ и возвращает его числовой код.')


def func_callable(update, context):
    send_photo_file('>>> callable(5)\n'
                    "False\n", update.message.chat_id, context,
                    name='func_callable')
    update.message.reply_html(text='Вызываемый объект — это объект, который можно вызвать. Функция <u><b>callable('
                                   ')</b></u> сообщает, является ли объект вызываемым. Если да, то возвращает '
                                   '<u><b>True</b></u>, а в противном случае — <u><b>False</b></u>.')


def func_dict(update, context):
    send_photo_file('>>> dict({"a":1, "b":2}, c = 3)\n'
                    "{'a': 1, 'b': 2, 'c': 3}\n\n"
                    '>>> list = [["a",1],["b",2]]\n'
                    '>>> dict(list)\n'
                    "{'a': 1, 'b': 2}\n", update.message.chat_id, context,
                    name='func_dict')
    update.message.reply_html(text='Эта функция используется в Python для создания словарей. Это же можно делать и '
                                   'вручную, но функция предоставляет большую гибкость и дополнительные возможности. '
                                   'Например, ей в качестве параметра можно передать несколько словарей, объединив их '
                                   'в один большой.')


def func_dir(update, context):
    send_photo_file('>>> x = ["Яблоко", "Апельсин", "Гранат"]\n'
                    '>>> print(dir(x))\n'
                    "['__add__', '__class__', '__contains__',....]\n", update.message.chat_id, context,
                    name='func_dir')
    update.message.reply_html(text='Функция <u><b>dir()</b></u> получает список вех атрибутов и методов объекта. Если '
                                   'объект не передать, то функция вернет все имена модулей в локальном пространстве '
                                   'имен.')


def func_enumerate(update, context):
    send_photo_file(">>> x = 'Строка'\n"
                    ">>> list(enumerate(x))\n"
                    "[(0, 'С'), (1, 'т'), (2, 'р'), (3, 'о'), (4, 'к'), (5, 'а')]\n",
                    update.message.chat_id, context,
                    name='func_enumerate')
    update.message.reply_html(text='В качестве параметра эта функция принимает последовательность. После этого она '
                                   'перебирает каждый элемент и возвращает его вместе со счетчиком в виде '
                                   'перечисляемого объекта. Основная особенность таких объектов — возможность '
                                   'размещать их в цикле для перебора.')


def func_eval(update, context):
    send_photo_file(">>> eval('2+2')\n"
                    "4\n"
                    ">>> eval('2*7')\n"
                    "14\n"
                    ">>> eval('5/2')\n"
                    "2.5\n", update.message.chat_id, context,
                    name='func_eval')
    update.message.reply_html(text='<u><b>eval()</b></u> обрабатывает переданное в нее выражение и исполняет его как '
                                   'выражение Python. После этого возвращается значение. Чаще всего эта функция '
                                   'используется для выполнения математических функций.')


def func_filter(update, context):
    send_photo_file("list1 = [3, 5, 4, 8, 6, 33, 22, 18, 76, 1]\n"
                    "result = list(filter(lambda x: (x%2 != 0) , list1))\n"
                    "print(result)\n", update.message.chat_id, context,
                    name='func_float')
    update.message.reply_html(text='Как можно догадаться по названию, эта функция используется для перебора '
                                   'итерируемых объектов и последовательностей, таких как списки, кортежи и словари. '
                                   'Но перед ее использованием нужно также иметь подходящую функцию, которая бы '
                                   'проверяла каждый элемент на валидность. Если элемент подходит, '
                                   'он будет возвращаться в вывод.')


def func_float(update, context):
    send_photo_file(
        ">>> float('596')\n"
        "596.0\n"
        ">>> float(26)\n"
        "26.0\n", update.message.chat_id, context,
        name='func_float')
    update.message.reply_html(text='Эта встроенная функция конвертирует число или строку в число с плавающей точкой и '
                                   'возвращает результат')


def func_input(update, context):
    send_photo_file(">>> value = input('Пожалуйста, введите значение: ')\n"
                    "Пожалуйста, введите значение: 123\n"
                    ">>> value\n"
                    "'123'\n", update.message.chat_id, context,
                    name='func_input')
    update.message.reply_html(text='Функция <u><b>input()</b></u> — это быстрый и удобный способ получить данные от '
                                   'пользователя. Вызов этой функции предоставляет пользователю возможность ввести на '
                                   'экране текст. Затем он конвертируется в строку и возвращается в программу.')


def func_int(update, context):
    send_photo_file(">>> int(5.6)\n"
                    "5\n\n"
                    ">>> int('0101', 2)\n"
                    "5\n", update.message.chat_id, context,
                    name='func_int')
    update.message.reply_html(text='Эта функция возвращает целое число из объекта, переданного в параметра. Она может '
                                   'конвертировать числа с разным основанием (шестнадцатеричные, двоичные и так '
                                   'далее) в целые.')


def func_iter(update, context):
    send_photo_file(">>> lis = ['a', 'b', 'c', 'd', 'e']\n"
                    ">>> x = iter(lis)\n"
                    ">>> next(x)\n"
                    "'a'\n"
                    ">>> next(x)\n"
                    "'b'\n"
                    ">>> next(x)\n"
                    "'c'\n"
                    ">>> next(x)\n"
                    "'d'\n", update.message.chat_id, context,
                    name='func_iter')
    update.message.reply_html(text='Эта функция принимает объект и возвращает итерируемый объект. Сам по себе он '
                                   'бесполезен, но оказывается крайне эффективным при использовании в циклах for и '
                                   'while. Благодаря этому объект можно перебирать по одному свойству за '
                                   'раз.\n/func_next')


def func_max(update, context):
    send_photo_file(
        ">>> max('a', 'A')\n"
        "'a'\n\n"
        ">>> x = [5, 7, 8, 2, 5]\n"
        ">>> max(x)\n"
        "8\n\n"
        ">>> x = ['Яблоко', 'Апельсин', 'Автомобиль']\n"
        ">>> max(x, key = len)\n"
        "'Яблоко'\n", update.message.chat_id, context,
        name='func_max')
    update.message.reply_html(text='Эта функция используется для нахождения «максимального» значения в '
                                   'последовательности, итерируемом объекте и так далее. В параметрах можно менять '
                                   'способ вычисления максимального значения.')


def func_min(update, context):
    send_photo_file(">>> min('a','A')\n"
                    "'A'\n\n"
                    ">>> x = [5, 7, 8, 2, 5]\n"
                    ">>> min(x)\n"
                    "2\n\n"
                    ">>> x = ['Виноград', 'Манго', 'Фрукты', 'Клубника']\n"
                    ">>> min(x)\n"
                    "'Виноград'\n", update.message.chat_id, context,
                    name='func_min')
    update.message.reply_html(text='Эта функция используется для нахождения «минимального» значения в '
                                   'последовательности, итерируемом объекте и так далее. В параметрах можно менять '
                                   'способ вычисления минимального значения.')


def func_len(update, context):
    send_photo_file(
        ">>> x = (2, 3, 1, 6, 7)\n"
        ">>> len(x)\n"
        "5\n"
        ">>> len('Строка')\n"
        "6\n", update.message.chat_id, context,
        name='func_len')
    update.message.reply_html(text='Эта функция используется для вычисления длины последовательности или итерируемого '
                                   'объекта.')


def func_list(update, context):
    send_photo_file(">>> list('Привет')\n"
                    "['П', 'р', 'и', 'в', 'е', 'т']\n\n"
                    ">>> list({1:'a', 2:'b', 3:'c'})\n"
                    "[1, 2, 3]\n", update.message.chat_id, context,
                    name='func_list')
    update.message.reply_html(text='В качестве параметра функция <u><b>list()</b></u> принимает итерируемый объект и '
                                   'возвращает '
                                   'список. Она обеспечивает большие гибкость и скорость при создании списков по '
                                   'сравнению с обычным способом.')


def func_map(update, context):
    send_photo_file(">>> def inc(x):\n"
                    "\t\t\tx = x + 1\n"
                    "\t\t\treturn x\n\n"
                    ">>> lis = [1,2,3,4,5]\n"
                    ">>> result = map(inc,lis)\n\n"
                    ">>> for x in result:\n"
                    "\t\t\tprint(x)\n\n"
                    "2\n"
                    "3\n"
                    "4\n"
                    "5\n"
                    "6\n", update.message.chat_id, context,
                    name='func_map')
    update.message.reply_html(text='Используется для применения определенной функции к итерируемому объекту. Она '
                                   'возвращает результат в виде итерируемого объекта (списки, кортежи, множества). '
                                   'Можно передать и несколько объектов, но в таком случае нужно будет и '
                                   'соответствующее количество функций.')


def func_next(update, context):
    send_photo_file(
        ">>> lis = ['a', 'b', 'c', 'd', 'e']\n"
        ">>> x = iter(lis)\n"
        ">>> next(x)\n"
        "'a'\n"
        ">>> next(x)\n"
        "'b'\n"
        ">>> next(x)\n"
        "'c'\n"
        ">>> next(x)\n"
        "'d'\n", update.message.chat_id, context,
        name='func_next')
    update.message.reply_html(text='Используется для итерируемых объектов. Умеет получать следующий (next) элемент в '
                                   'последовательности. Добравшись до конца, выводит значение по умолчанию.')


def func_ord(update, context):
    send_photo_file('>>> ord("a")\n'
                    '97\n'
                    '>>> ord("A")\n'
                    '"65"\n', update.message.chat_id, context,
                    name='func_ord')
    update.message.reply_html(text='Функция <u><b>ord()</b></u> принимает один символ или строку длиной в один символ '
                                   'и возвращает соответствующее значение Unicode.')


def func_reversed(update, context):
    send_photo_file(
        ">>> x = [3,4,5]\n"
        ">>> b = reversed(x)\n"
        ">>> list(b)\n"
        "[5, 4, 3]\n", update.message.chat_id, context,
        name='func_reversed')
    update.message.reply_html(text='Эта функция предоставляет простой и быстрый способ развернуть порядок элементов в '
                                   'последовательности. В качестве параметра она принимает валидную '
                                   'последовательность, например список, а возвращает итерируемый объект.')


def func_range(update, context):
    send_photo_file(">>> list(range(10,20,2))\n"
                    "[10, 12, 14, 16, 18]\n", update.message.chat_id, context,
                    name='func_range')
    update.message.reply_html(text='Используется для создания последовательности чисел с заданными значениями от и '
                                   'до, а также интервалом. Такая последовательность часто используется в циклах, '
                                   'особенно в цикле for.')


def func_sorted(update, context):
    send_photo_file(">>> X = [4, 5, 7, 3, 1]\n"
                    ">>> sorted(X)\n"
                    "[1, 3, 4, 5, 7]\n", update.message.chat_id, context,
                    name='func_sorted')
    update.message.reply_html(text='Используется для сортировки последовательностей значений разных типов. Например, '
                                   'может отсортировать список строк в алфавитном порядке или список числовых '
                                   'значений по возрастанию или убыванию.')


def func_str(update, context):
    send_photo_file(
        ">>> str(5)\n"
        "'5'\n\n"
        ">>> X = [5,6,7]\n"
        ">>> str(X)\n"
        "'[5, 6, 7]'\n", update.message.chat_id, context,
        name='func_str')
    update.message.reply_html(text='Используется для создания строковых представлений объектов, но не меняет сам '
                                   'объект, а возвращает новый. У нее есть встроенные механизмы кодировки и обработки '
                                   'ошибок, которые помогают при конвертации.')


def func_set(update, context):
    send_photo_file(">>> set()\n"
                    "set()\n\n"
                    ">>> set('Hello')\n"
                    "{'e', 'l', 'o', 'H'}\n\n"
                    ">>> set((1,2,3,4,5))\n"
                    "{1, 2, 3, 4, 5}\n", update.message.chat_id, context,
                    name='func_set')
    update.message.reply_html(text='Функция <u><b>set()</b></u> используется для создания наборов данных, которые '
                                   'передаются в '
                                   'качестве параметра. Обычно это последовательность, например строка или список, '
                                   'которая затем преобразуется в множество уникальных значений.')


def func_sum(update, context):
    send_photo_file(">>> x = [1, 2, 5, 3, 6, 7]\n"
                    ">>> sum(x)\n"
                    "24\n", update.message.chat_id, context,
                    name='func_sum')
    update.message.reply_html(text='Вычисление суммы — стандартная задача во многих приложениях. И для этого в Python '
                                   'есть встроенная функция. Она автоматически суммирует все элементы и возвращает '
                                   'сумму.')


def func_tuple(update, context):
    send_photo_file(">>> tuple('Привет')\n"
                    "('П', 'р', 'и', 'в', 'е', 'т')\n\n"
                    ">>> tuple([1, 2, 3, 4, 5])\n"
                    "(1, 2, 3, 4, 5)\n", update.message.chat_id, context,
                    name='func_tuple')
    update.message.reply_html(text='Принимает один аргумент (итерируемый объект), которым может быть, например, '
                                   'список или словарь, последовательность или итератор и возвращает его в форме '
                                   'кортежа. Если не передать объект, то вернется пустой кортеж.')


def func_type(update, context):
    send_photo_file(">>> x = 1\n"
                    ">>> type(x)\n"
                    "<class 'int'>\n\n"
                    ">>> x = [1, 2, 3]\n"
                    ">>> type(x)\n"
                    "<class 'list'>\n\n"
                    ">>>class Foo(object):\n"
                    "...\t\tbar = True\n"
                    ">>> f = Foo()\n"
                    ">>> f.bar\n"
                    "True\n"
                    ">>> type(f)\n"
                    "<class '__main__.Foo'>\n\n\n"
                    ">>> Foo2 = type(Foo2, (), {'bar':True})\n"
                    ">>> f = Foo2()\n"
                    ">>> f.bar\n"
                    "True\n"
                    ">>> type(f)\n"
                    "<class '__main__.Foo2'>\n", update.message.chat_id, context,
                    name='func_type')
    update.message.reply_html(text='Функция <u><b>type()</b></u> применяется в двух сценариях. Если передать один '
                                   'параметр, '
                                   'то она вернет тип этого объекта. Если же передать три параметра, то можно создать'
                                   ' новый объект.')


def func_print(update, context):
    send_photo_file('''>>> print('Это предложение выводится на экран')
    Это предложение выводится на экран''', update.message.chat_id, context, name='func_print')
    update.message.reply_html(text='Функция <u><b>print()</b></u> используется для вывода данных '
                                                       'на экран. Эти данные '
                                   'мы можем записать и в файл, но об этом мы поговорим позже.\n'
                                   ' /special_print, /Special_symbols')


def special_print(update, context):
    send_photo_file('''>>> print('При')
... print('вет!')
При
вет!
>>> print('При', end='')
... print('вет!')
Привет!
>>> print('Раз', 'два', 'три')
Раз два три
>>> print('Раз', 'два', 'три', sep='--')
Раз--два--три''', update.message.chat_id, context, name='special_print')
    update.message.reply_html(text='Функция <u><b>print</b></u>, наряду с другими аргументами,'
                                   ' может (вместе или по отдельности) '
                                   'принимать два следующих аргумента: <u>sep</u> — разделитель аргументов '
                                   '(по умолчанию пробел)'
                                   ' и <u>end</u> — то, что выводится после вывода всех аргументов '
                                   '(по умолчанию символ начала новой строки).')


def Special_symbols(update, context):
    send_photo_file(r'''>>> print('восход\t07:15\nзакат\t22:03')
восход	07:15
закат	22:03
>>> print('Предыдущая строка этой программы выглядит так:')
... print('print(\'восход\\t07:15\\nзакат\\t22:03\')')
Предыдущая строка этой программы выглядит так:
print('восход\t07:15\nзакат\t22:03')
''', update.message.chat_id, context, name='Special_symbols1')
    update.message.reply_html(text='<u><b>Экранирующая последовательность</b></u>'
                                   r'Если внутри кавычек встречается символ \ — обратная косая черта, обратный слеш,'
                                   ' бэкслеш, он вместе с идущим после '
                                   'него символом образует экранирующую последовательность (escape sequence) и '
                                   'воспринимается интерпретатором как единый специальный символ. '
                                   r'В частности, \n — символ начала новой строки. Кроме того, \t — табуляция, '
                                   r'\'  — кавычка, \\ — просто бэкслеш')
    send_photo_file(r'''>>> print(r'\\\\\\\nnnnn <- забор, переходящий в низкую изгородь')
\\\\\\\nnnnn <- забор, переходящий в низкую изгородь
'''
                    ">>> print('''Нужно сказать много важного.\n"
                    "Одной строки для этого мало.\n"
                    "Зато три - в самый раз.''')\n"
                    "Нужно сказать много важного.\n"
                    "Одной строки для этого мало.\n"
                    "Зато три - в самый раз.\n", update.message.chat_id, context, name='Special_symbols2')
    update.message.reply_html(
        text='При этом если приписать букву r перед открывающей строку кавычкой, бэкслеши будут считаться обычными '
             'символами. '
             'А если открывать и закрывать строку не одной,'
             ' а тремя кавычками подряд, внутри можно делать обычные переводы строки '
             '(внутри одинарных кавычек так делать нельзя).')
