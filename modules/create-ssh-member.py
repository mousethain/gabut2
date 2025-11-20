from cybervpn import *
import subprocess
import datetime as DT
import sys
from telethon.sync import TelegramClient
import sqlite3

@bot.on(events.CallbackQuery(data=b'create-ssh-member'))
async def create_ssh(event):
    user_id = str(event.sender_id)

    async def create_ssh_(event):
        async with bot.conversation(chat) as user_conv:
            await event.respond('**Username:**')
            user_msg = user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user_msg).raw_text
        
        async with bot.conversation(chat) as pw_conv:
            await event.respond("**Password:**")
            pw_msg = pw_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            pw = (await pw_msg).raw_text
        
        async with bot.conversation(chat) as exp_conv:
            await event.respond("**Choose Expiry Day**", buttons=[
                [
                 Button.inline("• 30 Day •", "30")]
            ])
            exp_msg = exp_conv.wait_event(events.CallbackQuery)
            exp = (await exp_msg).data.decode("ascii")
        
        async with bot.conversation(chat) as ip_conv:
            await event.respond("**Choose ip limit**", buttons=[
                [
                 Button.inline(" 2 IP ", "2")]
            ])
            ip_msg = ip_conv.wait_event(events.CallbackQuery)
            ip = (await ip_msg).data.decode("ascii")
        
        # Simpan informasi IP limit ke dalam file
        with open(f'/etc/cybervpn/limit/ssh/ip/{user}', 'w') as file:
            file.write(ip)

        # Panggil fungsi untuk memproses saldo pengguna
        await process_user_balance_ssh(event, user_id)

        # Lanjutkan dengan eksekusi perintah useradd dan pesan respons
        cmd = f'useradd -e `date -d "{exp} days" +"%Y-%m-%d"` -s /bin/false -M {user} && echo "{pw}\n{pw}" | passwd {user}'
        try:
            subprocess.check_output(cmd, shell=True)
        except:
            await event.respond("**User Already Exist**")
        else:
            today = DT.date.today()
            later = today + DT.timedelta(days=int(exp))
            msg = f"""
**━━━━━━━━━━━━━━━━**
╔═══╦═══╦╗─╔╗
║╔═╗║╔═╗║║─║║
║╚══╣╚══╣╚═╝║
╚══╗╠══╗║╔═╗║
║╚═╝║╚═╝║║─║║
╚═══╩═══╩╝─╚╝
`•websocket•`
**━━━━━━━━━━━━━━━━**
**» Host:** `{DOMAIN}`
**» Username:** `{user.strip()}`
**» Password:** `{pw.strip()}`
**» limit ip:** `{ip}`
**» pubkey:** `{PUB}`
**» Nameserver:** `{DNS}`
**» Harga akun:** `RP.10.000`
**» Sisa saldo:** `RP.{get_saldo_from_db(user_id)}` 
**━━━━━━━━━━━━━━━━**
**» Port OpenSSH     :** `22,58080`
**» Port Dropbear    :** `69, 143, 109`
**» Port Dropbear WS :** `443, 109`
**» Port SSH WS      :** `80`
**» Port SSH SSL WS  :** `443`
**» Port SSH Direct  :** `8880,8080,2082`
**» Port Stunnel4    :** `222,777,2096`
**» Port OVPN SSL    :** `110`
**» Port OVPN TCP    :** `1194`
**» Port OVPN UDP    :** `2200`
**» Port OHP SSH     :** `8686`
**» Port OHP Dropbear:** `8585`
**» Port OHP OpenVpn :** `8787`
**» Port UDP Custom  :** `1-2288`
**» Port UDP Custom  :** `80`
**» Port UDP Custom  :** `443`
**» Proxy Squid      :** `3128, 8000`
**» BadVPN UDP       :** `7100-7300`
**◇━━━━━━━━━━━━━━━━━◇**
**⟨ OpenVPN & OHP  ⟩**
**» OpenVPN TCP      :** `1194 http://{DOMAIN}:81/tcp.ovpn`
**» OpenVPN UDP      :** `2200 http://{DOMAIN}:81/udp.ovpn`
**» OpenVPN SSL      :** `110 http://{DOMAIN}:81/ssl.ovpn`
**◇━━━━━━━━━━━━━━━━━◇**
**⟨ Payload WS  ⟩**
`GET / HTTP/1.1[crlf]Host: {DOMAIN}[crlf]Upgrade: websocket[crlf][crlf]`
**⟨ Payload WS SSL ⟩**
`GET wss:/// HTTP/1.1[crlf]Host: {DOMAIN}[crlf]Upgrade: websocket[crlf]Connection: Keep-Alive[crlf][crlf]`
**━━━━━━━━━━━━━━━━**
**» Expired Until:** `{later}`
**» 🛂@mousethain**
**━━━━━━━━━━━━━━━━**
"""
            inline = [
                [Button.url("[ Contact ]", "t.me/mousethain")]
            ]
            await event.respond(msg, buttons=inline)
    
    chat = event.chat_id
    sender = await event.get_sender()
    try:
        level = get_level_from_db(user_id)
        print(f'Retrieved level from database: {level}')

        if level == 'user':
            await create_ssh_(event)
        else:
            await event.answer(f'Akses Ditolak.!!', alert=True)
    except Exception as e:
        print(f'Error: {e}')

