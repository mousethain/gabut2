from cybervpn import *
import subprocess
import datetime as DT

@bot.on(events.NewMessage(pattern=r"(?:/registrasi)$"))
@bot.on(events.CallbackQuery(data=b'registrasi'))
async def registrasi_handler(event):
    chat = event.chat_id
    sender = await event.get_sender()
    user_id = str(event.sender_id)

    async def get_username(user_conv):
        await event.edit('**Masukkan usernamemu:**')
        user_msg = await user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
        return user_msg.raw_text

    async with bot.conversation(chat) as user_conv:
        user = await get_username(user_conv)

    saldo = 0
    level = "user"
    register_user(user_id, saldo, level)

    today = DT.date.today()
    later = today + DT.timedelta(days=int(0))
    msg = f"""
**━━━━━━━━━━━━━━━━**
**⟨🕊Registration Success🕊⟩**
**━━━━━━━━━━━━━━━━**
**» Your ID:** `{user_id}`
**» Username:** `{user}`
**» Balance:** `IDR.0`
**» Ketik /menu untuk login**
**━━━━━━━━━━━━━━━━**
**» Registration Date:** `{later}`
**» 🛂@wongedan_kuwibebas**
**━━━━━━━━━━━━━━━━**
"""
    inline = [
        [
         Button.inline("[ login ]", "menu")]
    ]
    await event.respond(msg, buttons=inline)

