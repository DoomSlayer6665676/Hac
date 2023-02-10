from CONST import *


def add_lam_handler():
    dp.add_handler(CommandHandler("lam_1arg", lam_1arg))
    dp.add_handler(CommandHandler("lam_narg", lam_narg))
    dp.add_handler(CommandHandler("lam_farg", lam_farg))
    dp.add_handler(CommandHandler("lam_map", lam_map))
    dp.add_handler(CommandHandler("lam_fil", lam_fil))
    dp.add_handler(CommandHandler("lam_sort", lam_sort))


def lam_1arg(update, context):
    send_photo_file( '>>> f = lambda x: x * x\n'
'>>> f(5)\n'
'#Вывод: 25\n' , update.message.chat_id, context, name='lam_1arg')
    update.message.reply_html(text='')


def lam_narg(update, context):
    send_photo_file( '>>> f = lambda x, y: x * y\n'
'>>> f(5, 2)\n'
'#Вывод: 10\n' , update.message.chat_id, context, name='lam_narg')
    update.message.reply_html(text='Предположим, что нужна функция, которая берет два числовых аргумента и возвращает их произведение.')


def lam_farg(update, context):
    send_photo_file( '>>> f = lambda: True\n'
'>>> f()\n'
'True\n' , update.message.chat_id, context, name='lam_farg')
    update.message.reply_html(text='Этого можно добиться с помощью следующего кода.')


def lam_map(update, context):
    send_photo_file( '>>> L = [1, 2, 3, 4]\n'
'>>> list(map(lambda x: x**2, L))\n'
'[1, 4, 9, 16]\n' , update.message.chat_id, context, name='lam_map')
    update.message.reply_html(text='Предположим, есть список целых чисел, которые нужно возвести в квадрат с помощью map.\n'
                                   'Обратите внимание на то, что в Python3 функция map возвращает объект Map, а в Python2 — список.\n'
                                   'Так, вместо определения функции и передачи ее в map в качестве аргумента, можно просто использовать лямбда для быстрого определения ее прямо внутри.' 
                                   'В этом есть смысл, если упомянутая функция больше не будет использоваться в коде.')


def lam_fil(update, context):
    send_photo_file( 'def even_fn(x):\n'
  'if x % 2 == 0:\n'
    'return True\n'
  'return False\n'

'print(list(filter(even_fn, [1, 3, 2, 5, 20, 21])))\n'

'#вывод: [2, 20]\n'
'###############################################################\n'
'print(list(filter(lambda x: x % 2 == 0, [1, 3, 2, 5, 20, 21])))\n' , update.message.chat_id, context, name='lam_fil')
    update.message.reply_html(text='Если возвращаемое значение — True, элемент остается. В противном случае — отклоняется.\n' 
        'Определим, например, простую функцию, которая возвращает True для четных чисел и False — для нечетных:\n'
        'С лямбда-функциями это все можно сделать максимально сжато. Код выше можно преобразовать в такой, написанный в одну строку.')


def lam_sort(update, context):
    send_photo_file( '#1\n'
    'class Employee:\n'
    'def __init__(self, name, age):\n'
        'self.name = name\n'
        'self.age = age\n'
'#2\n'
"Alex = Employee('Alex', 20)\n"
"Amanda = Employee('Amanda', 30)\n"
"David = Employee('David', 15)\n"
'L = [Alex, Amanda, David]\n'
'#3\n'
'L.sort(key=lambda x: x.age)\n'
'print([item.name for item in L])\n'
"# вывод: ['David', 'Alex', 'Amanda']\n" , update.message.chat_id, context, name='lam_sort')
    update.message.reply_html(text=' Рассмотрим пример. Есть класс Employee.(1)\n'
                                   'Теперь создадим экземпляры этого класса и добавим их в список.(2)\n'
                                   'Предположим, что мы хотим отсортировать его на основе поля age сотрудников. Вот что нужно сделать для этого:(3)\n'
                                   'Лямбда-выражение было использовано в качестве параметра key вместо отдельного ее определения и затем передачи в функцию sort.')

