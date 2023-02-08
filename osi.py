from CONST import *


def add_os_handler():
    pass


def os_info(update, context):
    send_photo_file(""">>> import os
... print(os.name)
nt""",
                    update.message.chat_id, context,
                    name='os_info1')
    update.message.reply_html(
        text="""Чтобы узнать имя текущей ОС, достаточно воспользоваться методом name. 
        Вам откроются следующие значения: ‘posix’, ‘nt’, ‘os2’, ‘ce’, ‘java’, ‘riscos’. 
        Следующая программа была запущена на ПК с ОС Windows 10, поэтому результатом работы функции name является строка nt.""")
    send_photo_file(""">>> import os
... print(os.environ)
environ({'ALLUSERSPROFILE': 'C:\\ProgramData',
         'APPDATA': 'C:\\Users\\[USER NAME]\\AppData\\Roaming', 
          ...}""",
                    update.message.chat_id, context,
                    name='os_info2')
    update.message.reply_html(
        text="""Получить сведения, которые касаются конфигурации компьютера, можно при помощи метода environ.
        "Этот метод дает вам полезную информацию, такую как количество процессоров, тип ОЗУ, имя компьютера, и так далее.""")
    send_photo_file(""">>> import os
... print(os.environ["TMP"])
C:\\Users\\mike\\AppData\\Local\\Temp
... print(os.getenv("TMP"))
C:\\Users\\mike\\AppData\\Local\\Temp""",
                    update.message.chat_id, context,
                    name='os_info3')
    update.message.reply_html(
        text="""Как вы могли заметить, это вернуло словарь. Это значит, что вы можете получить доступ к значениям среды, пользуясь обычными словарными методами.
        Вы также можете использовать функцию os.getenv для доступа к этой переменной.""")
    send_photo_file(""">>> import os
... print(os.environ["TMP2"])
Traceback (most recent call last):
  File "<input>", line 3, in <module>
  File "C:\\Users\\HYPERPC\\AppData\\Local\\Programs\\Python\\Python310\\lib\\os.py", line 679, in __getitem__
    raise KeyError(key) from None
KeyError: 'TMP2'""",
                    update.message.chat_id, context,
                    name='os_info4')
    update.message.reply_html(
        text="""Полезность использования os.getenv() вместо словаря os.environ заключается в том, что если вы находитесь в положении, когда вам нужно получить доступ к переменной среды, которая не существует, функция getenv попросту ничего не сделает. Если вы попытаетесь сделать то же самое, пользуясь os.environ, вы получите уведомление об ошибке.""")


def working_directory(update, context):
    send_photo_file(""">>> import os
... print(os.getcwd())
    C:\\Users\\HYPERPC\\PycharmProjects\\pythonProject""",
                    update.message.chat_id, context,
                    name='working_directory1')
    update.message.reply_html(
        text="""По умолчанию рабочей директорией программы является каталог, где содержится документ с ее исходным кодом. Благодаря этому, можно не указывать абсолютный путь к файлу, если тот находится именно в этой папке. Получить сведения о текущей директории позволяет функция getcwd, которая возвращает полный адрес рабочего каталога на жестком диске.""")
    send_photo_file("""""",
                    update.message.chat_id, context,
                    name='working_directory2')
    update.message.reply_html(
        text="""""")


def path_existence(update, context):
    send_photo_file("""""",
                    update.message.chat_id, context,
                    name='os_info')
    update.message.reply_html(
        text="""""")


def Creating_directories(update, context):
    send_photo_file("""""",
                    update.message.chat_id, context,
                    name='os_info')
    update.message.reply_html(
        text="""""")


def Deleting_files_directories(update, context):
    send_photo_file("""""",
                    update.message.chat_id, context,
                    name='os_info')
    update.message.reply_html(
        text="""""")


def start(update, context):
    send_photo_file("""""",
                    update.message.chat_id, context,
                    name='os_info')
    update.message.reply_html(
        text="""""")


def directory_file_name(update, context):
    send_photo_file("""""",
                    update.message.chat_id, context,
                    name='os_info')
    update.message.reply_html(
        text="""""")


def size(update, context):
    send_photo_file("""""",
                    update.message.chat_id, context,
                    name='os_info')
    update.message.reply_html(
        text="""""")


def Renaming(update, context):
    send_photo_file("""""",
                    update.message.chat_id, context,
                    name='os_info')
    update.message.reply_html(
        text="""""")


def Content(update, context):
    send_photo_file("""""",
                    update.message.chat_id, context,
                    name='os_info')
    update.message.reply_html(
        text="""""")


def Info(update, context):
    send_photo_file("""""",
                    update.message.chat_id, context,
                    name='os_info')
    update.message.reply_html(
        text="""""")


def Path_handling(update, context):
    send_photo_file("""""",
                    update.message.chat_id, context,
                    name='os_info')
    update.message.reply_html(
        text="""""")
