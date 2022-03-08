from .. import loader, utils 
from telethon import events 
from telethon.errors.rpcerrorlist import YouBlockedUserError 
from asyncio.exceptions import TimeoutError 
 
 
def register(cb): 
    cb(WikiMod()) 
 
class WikiMod(loader.Module): 
    """Ахуенный мод с Ебучей Галей""" 
    strings = {'name': 'Асдалхощ)0)))'} 
 
    async def galyacmd(self, message): 
        """Пиши .galya + Ненужное нахуй слово или реплай.""" 
        try: 
            text = utils.get_args_raw(message) 
            reply = await message.get_reply_message() 
            chat = "@GPT3AutismBot" 
            if not text and not reply: 
                await message.edit("<b> Что это блять?..</b>") 
                return 
            if text: 
                await message.edit("<b>Галя, жрать!</b>") 
                async with message.client.conversation(chat) as conv: 
                    try: 
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=1760933394)) 
                        await message.client.send_message(chat, " " + text) 
                        response = await response 
                    except YouBlockedUserError: 
                        await message.reply("<b>ЗАЕБАЛ! УДАЛИ ИЗ ЧС ЭТОГО ПРИДУРКА! @GPT3AutismBot </b>") 
                        return 
                    if not response.text: 
                        await message.edit("<Давай по новой, Леня!</b>") 
                        return 
                    await message.delete() 
                    await message.client.send_message(message.to_id, response.text) 
            if reply: 
                await message.edit("<b>Макщ, когда вторая часть Хуйониных The Movie???</b>") 
                async with message.client.conversation(chat) as conv: 
                    try: 
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=1760933394)) 
                        await message.client.send_message(chat, reply) 
                        response = await response 
                    except YouBlockedUserError: 
                        await message.reply("<b>Удаляй при мне блять! @GPT3AutismBot</b>") 
                        return 
                    if not response.text: 
                        await message.edit("<Костя нюхнул Спарта Ремикс... </b>") 
                        return 
                    await message.delete() 
                    await message.client.send_message(message.to_id, response.text) 
        except TimeoutError: 
            return await message.edit("<b>Ага, секс, Вера обасралась(((((.</b>")