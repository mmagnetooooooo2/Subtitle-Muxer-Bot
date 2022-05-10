# :d hahhaha
import shutil
import psutil
import heroku3
from pyrogram import filters
from pyrogram.types import (
    Message
)
from config import Config
from pyrogram import Client
from database.database import db
from helper_func.progress_bar import humanbytes
from plugins.broadcast import broadcast_handler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


@Client.on_message(filters.command("status") & filters.user(Config.OWNER_ID))
async def status_handler(_, m: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await m.reply_text(
        text=f"**Toplam alan:** {total} \n"
             f"**Kullanılan alan:** {used}({disk_usage}%) \n"
             f"**Boş alan:** {free} \n"
             f"**Cpu kullanımı:** {cpu_usage}% \n"
             f"**Ram kullanımı:** {ram_usage}%\n\n"
             f"**Tüm kullanıcılar:** `{total_users}`",
        parse_mode="Markdown",
        quote=True
    )
@Client.on_message(filters.command("restart") & filters.user(Config.OWNER_ID))
async def restart(_, m: Message):
    restart_msg = await m.reply_text(text="`İşleniyor...`")
    await restart_msg.edit("`Yeniden başlatılıyor! Lütfen bekle...`")
    try:
        if HEROKU_API_KEY is not None and HEROKU_APP_NAME is not None:
            heroku_conn = heroku3.from_key(HEROKU_API_KEY)
            server = heroku_conn.app(HEROKU_APP_NAME)
            server.restart()
        else:
            await restart_msg.edit("`Heroku değişkenlerini ekleyin.`")
    except Exception as e:
        await restart_msg.edit(f"**Error:** `{e}`")

@Client.on_message(filters.command("broadcast") & filters.user(Config.OWNER_ID) & filters.reply)
async def broadcast_in(_, m: Message):
    await broadcast_handler(m)

# @Client.on_message(filters.command("log") & filters.user(Config.OWNER_ID))
