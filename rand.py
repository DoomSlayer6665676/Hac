from CONST import *


def add_random_handler():
    dp.add_handler(CommandHandler("rand_random", rand_random))
    dp.add_handler(CommandHandler("rand_seed", rand_seed))
    dp.add_handler(CommandHandler("rand_uniform", rand_uniform))
    dp.add_handler(CommandHandler("rand_randint", rand_randint))
    dp.add_handler(CommandHandler("rand_choince", rand_choince))
    dp.add_handler(CommandHandler("rand_randrange", rand_randrange))
    dp.add_handler(CommandHandler("rand_shuffle", rand_shuffle))


def rand_random(update, context):
    send_photo_file("""random.random()
0.07500815468466127""",
                    update.message.chat_id, context,
                    name='rand_random')
    update.message.reply_html(
        text="""<u><b>random.random()</b></u> — возвращает псевдослучайное число от 0.0 до 1.0""")


def rand_seed(update, context):
    send_photo_file("""random.seed(20)
random.random()
0.9056396761745207

random.random()
0.6862541570267026

random.seed(20)
random.random()
0.9056396761745207

random.random()
0.7665092563626442""",
                    update.message.chat_id, context,
                    name='rand_seed')
    update.message.reply_html(
        text="""<u><b>random.seed([Параметр])</b></u> — настраивает генератор случайных чисел на новую последовательность. По умолчанию используется системное время. Если значение параметра будет одиноким, то генерируется одинокое число""")


def rand_uniform(update, context):
    send_photo_file("""random.uniform(0, 20)
15.330185127252884

random.uniform(0, 20)
18.092324756265473""",
                    update.message.chat_id, context,
                    name='rand_uniform')
    update.message.reply_html(
        text="""<u><b>random.uniform([Начало], [Конец])</b></u> — возвращает псевдослучайное вещественное число в диапазоне от [Начало] до [Конец]""")


def rand_randint(update, context):
    send_photo_file("""random.randint(1,27)
9
random.randint(1,27)
22""",
                    update.message.chat_id, context,
                    name='rand_randint')
    update.message.reply_html(
        text="""<u><b>random.randint([Начало], [Конец])</b></u> — возвращает псевдослучайное целое число в диапазоне от [Начало] до [Конец]""")


def rand_choince(update, context):
    send_photo_file("""random.choice('Chewbacca')
'h'
random.choice([1,2,'a','b'])
2
random.choice([1,2,'a','b'])
'a'""",
                    update.message.chat_id, context,
                    name='rand_choince')
    update.message.reply_html(
        text="""<u><b>random.choince([Последовательность])</b></u> — возвращает случайный элемент из любой последовательности (строки, списка, кортежа)""")


def rand_randrange(update, context):
    update.message.reply_html(
        text="""<u><b>random.randrange([Начало], [Конец], [Шаг])</b></u> — возвращает случайно выбранное число из последовательности range.""")


def rand_shuffle(update, context):
    send_photo_file("""List = [1,2,3,4,5,6,7,8,9]
List
[1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(List)
List
[6, 7, 1, 9, 5, 8, 3, 2, 4]""",
                    update.message.chat_id, context,
                    name='rand_shuffle')
    update.message.reply_html(
        text="""<u><b>random.shuffle([Список])</b></u> — перемешивает последовательность (изменяется сама последовательность). Поэтому функция не работает для неизменяемых объектов""")
