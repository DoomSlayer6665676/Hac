from CONST import *


def operations_list(update, context):
    send_photo_file("""5 in [2, 3, 5]""",
                    update.message.chat_id, context,
                    name='metod_list1')
    delete_group.append(update.message.reply_text('x in a')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Проверка, что x содержится в а""")['message_id'])
    send_photo_file("""5 not in [2, 3, 6]""",
                    update.message.chat_id, context,
                    name='metod_list2')
    delete_group.append(update.message.reply_text('x not in a')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Проверка, что x не содержится в а
То же, что и not (x in a)""")['message_id'])
    send_photo_file("""[2, 4] + [5, 3] == [2, 4, 5, 3]""",
                    update.message.chat_id, context,
                    name='metod_list3')
    delete_group.append(update.message.reply_text('a + a2')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Конкатенация списков, то есть новый список, в котором сначала идут все элементы a,
а затем все элементы a2""")['message_id'])
    send_photo_file("""[2, 3] * 3 == [2, 3, 2, 3, 2, 3]""",
                    update.message.chat_id, context,
                    name='metod_list4')
    delete_group.append(update.message.reply_text('a * k')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Список a, повторенный k раз""")['message_id'])
    send_photo_file("""[2, 3, 7][0] == 2
[2, 3, 7][-1] == 7""",
                    update.message.chat_id, context,
                    name='metod_list5')
    delete_group.append(update.message.reply_text('a[n]')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""n-й элемент списка,
отрицательные n — для отсчета с конца""")['message_id'])
    send_photo_file("""[2, 3, 7][:2] == [2, 3]""",
                    update.message.chat_id, context,
                    name='metod_list6')
    delete_group.append(update.message.reply_text('a[start:stop:step]')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Срез списка""")['message_id'])
    send_photo_file("""len([2, 3, 7]) == 3""",
                    update.message.chat_id, context,
                    name='metod_list7')
    delete_group.append(update.message.reply_text('len(a)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Длина списка""")['message_id'])
    send_photo_file("""max([2, 3, 7]) == 7""",
                    update.message.chat_id, context,
                    name='metod_list8')
    delete_group.append(update.message.reply_text('max(a)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Максимальный элемент списка""")['message_id'])
    send_photo_file("""min([2, 3, 7]) == 2""",
                    update.message.chat_id, context,
                    name='metod_list9')
    delete_group.append(update.message.reply_text('min(a)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Минимальный элемент списка""")['message_id'])
    send_photo_file("""sum([2, 3, 7]) == 12""",
                    update.message.chat_id, context,
                    name='metod_list10')
    delete_group.append(update.message.reply_text('sum(a)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Сумма элементов списка""")['message_id'])
    send_photo_file("""[2, 3, 7].index(7) == 2""",
                    update.message.chat_id, context,
                    name='metod_list11')
    delete_group.append(update.message.reply_text('a.index(x)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Индекс первого вхождения x в a
(вызовет ошибку, если x not in a, то есть если х отсутствует в а)""")['message_id'])
    send_photo_file("""[2, 7, 3, 7].count(7) == 2""",
                    update.message.chat_id, context,
                    name='metod_list12')
    delete_group.append(update.message.reply_text('a.count(x)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Количество вхождений x в a""")['message_id'])
    send_photo_file("""a = [2, 3, 7]
a.append(8)
a == [2, 3, 7, 8]""",
                    update.message.chat_id, context,
                    name='metod_list13')
    delete_group.append(update.message.reply_text('a.append(x)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Добавить x в конец a""")['message_id'])
    send_photo_file("""a = [2, 3, 7]
a.extend([8, 4, 5])
a == [2, 3, 7, 8, 4, 5]""",
                    update.message.chat_id, context,
                    name='metod_list14')
    delete_group.append(update.message.reply_text('a.extend(a2)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Добавить элементы коллекции a2 в конец a""")['message_id'])
    send_photo_file("""a = [2, 3, 7]
del a[1]
a == [2, 7]""",
                    update.message.chat_id, context,
                    name='metod_list15')
    delete_group.append(update.message.reply_text('del a[n]')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Удалить n-й элемент списка""")['message_id'])
    send_photo_file("""a = [2, 3, 7]
del a[:2]
a == [7]""",
                    update.message.chat_id, context,
                    name='metod_list16')
    delete_group.append(update.message.reply_text('del a[start:stop:step]')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Удалить из a все элементы, попавшие в срез""")['message_id'])
    send_photo_file("""a.clear()""",
                    update.message.chat_id, context,
                    name='metod_list17')
    delete_group.append(update.message.reply_text('a.clear()')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Удалить из a все элементы (то же, что del a[:])""")['message_id'])
    send_photo_file("""b = a.copy()""",
                    update.message.chat_id, context,
                    name='metod_list18')
    delete_group.append(update.message.reply_text('a.copy()')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Копия a (то же, что и полный срез a[:])""")['message_id'])
    send_photo_file("""Заменить содержимое списка на a + a2
и a * k соответственно""",
                    update.message.chat_id, context,
                    name='metod_list19')
    delete_group.append(update.message.reply_text('a += a2\na *= k')['message_id'])
    send_photo_file("""a = [2, 3, 7]
a.insert(0, 8)
a == [8, 2, 3, 7]""",
                    update.message.chat_id, context,
                    name='metod_list20')
    delete_group.append(update.message.reply_text('a.insert(n, x)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""	Вставить x в a на позицию n, подвинув последующую часть дальше""")['message_id'])
    send_photo_file("""a = [2, 3, 7]
a.pop(1) == 3
a == [2, 7]""",
                    update.message.chat_id, context,
                    name='metod_list21')
    delete_group.append(update.message.reply_text('a.pop(n)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Получить n-й элемент списка и одновременно удалить его из списка.
Вызов метода без аргументов равносилен удалению последнего элемента:
a.pop() == a.pop(-1)""")['message_id'])
    send_photo_file("""a = [2, 3, 7]
a.remove(3)
a == [2, 7]""",
                    update.message.chat_id, context,
                    name='metod_list22')
    delete_group.append(update.message.reply_text('a.remove(x)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Удалить первое вхождение x в a, в случае x not in a — ошибка""")['message_id'])
    send_photo_file("""a = [2, 3, 7]
a.reverse()
a == [7, 3, 2]""",
                    update.message.chat_id, context,
                    name='metod_list23')
    delete_group.append(update.message.reply_text('a.reverse()')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Изменить порядок элементов в a на обратный (перевернуть список)""")['message_id'])
    send_photo_file("""a = [3, 2, 7]
a.sort()
a == [2, 3, 7]""",
                    update.message.chat_id, context,
                    name='metod_list24')
    delete_group.append(update.message.reply_text('a.sort()')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Отсортировать список по возрастанию""")['message_id'])
    send_photo_file("""a = [3, 2, 7]
a.sort(reverse = True)
a == [7, 3, 2]""",
                    update.message.chat_id, context,
                    name='metod_list25')
    delete_group.append(update.message.reply_text('a.sort(reverse=True)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Отсортировать список по убыванию""")['message_id'])
    send_photo_file("""Один из способов проверить список на пустоту (возвращает True, если список 
    непустой, и False в противном случае)""",
                    update.message.chat_id, context,
                    name='metod_list26')
    delete_group.append(update.message.reply_text('bool(a)')['message_id'])


def operations_str(update, context):
    send_photo_file("""'m' in 'team'""",
                    update.message.chat_id, context,
                    name='metod_str1')
    delete_group.append(update.message.reply_text('s2 in s')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Проверка, что подстрока s2 содержится в s""")['message_id'])
    send_photo_file("""'I' not in 'team'""",
                    update.message.chat_id, context,
                    name='metod_str2')
    delete_group.append(update.message.reply_text('s2 not in s')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Проверка, что подстрока s2 не содержится в s
то же, что not (s2 in s)""")['message_id'])
    send_photo_file("""'tea' + 'm' == 'team'""",
                    update.message.chat_id, context,
                    name='metod_str3')
    delete_group.append(update.message.reply_text('s + s2')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""	Конкатенация (склейка) строк, то есть строка,
в которой сначала идут все символы из s,
а затем все символы из s2""")['message_id'])
    send_photo_file("""'ha' * 3 == 'hahaha'""",
                    update.message.chat_id, context,
                    name='metod_str4')
    delete_group.append(update.message.reply_text('s * k')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Строка s, повторенная k раз""")['message_id'])
    send_photo_file("""'team'[2] == 'a'
'team'[-1] == 'm'""",
                    update.message.chat_id, context,
                    name='metod_str5')
    delete_group.append(update.message.reply_text('s[n]')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""n-й элемент строки,
отрицательные n — для отсчета с конца""")['message_id'])
    send_photo_file("""'mama'[:2] == 'ma'""",
                    update.message.chat_id, context,
                    name='metod_str6')
    delete_group.append(update.message.reply_text('s[start:stop:step]')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Срез строки""")['message_id'])
    send_photo_file("""len('abracadabra') == 11""",
                    update.message.chat_id, context,
                    name='metod_str7')
    delete_group.append(update.message.reply_text('len(s)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Длина строки""")['message_id'])
    send_photo_file("""s = 'abracadabra'
s.find('ab') == 0
s.rfind('ab') == 7
s.find('x') == -1""",
                    update.message.chat_id, context,
                    name='metod_str8')
    delete_group.append(update.message.reply_text('s.find(s2)\ns.rfind(s2)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Индекс начала первого или последнего
вхождения подстроки s2 в s (вернет -1, если s2 not in s""")['message_id'])
    send_photo_file("""'abracadabra'.count('a') == 5""",
                    update.message.chat_id, context,
                    name='metod_str9')
    delete_group.append(update.message.reply_text('s.count(s2)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Количество неперекрывающихся вхождений s2 в s""")['message_id'])
    send_photo_file("""'abracadabra'.startswith('abra')""",
                    update.message.chat_id, context,
                    name='metod_str10')
    delete_group.append(update.message.reply_text('s.startswith(s2)\ns.endswith(s2)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Проверка, что s начинается с s2 или оканчивается на s2""")['message_id'])
    send_photo_file("""Заменить содержимое строки на
s + s2 и s * k соответственно""",
                    update.message.chat_id, context,
                    name='metod_str11')
    delete_group.append(update.message.reply_text('s += s2\ns *= k')['message_id'])
    send_photo_file("""'100'.isdigit()
'abc'.isalpha()
'E315'.isalnum()""",
                    update.message.chat_id, context,
                    name='metod_str12')
    delete_group.append(update.message.reply_text('s.isdigit()\ns.isalpha()\ns.isalnum()')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Проверка, что в строке s все символы — цифры,
буквы (включая кириллические),
цифры или буквы соответственно""")['message_id'])
    send_photo_file("""'hello!'.islower()
'123PYTHON'.isupper()""",
                    update.message.chat_id, context,
                    name='metod_str13')
    delete_group.append(update.message.reply_text('s.islower()\ns.isupper()')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Проверка, что в строке s не встречаются большие буквы, маленькие буквы.
Обратите внимание, что для обеих этих функций знаки препинания и цифры дают True""")['message_id'])
    send_photo_file("""'Привет!'.lower() == 'привет!'
'Привет!'.upper() == 'ПРИВЕТ!'""",
                    update.message.chat_id, context,
                    name='metod_str14')
    delete_group.append(update.message.reply_text('s.lower()\ns.upper()')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Строка s, в которой все буквы (включая кириллические)
приведены к верхнему или нижнему регистру,
т. е. заменены на строчные (маленькие) или заглавные (большие)""")['message_id'])
    send_photo_file("""'привет'.capitalize() == 'Привет'""",
                    update.message.chat_id, context,
                    name='metod_str15')
    delete_group.append(update.message.reply_text('s.capitalize()')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Строка s, в которой первая буква — заглавная""")['message_id'])
    send_photo_file("""' Привет! '.strip() == 'Привет!'""",
                    update.message.chat_id, context,
                    name='metod_str16')
    delete_group.append(update.message.reply_text('s.lstrip()\ns.rstrip()\ns.strip()')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Строка s, у которой удалены символы пустого пространства
(пробелы, табуляции) в начале,
в конце или с обеих сторон""")['message_id'])
    send_photo_file("""'Привет'.ljust(8, '!') == 'Привет!!'""",
                    update.message.chat_id, context,
                    name='metod_str17')
    delete_group.append(update.message.reply_text('s.ljust(k, c)\ns.rjust(k, c)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Добавляет справа или слева нужное количество
символов c, чтобы длина s достигла k""")['message_id'])
    send_photo_file("""'+'.join(['Вася', 'Маша']) == 'Вася+Маша'""",
                    update.message.chat_id, context,
                    name='metod_str18')
    delete_group.append(update.message.reply_text('s.join(a)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Склеивает строки из списка a через символ s""")['message_id'])
    send_photo_file("""'Раз два три!'.split('а') ==
['Р', 'з дв', ' три!']""",
                    update.message.chat_id, context,
                    name='metod_str19')
    delete_group.append(update.message.reply_text('s.split(s2)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Список всех слов строки s
(подстрок, разделенных строками s2)""")['message_id'])
    send_photo_file("""'Раз два три!'.replace('а', 'я') =='Ряз двя три!'
'Раз два три!'.replace('а', 'я', 1) == 'Ряз два три!'""",
                    update.message.chat_id, context,
                    name='metod_str20')
    delete_group.append(update.message.reply_text('s.replace(s2, s3)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Cтрока s, в которой все неперекрывающиеся
вхождения s2 заменены на s3
Есть необязательный третий параметр, с помощью которого можно указать, сколько раз производить замену""")['message_id'])
    send_photo_file("""list('Привет') ==
['П', 'р', 'и', 'в', 'е', 'т']""",
                    update.message.chat_id, context,
                    name='metod_str21')
    delete_group.append(update.message.reply_text('list(s)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Список символов из строки строки s""")['message_id'])
    send_photo_file("""Проверка, что строка не пустая (возвращает True,
     если не пустая, и False в противном случае)""",
                    update.message.chat_id, context,
                    name='metod_str22')
    delete_group.append(update.message.reply_text('bool(s)')['message_id'])
    send_photo_file("""int('25') == 25""",
                    update.message.chat_id, context,
                    name='metod_str23')
    delete_group.append(update.message.reply_text('int(s)\nfloat(s)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Если в строке s записано целое (дробное) число,
получить это число, иначе — ошибка""")['message_id'])
    send_photo_file("""str(25) == '25'""",
                    update.message.chat_id, context,
                    name='metod_str24')
    delete_group.append(update.message.reply_text('str(x)')['message_id'])
    delete_group.append(update.message.reply_html(
        text="""Представить любой объект x в виде строки""")['message_id'])
