import logging
import os
import time
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from functions.utils import ReadableTime
from pyromod import listen
logging.basicConfig(level = logging.DEBUG,
                     format="%(asctime)s - %(name)s - %(message)s - %(levelname)s")

logger = logging.getLogger(__name__)

import os

if os.path.exists('testconfig.py'):
    from testconfig import Config
else:
    from config import Config

from helper_func.dbhelper import Database as Db
db = Db().setup()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)
botStartTime = time.time()

import pyrogram
logging.getLogger('pyrogram').setLevel(logging.WARNING)


if __name__ == '__main__':

    if not os.path.isdir(Config.DOWNLOAD_DIR):
        os.mkdir(Config.DOWNLOAD_DIR)

    plugins = dict(root='plugins')

    app = pyrogram.Client(
        'Subtitle Muxer',
        bot_token = Config.BOT_TOKEN,
        api_id = Config.APP_ID,
        api_hash = Config.API_HASH,
        plugins = plugins
    )
async def start(self):
        if not os.path.isdir(DOWNLOAD_LOCATION): os.makedirs(DOWNLOAD_LOCATION)
        await super().start()
        me = await self.get_me()
        self.username = '@' + me.username
        LOGGER.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
        if OWNER_ID != 0:
            try:
                await self.send_message(text="Karanlığın küllerinden yeniden doğdum.",
                    chat_id=OWNER_ID)
            except Exception as t:
                LOGGER.error(str(t))

    async def stop(self, *args):
        if OWNER_ID != 0:
            texto = f"Son nefesimi verdim.\nÖldüğümde yaşım: {ReadableTime(time.time() - botStartTime)}"
            try:
                if SEND_LOGS_WHEN_DYING:
                    await self.send_document(document='log.txt', caption=texto, chat_id=OWNER_ID)
                else:
                    await self.send_message(text=texto, chat_id=OWNER_ID)
            except Exception as t:
                LOGGER.warning(str(t))
        await super().stop()
        LOGGER.info(msg="App Stopped.")
        exit()

    app.run()
