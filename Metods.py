from CONST import *


def add_metods_handler():
    dp.add_handler(CommandHandler("list_in", list_in))
    dp.add_handler(CommandHandler("list_not_in", list_not_in))
    dp.add_handler(CommandHandler("list_summa", list_summa))
    dp.add_handler(CommandHandler("list_summa", list_summa))
    dp.add_handler(CommandHandler("list_ind", list_ind))
    dp.add_handler(CommandHandler("list_slice", list_slice))
    dp.add_handler(CommandHandler("list_len", list_len))
    dp.add_handler(CommandHandler("list_max", list_max))
    dp.add_handler(CommandHandler("list_min", list_min))
    dp.add_handler(CommandHandler("list_sum", list_sum))
    dp.add_handler(CommandHandler("list_del", list_del))
    dp.add_handler(CommandHandler("list_sumpl", list_sumpl))
    dp.add_handler(CommandHandler("list_bool", list_bool))
    dp.add_handler(CommandHandler("operations_list", operations_list))
    dp.add_handler(CommandHandler("list_index", list_index))
    dp.add_handler(CommandHandler("list_count", list_count))
    dp.add_handler(CommandHandler("list_append", list_append))
    dp.add_handler(CommandHandler("list_extend", list_extend))
    dp.add_handler(CommandHandler("list_insert", list_insert))
    dp.add_handler(CommandHandler("list_pop", list_pop))
    dp.add_handler(CommandHandler("list_remove", list_remove))
    dp.add_handler(CommandHandler("list_reverse", list_reverse))
    dp.add_handler(CommandHandler("list_sort", list_sort))
    dp.add_handler(CommandHandler("list_sortr", list_sortr))
    dp.add_handler(CommandHandler("list_clear", list_clear))
    dp.add_handler(CommandHandler("list_copy", list_copy))
    dp.add_handler(CommandHandler("methods_list", methods_list))
    dp.add_handler(CommandHandler("str_in", str_in))
    dp.add_handler(CommandHandler("str_not_in", str_not_in))
    dp.add_handler(CommandHandler("str_summa", str_summa))
    dp.add_handler(CommandHandler("str_multiply", str_multiply))
    dp.add_handler(CommandHandler("str_ind", str_ind))
    dp.add_handler(CommandHandler("str_slice", str_slice))
    dp.add_handler(CommandHandler("str_len", str_len))
    dp.add_handler(CommandHandler("str_summpl", str_summpl))
    dp.add_handler(CommandHandler("str_list", str_list))
    dp.add_handler(CommandHandler("str_bool", str_bool))
    dp.add_handler(CommandHandler("str_int", str_int))
    dp.add_handler(CommandHandler("str_str", str_str))
    dp.add_handler(CommandHandler("operations_str", operations_str))
    dp.add_handler(CommandHandler("str_find", str_find))
    dp.add_handler(CommandHandler("str_count", str_count))
    dp.add_handler(CommandHandler("str_swith", str_swith))
    dp.add_handler(CommandHandler("str_isdigit", str_isdigit))
    dp.add_handler(CommandHandler("str_islower", str_islower))
    dp.add_handler(CommandHandler("str_lower", str_lower))
    dp.add_handler(CommandHandler("str_capitalize", str_capitalize))
    dp.add_handler(CommandHandler("str_lstrip", str_lstrip))
    dp.add_handler(CommandHandler("str_ljust", str_ljust))
    dp.add_handler(CommandHandler("str_join", str_join))
    dp.add_handler(CommandHandler("str_split", str_split))
    dp.add_handler(CommandHandler("str_replace", str_replace))
    dp.add_handler(CommandHandler("methods_str", methods_str))


def list_in(update, context):
    send_photo_file("""5 in [2, 3, 5]""",
                    update.message.chat_id, context,
                    name='metod_list1')
    update.message.reply_text('x in a')
    update.message.reply_html(
        text="""Проверка, что x содержится в а""")


def list_not_in(update, context):
    send_photo_file("""5 not in [2, 3, 6]""",
                    update.message.chat_id, context,
                    name='metod_list2')
    update.message.reply_text('x not in a')
    update.message.reply_html(
        text="""Проверка, что x не содержится в а
    То же, что и not (x in a)""")


def list_summa(update, context):
    send_photo_file("""[2, 4] + [5, 3] == [2, 4, 5, 3]""",
                    update.message.chat_id, context,
                    name='metod_list3')
    update.message.reply_text('a + a2')
    update.message.reply_html(
        text="""Конкатенация списков, то есть новый список, в котором сначала идут все элементы a,
    а затем все элементы a2""")


def list_multiply(update, context):
    send_photo_file("""[2, 3] * 3 == [2, 3, 2, 3, 2, 3]""",
                    update.message.chat_id, context,
                    name='metod_list4')
    update.message.reply_text('a * k')
    update.message.reply_html(
        text="""Список a, повторенный k раз""")


def list_ind(update, context):
    send_photo_file("""[2, 3, 7][0] == 2
    [2, 3, 7][-1] == 7""",
                    update.message.chat_id, context,
                    name='metod_list5')
    update.message.reply_text('a[n]')
    update.message.reply_html(
        text="""n-й элемент списка,
    отрицательные n — для отсчета с конца""")


def list_slice(update, context):
    send_photo_file("""[2, 3, 7][:2] == [2, 3]""",
                    update.message.chat_id, context,
                    name='metod_list6')
    update.message.reply_text('a[start:stop:step]')
    update.message.reply_html(
        text="""Срез списка""")


def list_len(update, context):
    send_photo_file("""len([2, 3, 7]) == 3""",
                    update.message.chat_id, context,
                    name='metod_list7')
    update.message.reply_text('len(a)')
    update.message.reply_html(
        text="""Длина списка""")


def list_max(update, context):
    send_photo_file("""max([2, 3, 7]) == 7""",
                    update.message.chat_id, context,
                    name='metod_list8')
    update.message.reply_text('max(a)')
    update.message.reply_html(
        text="""Максимальный элемент списка""")


def list_min(update, context):
    send_photo_file("""min([2, 3, 7]) == 2""",
                    update.message.chat_id, context,
                    name='metod_list9')
    update.message.reply_text('min(a)')
    update.message.reply_html(
        text="""Минимальный элемент списка""")


def list_sum(update, context):
    send_photo_file("""sum([2, 3, 7]) == 12""",
                    update.message.chat_id, context,
                    name='metod_list10')
    update.message.reply_text('sum(a)')
    update.message.reply_html(
        text="""Сумма элементов списка""")


def list_del(update, context):
    send_photo_file("""a = [2, 3, 7]
    del a[1]
    a == [2, 7]""",
                    update.message.chat_id, context,
                    name='metod_list15')
    update.message.reply_text('del a[n]')
    update.message.reply_html(
        text="""Удалить n-й элемент списка""")
    send_photo_file("""a = [2, 3, 7]
    del a[:2]
    a == [7]""",
                    update.message.chat_id, context,
                    name='metod_list16')
    update.message.reply_text('del a[start:stop:step]')
    update.message.reply_html(
        text="""Удалить из a все элементы, попавшие в срез""")


def list_sumpl(update, context):
    send_photo_file("""a = [1]
    a *= 2
    a == [1, 1]
    a += [2]
    a == [1, 1, 2]""",
                    update.message.chat_id, context,
                    name='metod_list19')
    update.message.reply_text("""'a += a2\na *= k'""")
    update.message.reply_text("""Заменить содержимое списка на a + a2
    и a * k соответственно""")


def list_bool(update, context):
    send_photo_file("""bool([]) == False
    bool([1]) == True""",
                    update.message.chat_id, context,
                    name='metod_list26')
    update.message.reply_text('bool(a)')
    update.message.reply_text("""Один из способов проверить список на пустоту (возвращает True, если список 
        непустой, и False в противном случае)""")


def operations_list(update, context):
    update.message.reply_html(
        text="""Операции над списками:
        x <b>in</b> a - /list_in
        x <b>not in</b> a - /list_not_in
        a <b>+</b> a2 - /list_summa
        a <b>*</b> k - /list_multiply
        a<b>[n]</b> - /list_ind
        a<b>[start:stop:step]</b> - /list_slice
        <b>len(a)</b> - /list_len
        <b>max(a)</b> - /list_max
        <b>min(a)</b> - /list_min
        <b>sum(a)</b> - /list_sum
        <b>del</b> a[n] - /list_del
        a <b>+=</b> a2 - /list_sumpl
        <b>bool(a)</b> - /list_bool""", reply_markup=create_markup([['/listi', '/operations_list']]))


def list_index(update, context):
    send_photo_file("""[2, 3, 7].index(7) == 2""",
                    update.message.chat_id, context,
                    name='metod_list11')
    update.message.reply_text('a.index(x)')
    update.message.reply_html(
        text="""Индекс первого вхождения x в a
        (вызовет ошибку, если x not in a, то есть если х отсутствует в а)""")


def list_count(update, context):
    send_photo_file("""[2, 7, 3, 7].count(7) == 2""",
                    update.message.chat_id, context,
                    name='metod_list12')
    update.message.reply_text('a.count(x)')
    update.message.reply_html(
        text="""Количество вхождений x в a""")


def list_append(update, context):
    send_photo_file("""a = [2, 3, 7]
        a.append(8)
        a == [2, 3, 7, 8]""",
                    update.message.chat_id, context,
                    name='metod_list13')
    update.message.reply_text('a.append(x)')
    update.message.reply_html(
        text="""Добавить x в конец a""")


def list_extend(update, context):
    send_photo_file("""a = [2, 3, 7]
        a.extend([8, 4, 5])
        a == [2, 3, 7, 8, 4, 5]""",
                    update.message.chat_id, context,
                    name='metod_list14')
    update.message.reply_text('a.extend(a2)')
    update.message.reply_html(
        text="""Добавить элементы коллекции a2 в конец a""")


def list_insert(update, context):
    send_photo_file("""a = [2, 3, 7]
        a.insert(0, 8)
        a == [8, 2, 3, 7]""",
                    update.message.chat_id, context,
                    name='metod_list20')
    update.message.reply_text('a.insert(n, x)')
    update.message.reply_html(
        text="""	Вставить x в a на позицию n, подвинув последующую часть дальше""")


def list_pop(update, context):
    send_photo_file("""a = [2, 3, 7]
        a.pop(1) == 3
        a == [2, 7]""",
                    update.message.chat_id, context,
                    name='metod_list21')
    update.message.reply_text('a.pop(n)')
    update.message.reply_html(
        text="""Получить n-й элемент списка и одновременно удалить его из списка.
        Вызов метода без аргументов равносилен удалению последнего элемента:
        a.pop() == a.pop(-1)""")


def list_remove(update, context):
    send_photo_file("""a = [2, 3, 7]
        a.remove(3)
        a == [2, 7]""",
                    update.message.chat_id, context,
                    name='metod_list22')
    update.message.reply_text('a.remove(x)')
    update.message.reply_html(
        text="""Удалить первое вхождение x в a, в случае x not in a — ошибка""")


def list_reverse(update, context):
    send_photo_file("""a = [2, 3, 7]
        a.reverse()
        a == [7, 3, 2]""",
                    update.message.chat_id, context,
                    name='metod_list23')
    update.message.reply_text('a.reverse()')
    update.message.reply_html(
        text="""Изменить порядок элементов в a на обратный (перевернуть список)""")


def list_sort(update, context):
    send_photo_file("""a = [3, 2, 7]
        a.sort()
        a == [2, 3, 7]""",
                    update.message.chat_id, context,
                    name='metod_list24')
    update.message.reply_text('a.sort()')
    update.message.reply_html(
        text="""Отсортировать список по возрастанию""")


def list_sortr(update, context):
    send_photo_file("""a = [3, 2, 7]
        a.sort(reverse = True)
        a == [7, 3, 2]""",
                    update.message.chat_id, context,
                    name='metod_list25')
    update.message.reply_text('a.sort(reverse=True)')
    update.message.reply_html(
        text="""Отсортировать список по убыванию""")


def list_clear(update, context):
    send_photo_file("""a.clear()""",
                    update.message.chat_id, context,
                    name='metod_list17')
    update.message.reply_text('a.clear()')
    update.message.reply_html(
        text="""Удалить из a все элементы (то же, что del a[:])""")


def list_copy(update, context):
    send_photo_file("""b = a.copy()""",
                    update.message.chat_id, context,
                    name='metod_list18')
    update.message.reply_text('a.copy()')
    update.message.reply_html(
        text="""Копия a (то же, что и полный срез a[:])""")


def methods_list(update, context):
    update.message.reply_html(text="""Методы списков:
    <b>a.index(x)</b> - /list_index
    <b>a.count(x)</b> - /list_count
    <b>a.append(x)</b> - /list_append
    <b>a.extend(a2)</b> - /list_extend
    <b>a.insert(n, x)</b> - /list_insert
    <b>a.pop(n)</b> - /list_pop
    <b>a.remove(x)</b> - /list_remove
    <b>a.reverse()</b> - /list_reverse
    <b>a.sort()</b> - /list_sort
    <b>a.sort(reverse=True)</b> - /list_sortr
    <b>a.clear()</b> - /list_clear
    <b>a.copy()</b> - /list_copy""", reply_markup=create_markup([['/listi', '/methods_list']]))


def str_in(update, context):
    send_photo_file("""'m' in 'team'""",
                    update.message.chat_id, context,
                    name='metod_str1')
    update.message.reply_text('s2 in s')
    update.message.reply_html(
        text="""Проверка, что подстрока s2 содержится в s""")


def str_not_in(update, context):
    send_photo_file("""'I' not in 'team'""",
                    update.message.chat_id, context,
                    name='metod_str2')
    update.message.reply_text('s2 not in s')
    update.message.reply_html(
        text="""Проверка, что подстрока s2 не содержится в s
    то же, что not (s2 in s)""")


def str_summa(update, context):
    send_photo_file("""'tea' + 'm' == 'team'""",
                    update.message.chat_id, context,
                    name='metod_str3')
    update.message.reply_text('s + s2')
    update.message.reply_html(
        text="""	Конкатенация (склейка) строк, то есть строка,
    в которой сначала идут все символы из s,
    а затем все символы из s2""")


def str_multiply(update, context):
    send_photo_file("""'ha' * 3 == 'hahaha'""",
                    update.message.chat_id, context,
                    name='metod_str4')
    update.message.reply_text('s * k')
    update.message.reply_html(
        text="""Строка s, повторенная k раз""")


def str_ind(update, context):
    send_photo_file("""'team'[2] == 'a'
    'team'[-1] == 'm'""",
                    update.message.chat_id, context,
                    name='metod_str5')
    update.message.reply_text('s[n]')
    update.message.reply_html(
        text="""n-й элемент строки,
    отрицательные n — для отсчета с конца""")


def str_slice(update, context):
    send_photo_file("""'mama'[:2] == 'ma'""",
                    update.message.chat_id, context,
                    name='metod_str6')
    update.message.reply_text('s[start:stop:step]')
    update.message.reply_html(
        text="""Срез строки""")


def str_len(update, context):
    send_photo_file("""len('abracadabra') == 11""",
                    update.message.chat_id, context,
                    name='metod_str7')
    update.message.reply_text('len(s)')
    update.message.reply_html(
        text="""Длина строки""")


def str_summpl(update, context):
    send_photo_file("""Заменить содержимое строки на
    s + s2 и s * k соответственно""",
                    update.message.chat_id, context,
                    name='metod_str11')
    update.message.reply_text('s += s2\ns *= k')


def str_list(update, context):
    send_photo_file("""list('Привет') ==
    ['П', 'р', 'и', 'в', 'е', 'т']""",
                    update.message.chat_id, context,
                    name='metod_str21')
    update.message.reply_text('list(s)')
    update.message.reply_html(
        text="""Список символов из строки строки s""")


def str_bool(update, context):
    send_photo_file("""Проверка, что строка не пустая (возвращает True,
         если не пустая, и False в противном случае)""",
                    update.message.chat_id, context,
                    name='metod_str22')
    update.message.reply_text('bool(s)')


def str_int(update, context):
    send_photo_file("""int('25') == 25""",
                    update.message.chat_id, context,
                    name='metod_str23')
    update.message.reply_text('int(s)\nfloat(s)')
    update.message.reply_html(
        text="""Если в строке s записано целое (дробное) число,
    получить это число, иначе — ошибка""")


def str_str(update, context):
    send_photo_file("""str(25) == '25'""",
                    update.message.chat_id, context,
                    name='metod_str24')
    update.message.reply_text('str(x)')
    update.message.reply_html(
        text="""Представить любой объект x в виде строки""")


def operations_str(update, context):
    update.message.reply_html(text="""Операции над строками:
    s2 <b>in</b> s - /str_in
    s2 <b>not in</b> s - /str_not_in
    s <b>+</b> s2 - /str_summa
    s <b>*</b> k - /str_multiply
    s<b>[n]</b> - /str_ind
    s<b>[start:stop:step]</b> - /str_slice
    <b>len(s)</b> - /str_len
    s <b>+=</b> s2 - /str_summpl
    <b>list(s)</b> - /str_list
    <b>bool(s)</b> - /str_bool
    <b>int(s)</b> - /str_int
    <b>str(x)</b> - /str_str""", reply_markup=create_markup([['/stri', '/operations_str']]))


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


def methods_str(update, context):
    update.message.reply_html(text="""Методы строк:
    <b>s.find(s2)</b> - /str_find
    <b>s.count(s2)</b> - /str_count
    <b>s.startswith(s2)</b> - /str_swith
    <b>s.isdigit()</b> - /str_isdigit
    <b>s.islower()</b> - /str_islower
    <b>s.lower()</b> - /str_lower
    <b>s.capitalize()</b> - /str_capitalize
    <b>s.lstrip()</b> - /str_lstrip
    <b>s.ljust(k, c)</b> - /str_ljust
    <b>s.join(a)</b> - /str_join
    <b>s.split(s2)</b> - /str_split
    <b>s.replace(s2, s3)</b> - /str_replace""", reply_markup=create_markup([['/stri', '/methods_str']]))
