import pyrogram
from pyrogram import Client

srijan = '''
░██████╗██████╗░██╗░░░░░██╗░█████╗░███╗░░██╗
██╔════╝██╔══██╗██║░░░░░██║██╔══██╗████╗░██║
╚█████╗░██████╔╝██║░░░░░██║███████║██╔██╗██║
░╚═══██╗██╔══██╗██║██╗░░██║██╔══██║██║╚████║
██████╔╝██║░░██║██║╚█████╔╝██║░░██║██║░╚███║
╚═════╝░╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝
'''

trollface = '''
⠀⠀⠀⠀⠀⠀⢀⣤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⢤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡼⠋⠀⣀⠄⡂⠍⣀⣒⣒⠂⠀⠬⠤⠤⠬⠍⠉⠝⠲⣄⡀⠀⠀
⠀⠀⠀⢀⡾⠁⠀⠊⢔⠕⠈⣀⣀⡀⠈⠆⠀⠀⠀⡍⠁⠀⠁⢂⠀⠈⣷⠀⠀
⠀⠀⣠⣾⠥⠀⠀⣠⢠⣞⣿⣿⣿⣉⠳⣄⠀⠀⣀⣤⣶⣶⣶⡄⠀⠀⣘⢦⡀
⢀⡞⡍⣠⠞⢋⡛⠶⠤⣤⠴⠚⠀⠈⠙⠁⠀⠀⢹⡏⠁⠀⣀⣠⠤⢤⡕⠱⣷
⠘⡇⠇⣯⠤⢾⡙⠲⢤⣀⡀⠤⠀⢲⡖⣂⣀⠀⠀⢙⣶⣄⠈⠉⣸⡄⠠⣠⡿
⠀⠹⣜⡪⠀⠈⢷⣦⣬⣏⠉⠛⠲⣮⣧⣁⣀⣀⠶⠞⢁⣀⣨⢶⢿⣧⠉⡼⠁
⠀⠀⠈⢷⡀⠀⠀⠳⣌⡟⠻⠷⣶⣧⣀⣀⣹⣉⣉⣿⣉⣉⣇⣼⣾⣿⠀⡼⠀
⠀⠀⠀⠈⢳⡄⠀⠀⠘⠳⣄⡀⡼⠈⠉⠛⡿⠿⠿⡿⠿⣿⢿⣿⣿⡇⠀⡇⠀
⠀⠀⠀⠀⠀⠙⢦⣕⠠⣒⠌⡙⠓⠶⠤⣤⣧⣀⣸⣇⣴⣧⠾⠾⠋⠀⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠶⣭⣒⠩⠖⢠⣤⠄⠀⠀⠀⠀⠀⠠⠔⠁⡰⠀⣧⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⢤⣀⣀⠉⠉⠀⠀⠀⠀⠀⠁⠀⣠⠏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠒⠲⠶⠤⠴⠒⠚⠁⠀⠀
'''

print(srijan)
api_id = input("Enter Your API ID: \n")
api_hash = input("Enter Your API HASH : \n")

with Client("Srijan", api_id=api_id, api_hash=api_hash) as bot_:
    channel_username = "OriginalSrijan" 
    try:
        bot_.join_chat(channel_username)
        print(f"Successfully joined the channel: @{channel_username}")
    except Exception as e:
        print(f"Failed to join channel: {e}")

    # Generate session string and send it to saved messages
    first_name = (bot_.get_me()).first_name
    string_session_ = f"<b>String Session For {first_name}</b> \nSubscribe To @OriginalSrijan, Otherwise you will die single 💀 \n<code>{bot_.export_session_string()}</code>"
    bot_.send_message("me", string_session_)
    print(f"String has been sent to your saved messages: {first_name}")

print(trollface)
