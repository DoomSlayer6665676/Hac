from CONST import *


def add_data_handler():
    dp.add_handler(CommandHandler("dat_now", dat_now))
    dp.add_handler(CommandHandler("dat_date", dat_date))
    dp.add_handler(CommandHandler("dat_time", dat_time))
    '''
    dp.add_handler(CommandHandler("lam_map", lam_map))
    dp.add_handler(CommandHandler("lam_fil", lam_fil))
    dp.add_handler(CommandHandler("lam_sort", lam_sort))
    dp.add_handler(CommandHandler("math_isnan", math_isnan))
    dp.add_handler(CommandHandler("math_sqrt", math_sqrt))
    dp.add_handler(CommandHandler("math_acos", math_acos))
    '''




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
'''
def dat_now(update, context):
    send_photo_file( '' , update.message.chat_id, context, name='dat_now')
    update.message.reply_html(text='')

def dat_now(update, context):
    send_photo_file( '' , update.message.chat_id, context, name='dat_now')
    update.message.reply_html(text='')

def dat_now(update, context):
    send_photo_file( '' , update.message.chat_id, context, name='dat_now')
    update.message.reply_html(text='')

def dat_now(update, context):
    send_photo_file( '' , update.message.chat_id, context, name='dat_now')
    update.message.reply_html(text='')
'''