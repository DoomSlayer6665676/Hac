import logging
import os
import asyncio
from carbon import Carbon
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, Chat
import sqlite3

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)
TOKEN = '5930700784:AAHZrkr1sEawfpY1bmKAgQzLUn5bYS8y-Q4'
board = [['/help'], ['/themes', '/techsupport']]
exp = [[' - что я умею'], [' - содержание справочника', ' - техподдержка']]
markup = ReplyKeyboardMarkup(board, one_time_keyboard=False)
updater = Updater(TOKEN)
dp = updater.dispatcher
client = Carbon(
    downloads_dir=os.getcwd(),
    colour="rgba(39,40,34,1)",
    shadow=False,
    shadow_blur_radius="0px",
    shadow_offset_y="0px",
    export_size="3x",
    font_size="18px",
    font_family= "IBM Plex Mono",
    first_line_number=1,
    language="python",
    line_numbers=False,
    horizontal_padding="13px",
    vertical_padding="30px",
    theme="monokai",
    watermark=False,
    width_adjustment=True,
    window_controls= True,
    window_theme='sharp'
)


def send_photo_file(img_text, id_chat, context, text=None, name=None):
    con = sqlite3.connect("photo_id.sqlite")
    cur = con.cursor()
    result = cur.execute("SELECT * FROM id WHERE Name=?", (name,)).fetchall()
    if result:
        pass
        context.bot.send_photo(id_chat, result[0][-1])
    else:
        asyncio.run(create_photo(img_text, name2=name))
        img = open(name + '.png', 'rb')
        pho = context.bot.send_photo(id_chat, img, caption=text)
        img.close()
        if os.path.isfile(f'{name}.png'):
            os.remove(f'{name}.png')
            print("success")
        else:
            print("File doesn't exists!")
        cur.execute(f"INSERT INTO id VALUES {(name, pho['photo'][0]['file_id'])}")
        print(pho['photo'][0]['file_id'])
        con.commit()
    con.close()


async def create_photo(img_text, name2=None):
    path = await client.create(img_text, file=name2)
    print(path)


def create_markup(mar):
    return ReplyKeyboardMarkup(mar, one_time_keyboard=False)