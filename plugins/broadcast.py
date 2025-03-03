# :d hahhahaha
import time
import string
import random
import asyncio
import datetime
import aiofiles
import traceback
import aiofiles.os
from config import Config
from database.database import db
from pyrogram.types import Message
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

broadcast_ids = {}


async def send_msg(user_id, message):
    try:
        if Config.BROADCAST_AS_COPY is False:
            await message.forward(chat_id=user_id)
        elif Config.BROADCAST_AS_COPY is True:
            await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : Aktif diil\n"
    except UserIsBlocked:
        return 400, f"{user_id} : bptu engellemiş\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : silinen hesap\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"


async def broadcast_handler(m: Message):
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if not broadcast_ids.get(broadcast_id):
            break
    out = await m.reply_text(
        text=f"Yayın başladı bitince log atçam ;)."
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(
        total=total_users,
        current=done,
        failed=failed,
        success=success
    )
    async with aiofiles.open('broadcast.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(
                user_id=int(user['id']),
                message=broadcast_msg
            )
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user['id'])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(
                        current=done,
                        failed=failed,
                        success=success
                    )
                )
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(
            text=f"Yayın Tammalandı `{completed_in}`\n\n"
                 f"Toplam kullanıcı {total_users}.\n"
                 f"Toplam Tamamlanan {done}, {success} başarılı ve {failed} başarısız.",
            quote=True
        )
    else:
        await m.reply_document(
            document='broadcast.txt',
            caption=f"yayın tamamlandı`{completed_in}`\n\n"
                    f"Toplam kullanıcı {total_users}.\n"
                    f"Toplam tamamlanan {done}, {success} başarılı ve {failed} başarısız.",
            quote=True
        )
    await aiofiles.os.remove('broadcast.txt')
