from .. import loader, utils 
from telethon import events 
from telethon.errors.rpcerrorlist import YouBlockedUserError 
from asyncio.exceptions import TimeoutError 
 
 
def register(cb): 
    cb(AsdalhoshMod()) 
 
class AsdalhoshMod(loader.Module): 
    """Асдалхощ)0)) """ 
    strings = {'name': 'asdalhosh'} 
 
    async def galyacmd(self, message): 
        """Пиши .galya + любое ненужное нахуй слово или сделай реплай.""" 
        try: 
            text = utils.get_args_raw(message) 
            reply = await message.get_reply_message() 
            chat = "@GPT3AutismBot" 
            if not text and not reply: 
                await message.edit("<b>А эм... Ладно</b>") 
                return 
            if text: 
                await message.edit("<b>Галя, принеси мне пива...</b>") 
                async with message.client.conversation(chat) as conv: 
                    try: 
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=528677877)) 
                        await message.client.send_message(chat, "  " + text) 
                        response = await response 
                    except YouBlockedUserError: 
                        await message.reply("<b>Удали из ЧС: @GPT3AutismBot</b>") 
                        return 
                    if not response.text: 
                        await message.edit("<Ещё раз пробуй</b>") 
                        return 
                    await message.delete() 
                    await message.client.send_message(message.to_id, response.text) 
            if reply: 
                await message.edit("<b>Хуйонины The Movie топ...</b>") 
                async with message.client.conversation(chat) as conv: 
                    try: 
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=528677877)) 
                        await message.client.send_message(chat, reply) 
                        response = await response 
                    except YouBlockedUserError: 
                        await message.reply("<b>Удали из ЧС: @GPT3AutismBot</b>") 
                        return 
                    if not response.text: 
                        await message.edit("<Пробуй еще раз </b>") 
                        return 
                    await message.delete() 
                    await message.client.send_message(message.to_id, response.text) 
        except TimeoutError: 
            return await message.edit("Все, он сдох...</b>")
