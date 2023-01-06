import logging
import asyncio
import os
from carbon import Carbon
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)
TOKEN = '5930700784:AAHZrkr1sEawfpY1bmKAgQzLUn5bYS8y-Q4'
board = [['/help'], ['/themes', '/bugs'], ['/techsupport', '/DONATE']]
exp = [[' - что я умею'], [' - содержание справочника', ' - распространённые ошибки'],
       [' - техподдержка', ' - пожертвования на развитие']]
markup = ReplyKeyboardMarkup(board, one_time_keyboard=False)
updater = Updater(TOKEN)
dp = updater.dispatcher
client = Carbon(
    downloads_dir=os.getcwd(),
    colour="rgba(39,40,34,1)",
    shadow=False,
    shadow_blur_radius="0px",
    shadow_offset_y="0px",
    export_size="2x",
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


async def send_photo_file(img_text, id_chat, context, name=None):
    path = await client.create(img_text, file=name)
    print(path)
    img = open(name + '.png', 'rb')
    context.bot.send_photo(id_chat, img)
    img.close()
    if os.path.isfile(f'{name}.png'):
        os.remove(f'{name}.png')
        print("success")
    else:
        print("File doesn't exists!")
