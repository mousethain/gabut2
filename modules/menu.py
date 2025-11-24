from mousevpn import *
from telethon import events, Button
import requests

url = "https://raw.githubusercontent.com/mousethain/tahu/main/statushariini"

response = requests.get(url)


if response.status_code == 200:
    print(response.text)
else:
    print("Gagal mendapatkan konten dari URL")

@bot.on(events.NewMessage(pattern=r"(?:.menu|/start|/menu)$"))
@bot.on(events.CallbackQuery(data=b'menu'))
async def start_menu(event):
    user_id = str(event.sender_id)

    if check_user_registration(user_id):
        try:
            saldo_mu, level = get_saldo_and_level_from_db(user_id)

            if level == "user":
                member_inline = [
                    [Button.inline("🎲Ssh Menu🎲", "ssh")],
                    [Button.inline("🎲Vmess Menu🎲", "vmess-member"),
                     Button.inline("🎲Vless Menu🎲", "vless-member")],
                    [Button.inline("🎲Trojan Menu🎲", "trojan-member"),
                     Button.inline("🎲Socks Menu🎲", "shadowsocks-member")],
                    [Button.inline("🎲Noobzv Vpn🎲", "noobzvpn-member")],
                    [Button.url("contact", "https://t.me/mousethain"),
                     Button.inline("🕊topup manual🕊", f"topup")]
                ]

                member_msg = f"""
**━━━━━━━━━━━━━━━━**
╔═╗─╔╗────╔╗─╔╦═╦═╦╗
║╔╬╦╣╚╦═╦╦╣╚╦╝║╬║║║║
║╚╣║║╬║╩╣╔╩╗║╔╣╔╣║║║
╚═╬╗╠═╩═╩╝─╚═╝╚╝╚╩═╝
──╚═╝`•member panel•`
**━━━━━━━━━━━━━━━━**
**Notice:{response.text}**
**━━━━━━━━━━━━━━━━**
**  ➢SERVICE STATUS **
**» ssh status      :** `{get_ssh_status()}`
**» ssh xray        :** `{get_xray_status()}`
**» udp status      :** `{get_udp_status()}`
**» Noobzvpns status:** `{get_noobz_status()}`
**» slowdns status  :** `{get_slowdns_status()}`
**» dropbear status :** `{get_dropbear_status()}`
**» websocket status:** `{get_ws_status()}`
**» Anti DDoS status:** `{get_ddos_status()}`
**━━━━━━━━━━━━━━━━**
**» 🎲Version:** `v3.1.1`
**» 🎲contact:** `@mousethain`
**» 🎲Your ID ** `{user_id}`
**» 🎲Harga SSH    IDR.10.000 **
**» 🎲Harga VMESS  IDR.15.000 **
**» 🎲Harga VLESS  IDR.15.000 **
**» 🎲Harga TROJAN IDR.15.000 **
**» 🎲SISA SALDO MU: ** `RP.{saldo_mu}`
**━━━━━━━━━━━━━━━━**
"""
                x = await event.edit(member_msg, buttons=member_inline)
                if not x:
                    await event.reply(member_msg, buttons=member_inline)


            elif level == "admin":
                admin_inline = [
                    [Button.inline("🎲Ssh Menu🎲", "ssh")],
                    [Button.inline("🎲Vmess Menu🎲", "vmess"),
                     Button.inline("🎲Vless Menu🎲", "vless")],
                    [Button.inline("🎲Trojan Menu🎲", "trojan"),
                     Button.inline("🎲Socks Menu🎲", "shadowsocks")],
                    [Button.inline("🎲Noobz Vpn🎲", "noobzvpns"),
                     Button.inline("🎲Add Member🎲", "registrasi-member"),
                     Button.inline("🎲Del Member🎲", "delete-member")],
                     [Button.inline("🎲List Member🎲", "show-user")],
                    [Button.inline("🎲Add Saldo Member🎲", "addsaldo")],
                    [Button.inline("🖥️Check Vps Info🖥️", "info"),
                     Button.inline("⚙️Other Settings⚙️", "setting")],
                    [Button.url("contact", "https://t.me/mousethain")]
                ]

                admin_msg = f"""
**━━━━━━━━━━━━━━━━**
╔═╗─╔╗────╔╗─╔╦═╦═╦╗
║╔╬╦╣╚╦═╦╦╣╚╦╝║╬║║║║
║╚╣║║╬║╩╣╔╩╗║╔╣╔╣║║║
╚═╬╗╠═╩═╩╝─╚═╝╚╝╚╩═╝
──╚═╝`•admin panel•`
**━━━━━━━━━━━━━━━━**
**Notice:{response.text}**
**━━━━━━━━━━━━━━━━**
**  ➢SERVICE STATUS **
**» ssh status      :** `{get_ssh_status()}`
**» ssh xray        :** `{get_xray_status()}`
**» udp status      :** `{get_udp_status()}`
**» Noobzvpns status:** `{get_noobz_status()}`
**» slowdns status  :** `{get_slowdns_status()}`
**» dropbear status :** `{get_dropbear_status()}`
**» websocket status:** `{get_ws_status()}`
**» Anti DDoS status:** `{get_ddos_status()}`
**━━━━━━━━━━━━━━━━**
**» 🎲Version:** `v3.1.1`
**» 🎲contact:** `@mousethain`
**» 🎲Your ID ** `{user_id}`
**» 🎲Harga SSH    IDR.10.000 **
**» 🎲Harga VMESS  IDR.15.000 **
**» 🎲Harga VLESS  IDR.15.000 **
**» 🎲Harga TROJAN IDR.15.000 **
**» 🎲Total user in databases:** `{get_user_count()}`
**━━━━━━━━━━━━━━━━**
"""
                x = await event.edit(admin_msg, buttons=admin_inline)
                if not x:
                    await event.reply(admin_msg, buttons=admin_inline)

        except Exception as e:
            print(f"Error: {e}")

    else:
        await event.reply(
            f'```Anda belum terdaftar, silahkan registrasi```',
            buttons=[[(Button.inline("Registrasi", "registrasi"))]]
        )

