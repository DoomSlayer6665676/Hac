from functions import *


def echo(update, context):
    update.message.reply_text('Извините, я вас не понимаю.\nДля выбора команд воспользуйтесь меню справа от ввода.')


def start(update, context):
    update.message.reply_text(
        'Привет! Я справочник по языку Python.\n /help', reply_markup=markup)
    return


def help(update, context):
    update.message.reply_text('Вот, что я умею:\n' + '\n'.join([j + exp[ind1][ind2] for ind1, i in enumerate(board)
                                                                for ind2, j in enumerate(i)]))
    return


def themes(update, context):
    update.message.reply_text('Темы:\n'
                              '/func - встроенные функции\n')


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
    update.message.reply_text('/func_abs - абсолютное значение числа\n'
                              '/func_chr - перевод Unicode в строку\n'
                              '/func_callable - является ли объект вызываемым\n'
                              '/func_dict - создание словарей\n'
                              '/func_dir - выводит список вех атрибутов и методов объекта\n'
                              '/func_enumerate - нумерует последовательность\n'
                              '/func_eval - обработка математических выражений\n'
                              '/func_filter - фильтрует итерируемые объекты\n'
                              '/func_float - создаёт число с плавающей точкой\n'
                              '/func_input - ввод данных\n'
                              '/func_int - создаёт целое число\n'
                              '/func_iter - привращает объект в итерируемый\n'
                              '/func_max - максимальное значение последовательности\n'
                              '/func_min - минимальное значение последовательности\n'
                              '/func_len - длинна последовательности\n'
                              '/func_list - создание списков\n'
                              '/func_map - применение функций к итерируемому объекту\n'
                              '/func_next - перебирает итерируемые объекты\n'
                              '/func_ord - перевод строки в Unicode\n'
                              '/func_reversed - разворачивает последовательность\n'
                              '/func_range - создания последовательности с заданными значениями\n'
                              '/func_sorted - сортирует последовательность\n'
                              '/func_str - создание строки\n'
                              '/func_set - создание множества\n'
                              '/func_sum - суммирует все элементы множества\n'
                              '/func_tuple - создание кортежей\n'
                              '/func_type - возвращает тип объекта либо создает объект type')


def main():
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("themes", themes))
    dp.add_handler(CommandHandler("bugs", bugs))
    dp.add_handler(CommandHandler("techsupport", techsupport))
    dp.add_handler(CommandHandler("DONATE", DONATE))
    dp.add_handler(CommandHandler("stop", stop))
    dp.add_handler(CommandHandler("func", func))
    add_function_handler()
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
