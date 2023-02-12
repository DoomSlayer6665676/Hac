from CONST import *


def add_data_handler():
    dp.add_handler(CommandHandler("dat_now", dat_now))
    dp.add_handler(CommandHandler("dat_date", dat_date))
    dp.add_handler(CommandHandler("dat_time", dat_time))
    dp.add_handler(CommandHandler("dat_timedelta", dat_timedelta))
    dp.add_handler(CommandHandler("dat_mat", dat_mat))
    dp.add_handler(CommandHandler("dat_strptime", dat_strptime))
    dp.add_handler(CommandHandler("dat_strftime", dat_strftime))


def dat_now(update, context):
    send_photo_file( 'import datetime\n'
'dt_now = datetime.datetime.now()\n'
'print(dt_now)\n'
'#Вывод: 2023-02-10 21:44:32.249588\n' , update.message.chat_id, context, name='dat_now')
    update.message.reply_html(text='')


def dat_date(update, context):
    send_photo_file( 'from datetime import date\n'

'current_date = date.today()\n'
'print(current_date)\n'
'#Вывод: 2023-02-10' , update.message.chat_id, context, name='dat_date')
    update.message.reply_html(text='Класс date можно использовать для получения или изменения объектов даты. Например, для получения текущей с учетом настроек подойдет следующее:')


def dat_time(update, context):
    send_photo_file( 'current_date_time = datetime.datetime.now()\n'
'current_time = current_date_time.time()\n'
'print(current_time)\n'
'#Вывод: 21:44:32.249588' , update.message.chat_id, context, name='dat_time')
    update.message.reply_html(text='Для получения текущего локального времени сперва нужно получить текущие дату и время, а затем достать из этого объекта только время с помощью метода time():')


def dat_timedelta(update, context):
    send_photo_file( 'td_object =timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)\n'
'td_object\n'
'datetime.timedelta(0)\n' , update.message.chat_id, context, name='dat_timedelta')
    update.message.reply_html(text='timedelta представляет длительность (даты или времени). Модуль datetime включает атрибут timedelta(), который используется для управления датой в Python.\n' 
        'Объект timedelta выглядит следующим образом:\n'
        'Все аргументы опциональные и их значения по умолчанию равно 0. Они могут быть целыми или числами с плавающей точкой, как положительными, так и отрицательными.' 
        'Благодаря этому можно выполнять математические операции, такие как сложение, вычитание и умножение.')


def dat_mat(update, context):
    send_photo_file( 'first_date = date(2023, 10, 2)\n'
'second_date = date(2023, 10, 30)\n'
'delta = second_date - first_date\n'
'print(delta)\n'
'#Вывод: 28 days,0:00:00' , update.message.chat_id, context, name='dat_mat')
    update.message.reply_html(text='В качестве примера возьмем вычитание. Для получения разницы нужно лишь вычесть значение одного объекта из второго:')


def dat_strptime(update, context):
    send_photo_file( 'datetime_string = "02/12/23 12:48:03"\n'
"datetime_obj = datetime.strptime(datetime_string, '%m/%d/%y %H:%M:%S')\n"
"print(datetime_obj)\n"
'#Вывод: 2023-02-12 12:48:03\n', update.message.chat_id, context, name='dat_strptime')
    update.message.reply_html(text='Предположим, что есть следующая строка с датой: «02/12/23 12:48:03», и ее нужно конвертировать в объект datetime.')


def dat_strftime(update, context):
    send_photo_file( 'current_date = datetime.datetime.now()\n'
"current_date_string = current_date.strftime('%m/%d/%y %H:%M:%S')\n"
'print(current_date_string)\n'
'Результат — 12/02/23 12:54:36' , update.message.chat_id, context, name='dat_strftime')
    update.message.reply_html(text='Предположим, нужно конвертировать текущий объект datetime в строку.\n'
                                   'Сначала нужно получить представление объекта datetime и вызвать на нем метод strftime().')
