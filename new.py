def str_find(update, context):
    send_photo_file("""s = 'abracadabra'
        s.find('ab') == 0
        s.rfind('ab') == 7
        s.find('x') == -1""",
                    update.message.chat_id, context,
                    name='metod_str8')
    update.message.reply_text('s.find(s2)\ns.rfind(s2)')
    update.message.reply_html(
        text="""Индекс начала первого или последнего
        вхождения подстроки s2 в s (вернет -1, если s2 not in s""")


def str_count(update, context):
    send_photo_file("""'abracadabra'.count('a') == 5""",
                    update.message.chat_id, context,
                    name='metod_str9')
    update.message.reply_text('s.count(s2)')
    update.message.reply_html(
        text="""Количество неперекрывающихся вхождений s2 в s""")


def str_swith(update, context):
    send_photo_file("""'abracadabra'.startswith('abra')""",
                    update.message.chat_id, context,
                    name='metod_str10')
    update.message.reply_text('s.startswith(s2)\ns.endswith(s2)')
    update.message.reply_html(
        text="""Проверка, что s начинается с s2 или оканчивается на s2""")


def str_isdigit(update, context):
    send_photo_file("""'100'.isdigit()
            'abc'.isalpha()
            'E315'.isalnum()""",
                    update.message.chat_id, context,
                    name='metod_str12')
    update.message.reply_text('s.isdigit()\ns.isalpha()\ns.isalnum()')
    update.message.reply_html(
        text="""Проверка, что в строке s все символы — цифры,
            буквы (включая кириллические),
            цифры или буквы соответственно""")


def str_islower(update, context):
    send_photo_file("""'hello!'.islower()
            '123PYTHON'.isupper()""",
                    update.message.chat_id, context,
                    name='metod_str13')
    update.message.reply_text('s.islower()\ns.isupper()')
    update.message.reply_html(
        text="""Проверка, что в строке s не встречаются большие буквы, маленькие буквы.
            Обратите внимание, что для обеих этих функций знаки препинания и цифры дают True""")


def str_lower(update, context):
    send_photo_file("""'Привет!'.lower() == 'привет!'
            'Привет!'.upper() == 'ПРИВЕТ!'""",
                    update.message.chat_id, context,
                    name='metod_str14')
    update.message.reply_text('s.lower()\ns.upper()')
    update.message.reply_html(
        text="""Строка s, в которой все буквы (включая кириллические)
            приведены к верхнему или нижнему регистру,
            т. е. заменены на строчные (маленькие) или заглавные (большие)""")


def str_capitalize(update, context):
    send_photo_file("""'привет'.capitalize() == 'Привет'""",
                    update.message.chat_id, context,
                    name='metod_str15')
    update.message.reply_text('s.capitalize()')
    update.message.reply_html(
        text="""Строка s, в которой первая буква — заглавная""")


def str_lstrip(update, context):
    send_photo_file("""' Привет! '.strip() == 'Привет!'""",
                    update.message.chat_id, context,
                    name='metod_str16')
    update.message.reply_text('s.lstrip()\ns.rstrip()\ns.strip()')
    update.message.reply_html(
        text="""Строка s, у которой удалены символы пустого пространства
            (пробелы, табуляции) в начале,
            в конце или с обеих сторон""")


def str_ljust(update, context):
    send_photo_file("""'Привет'.ljust(8, '!') == 'Привет!!'""",
                    update.message.chat_id, context,
                    name='metod_str17')
    update.message.reply_text('s.ljust(k, c)\ns.rjust(k, c)')
    update.message.reply_html(
        text="""Добавляет справа или слева нужное количество
            символов c, чтобы длина s достигла k""")


def str_join(update, context):
    send_photo_file("""'+'.join(['Вася', 'Маша']) == 'Вася+Маша'""",
                    update.message.chat_id, context,
                    name='metod_str18')
    update.message.reply_text('s.join(a)')
    update.message.reply_html(
        text="""Склеивает строки из списка a через символ s""")


def str_split(update, context):
    send_photo_file("""'Раз два три!'.split('а') ==
            ['Р', 'з дв', ' три!']""",
                    update.message.chat_id, context,
                    name='metod_str19')
    update.message.reply_text('s.split(s2)')
    update.message.reply_html(
        text="""Список всех слов строки s
            (подстрок, разделенных строками s2)""")


def str_replace(update, context):
    send_photo_file("""'Раз два три!'.replace('а', 'я') =='Ряз двя три!'
        'Раз два три!'.replace('а', 'я', 1) == 'Ряз два три!'""",
                    update.message.chat_id, context,
                    name='metod_str20')
    update.message.reply_text('s.replace(s2, s3)')
    update.message.reply_html(
        text="""Cтрока s, в которой все неперекрывающиеся
        вхождения s2 заменены на s3
        Есть необязательный третий параметр, с помощью которого можно указать, сколько раз производить замену""")