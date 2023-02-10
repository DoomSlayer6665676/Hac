from CONST import *


def add_mat_handler():
    dp.add_handler(CommandHandler("math_seil", math_seil))
    dp.add_handler(CommandHandler("math_fabs", math_fabs))
    dp.add_handler(CommandHandler("math_factorial", math_factorial))
    dp.add_handler(CommandHandler("math_floor", math_floor))
    dp.add_handler(CommandHandler("math_isfinite", math_isfinite))
    dp.add_handler(CommandHandler("math_isinf", math_isinf))
    dp.add_handler(CommandHandler("math_isnan", math_isnan))
    dp.add_handler(CommandHandler("math_sqrt", math_sqrt))
    dp.add_handler(CommandHandler("math_acos", math_acos))
    dp.add_handler(CommandHandler("math_asin", math_asin))
    dp.add_handler(CommandHandler("math_atan", math_atan))
    dp.add_handler(CommandHandler("math_cos", math_cos))
    dp.add_handler(CommandHandler("math_sin", math_sin))
    dp.add_handler(CommandHandler("math_tan", math_tan))
    dp.add_handler(CommandHandler("math_degrees", math_degrees))
    dp.add_handler(CommandHandler("math_radians", math_radians))






'''
def math(update, context):
    update.message.reply_html("""Модуль math – один из наиважнейших в Python. Этот модуль предоставляет обширный функционал для работы с числами.
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
    """)
'''



def math_seil(update, context):
    send_photo_file( 'x = math.seil(9.76)\n'
        'print(x)\n'
        '# Вывод: 10\n' , update.message.chat_id, context, name='math_seil')
    update.message.reply_html(text='Возвращает максимум от x , наименьшее целое число, большее или равное x. '
        'Если x не является числом с плавающей запятой, делегируется <u><b>x.__ceil__</b></u>, '
        'который должен возвращать <b>Integral</b> значение.')

def math_fabs(update, context):
    send_photo_file( 'x = math_fabs(-5)\n'

        'print(x)\n'
        '# Вывод: 5\n', update.message.chat_id, context, name='math_fabs')
    update.message.reply_html(text='Возвращает модуль числа, т.е. его абсолютное значение без знака.')

def math_factorial(update, context):
    send_photo_file( 'x = math.factorial(3)\n'
        'print(x)\n'
        '#Вывод: 6\n' , update.message.chat_id, context, name='math_factorial')
    update.message.reply_html(text='Возвращает факториал n как целое число. Выдает ValueError, если n не является целым или отрицательным.\n'
                        '<u><b>Важно:</u></b> с версии 3.9(самого math, не Python) не принимает дробные числа с целым значением(пример: 5.0)')

def math_floor(update, context):
    send_photo_file( 'x = math.seil(9.76)\n'
        'print(x)\n'
        '# Вывод: 9\n' , update.message.chat_id, context, name='math_floor')
    update.message.reply_html(text='Возвращает минимум от x , наибольшее целое число, меньшее или равное x.'
                                   'Если x не является числом с плавающей запятой, делегируется <u><b>x.__floor__</b></u>, который должен возвращать <b>Integral</b> значение.')

def math_isfinite(update, context):
    send_photo_file('x = math.isfinite("qwe")\n'
        'print(x)\n'
        '#Вывод: False\n' , update.message.chat_id, context, name='math_isfinite')
    update.message.reply_html(text='Возвращает <b>True</b>, если x не является ни бесконечностью, ни NaN, и в <b>False</b> противном случае. (Обратите внимание, что 0.0 считается конечным.) ')

def math_isinf(update, context):
    send_photo_file( 'x = math.isinf(10)\n'
        'print(x)\n'
        '#Вывод: False\n' , update.message.chat_id, context, name='math_isinf')
    update.message.reply_html(text='Возврат <b>True</b>, если x является положительной или отрицательной бесконечностью, и в <b>False</b> противном случае.')

def math_isnan(update, context):
    send_photo_file( 'x = math.isnan("qwerty")\n'
        'print(x)\n'
        '#Вывод: True\n' , update.message.chat_id, context, name='math_isnan')
    update.message.reply_html(text='Возврат <b>True<b>, если x является NaN (не числом), и в <b>False</b> противном случае.')

def math_sqrt(update, context):
    send_photo_file('x = math.sqrt(4)\n'
        'print(x)\n'
        '#Вывод: 2\n' , update.message.chat_id, context, name='math_sqrt')
    update.message.reply_html(text='')

def math_acos(update, context):
    send_photo_file('x = math.acos(1)\n'
        'print(x)\n'
        '#Вывод: 0.0\n' , update.message.chat_id, context, name='math_acos')
    update.message.reply_html(text='Возвращает арккосинус x в радианах. Результат между 0 и 𝝅.')

def math_asin(update, context):
    send_photo_file('x = math.asin(0)\n'
        'print(x)\n'
        '#Вывод: 0.0\n' , update.message.chat_id, context, name='math_asin')
    update.message.reply_html(text='Возвращает арксинус x в радианах. Результат между -𝝅/2 и 𝝅/2.')

def math_atan(update, context):
    send_photo_file('x = math.atan(0)\n'
        'print(x)\n'
        '#Вывод: 0.0\n' , update.message.chat_id, context, name='math_atan')
    update.message.reply_html(text='Возвращает арктангенс x в радианах. Результат между -𝝅/2 и 𝝅/2.')

def math_cos(update, context):
    send_photo_file('x = math.cos(30)\n'
        'print(x)\n'
        '#Вывод: ~0.15\n' , update.message.chat_id, context, name='math_cos')
    update.message.reply_html(text='Возвращает косинус x радиан.')

def math_sin(update, context):
    send_photo_file('x = math.sin(30)\n'
        'print(x)\n'
        '#Вывод: ~-0.98\n' , update.message.chat_id, context, name='math_sin')
    update.message.reply_html(text='Возвращает синус x радиан.')

def math_tan(update, context):
    send_photo_file('x = math.tan(30)\n'
        'print(x)\n'
        '#Вывод: ~-6.4\n' , update.message.chat_id, context, name='math_tan')
    update.message.reply_html(text='Возвращает тангенс x радиан.')

def math_degrees(update, context):
    send_photo_file('x = math.degrees(0.5)\n'
        'print(x)\n'
        '#Вывод: ~28\n' , update.message.chat_id, context, name='math_degrees')
    update.message.reply_html(text='Преобразование угла x из радианов в градусы.')

def math_radians(update, context):
    send_photo_file('x = math.radians(30)\n'
        'print(x)\n'
        '#Вывод: ~0.5\n', update.message.chat_id, context, name='math_radians')
    update.message.reply_html(text='Преобразование угла x из градусов в радианы.')