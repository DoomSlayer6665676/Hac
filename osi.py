from CONST import *


def add_os_handler():
    dp.add_handler(CommandHandler("os_info", os_info))
    dp.add_handler(CommandHandler("working_directory", working_directory))
    dp.add_handler(CommandHandler("path_existence", path_existence))
    dp.add_handler(CommandHandler("creating_directories", creating_directories))
    dp.add_handler(CommandHandler("deleting_files_directories", deleting_files_directories))
    dp.add_handler(CommandHandler("start_", start_))
    dp.add_handler(CommandHandler("directory_file_name", directory_file_name))
    dp.add_handler(CommandHandler("size", size))
    dp.add_handler(CommandHandler("renaming", renaming))
    dp.add_handler(CommandHandler("content", content))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("path_handling", path_handling))


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
    send_photo_file(""">>> os.chdir(r"C:\\Users\\[USER NAME]\\Documents")
... print(os.getcwd())
C:\\Users\\[USER NAME]\\Documents""",
                    update.message.chat_id, context,
                    name='working_directory2')
    update.message.reply_html(
        text="""При желании, рабочую директорию можно настроить по своему усмотрению, применив метод chdir. Для этого необходимо передать ему в качестве параметра абсолютный адрес к новому каталогу. Если указанного пути на самом деле не существует, программа будет завершена в аварийном режиме из-за выброшенного исключения.""")


def path_existence(update, context):
    send_photo_file(""">>> import os
... print(os.path.exists("D:/test.txt"))
True""",
                    update.message.chat_id, context,
                    name='path_existence1')
    update.message.reply_html(
        text="""Передав методу exists в качестве аргумента путь к нужному файлу или папке, можно рассчитывать на ответ в виде булевого значения true/false.""")
    send_photo_file("""import os
 
os.path.isfile(r'C:\Python27\Tools\pynche\ChipViewer.py') # True
 
os.path.isdir(r'C:\Python27\Tools\pynche\ChipViewer.py') # False
 
os.path.isdir(r'C:\Python27\Tools\pynche') # True
 
os.path.isfile(r'C:\Python27\Tools\pynche') # False""",
                    update.message.chat_id, context,
                    name='path_existence2')
    update.message.reply_html(
        text="""Методы isdir и isfile тесно связаны с методом exists, так как они также тестируют присутствие или отсутствие файлов или папок на тех или иных путях. Однако, isdir проверяет только пути к папкам, а isfile, соответственно, к файлам.""")


def creating_directories(update, context):
    send_photo_file(""">>> import os
... os.mkdir(r"D:\\folder")

... os.makedirs(r"D:\\folder\\first\\second\\third")""",
                    update.message.chat_id, context,
                    name='creating_directories')
    update.message.reply_html(
        text="""С помощью метода mkdir довольно легко создать папку, просто указав для нее желаемый путь.
        Благодаря методу makedirs можно создавать сразу несколько новых папок в неограниченном количестве, если предыдущая директория является родительской для следующей. Таким образом, в следующем примере показывается генерация целой цепочки папок из folder, first, second и third.""")


def deleting_files_directories(update, context):
    send_photo_file(""">>> import os
... os.remove(r"D:\\test.txt")""",
                    update.message.chat_id, context,
                    name='deleting_files_directories1')
    update.message.reply_html(
        text="""Избавиться от ненужного в дальнейшей работе файла можно с помощью метода remove, отдав ему в качестве аргумента абсолютный либо относительный путь к объекту.""")
    send_photo_file("""import os
os.rmdir(r"D:\\folder")
os.removedirs(r"D:\\folder\\first\second\\third")""",
                    update.message.chat_id, context,
                    name='deleting_files_directories2')
    update.message.reply_html(
        text="""Чтобы стереть из памяти папку, следует воспользоваться встроенной функцией rmdir, указав ей адрес объекта. Однако программа не позволит беспрепятственно удалить директорию, в которой хранятся другие объекты.
        Для быстрого удаления множества пустых папок следует вызывать функцию removedirs. Таким образом, указав путь к конечной папке, можно легко удалить все родительские директории, но только если они в результате оказываются пустыми.""")


def start_(update, context):
    send_photo_file("""""",
                    update.message.chat_id, context,
                    name='start')
    update.message.reply_html(
        text="""""")


def directory_file_name(update, context):
    send_photo_file("""import os
os.startfile(r"D:\\test.txt")""",
                    update.message.chat_id, context,
                    name='directory_file_name')
    update.message.reply_html(
        text="""Метод os.startfile() позволяет запустить файл в привязанной к нему программе.""")


def size(update, context):
    send_photo_file(""">>> import os
... print(os.path.getsize("D:\\test.txt"))
136226""",
                    update.message.chat_id, context,
                    name='size')
    update.message.reply_html(
        text="""Чтобы определить размер документа или папки, стоит воспользоваться функцией getsize""")


def renaming(update, context):
    send_photo_file("""os.rename("test.txt", "pytest.txt")""",
                    update.message.chat_id, context,
                    name='renaming')
    update.message.reply_html(
        text="""Функция os.rename() применяется тогда, когда нужно переименовать файл или папку.""")


def content(update, context):
    send_photo_file(""">>> import os
... print(os.listdir(r"D:\\folder"))
['first', 'test.txt']""",
                    update.message.chat_id, context,
                    name='content')
    update.message.reply_html(
        text="""Проверить наличие в каталоге определенных объектов позволяет функция listdir. С её помощью можно получить информацию о файлах и папках в виде списка. Метод принимает в качестве параметра путь к каталогу folder на диске D, а затем выводит название внутренней папки first и документа test.txt""")


def info(update, context):
    send_photo_file(""">>> import os
... print(os.stat(r"D:\test.txt"))
os.stat_result(st_mode=33206, …)""",
                    update.message.chat_id, context,
                    name='info')
    update.message.reply_html(
        text="""Поместив в качестве параметра расположение файла или папки на диске компьютера, возвращает небольшой массив информации. Здесь можно найти данные о размере объекта в байтах, а также некие числовые значения, отображающие доступ и режим его работы.""")


def path_handling(update, context):
    send_photo_file(""">>> import os
... print(os.path.split(r"D:\\folder\\test.txt"))
('D:\\folder', 'test.txt')""",
                    update.message.chat_id, context,
                    name='path_handling1')
    update.message.reply_html(
        text="""Функция split, позволяет разъединять путь к файлу и имя файла в различные строки.""")
    send_photo_file(""">>> import os
... print(os.path.join(r"D:\\folder", "test.txt"))
D:\\folder\\test.txt""",
                    update.message.chat_id, context,
                    name='path_handling2')
    update.message.reply_html(
        text="""Функция join, позволяет соединить путь к документу с его названием.""")
