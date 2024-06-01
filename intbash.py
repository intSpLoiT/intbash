import os
import re
from termcolor import colored

# Kullanıcının metin rengini sadece bir kez girmesini sağlamak için bir değişken
user_text_color_set = False

def print_banner():
    try:
        import pyfiglet
        import termcolor
    except ImportError:
        print("Please install 'pyfiglet' and 'termcolor' packages to use this script.")
        return
    
    banner_art = """
⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⠶⠾⠿⠛⠛⠻⠿⠶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠇⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡈⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⡆⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⣧⢸⡆⢀⣀⣀⣤⡀⠀⠀⢀⣤⣀⣀⡀⠀⡟⣸⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣿⠁⣿⣿⣿⣿⡟⠀⠀⠸⣿⣿⣿⣿⠆⣿⠟⠀⠀⠀⣀⠀
⠀⢰⡟⢿⣆⠀⠀⣿⠀⠙⢿⣿⠟⠀⣠⣄⠀⠹⣿⣿⠟⠀⢹⠀⠀⣠⡿⢻⠀
⣠⡾⠃⠈⠻⢷⣦⣽⣄⡀⠀⠀⠀⢸⣿⣿⣧⠀⠀⠀⢀⣠⣿⣤⡶⠟⠁⠘⢿⣆
⠻⠷⠶⠶⣶⣤⣈⠙⠻⣿⣷⣦⠀⠸⠋⠙⠟⠀⣠⣾⣿⠟⠋⣁⣠⣴⠶⠶⠟
⠀⠀⠀⠀⠀⠉⠛⠿⣶⣼⠿⣿⣲⡤⡤⡤⢤⢰⣿⡏⣿⣶⠿⠛⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⡄⠻⣹⡟⡟⡟⣻⣻⠽⠁⣿⣦⣄⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣶⠾⠶⠾⠟⠋⣁⣼⣷⡀⠀⠉⠉⠉⠉⠀⢀⣼⣧⣀⠉⠛⠷⠶⠿⣶⠀
⠀⠀⠀⠀⠀⠙⣷⡄⢀⣴⠿⠛⠁⠀⠙⠳⠶⠤⠴⠶⠞⠋⠀⠈⠙⠻⣶⡄⠀⣾⠟⠀
⠀⠀⠀⠀⠀⢸⣷⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣶⡿⠀⠀⠀
-----------------------------------------------------------

___ _   _ _____ ___ _  __    _    __  __ ____  _ _ ____
|_ _| \\ | |_   _|_ _| |/ /   / \\  |  \\/  |___ \\/ ( ) ___|
 | ||  \\| | | |  | || ' /   / _ \\ | |\\/| | __) | |/\\___ \\
 | || |\\  | | |  | || . \\  / ___ \\| |  | |/ __/| |  ___) |
|___|_| \\_| |_| |___|_|\\_\\/_/   \\_\\_|  |_|_____|_| |____/
"""

    global user_text_color_set
    current_directory = os.getcwd()
    
    # Kullanıcı metin rengini henüz belirlemediyse sormak için
    if not user_text_color_set:
        user_text_color = input("Enter the color for user text (e.g., red, green, blue): ")
        user_text_color_set = True

    # Metin rengini sadece bir kez ayarla
    try:
        user_input_color = getattr(termcolor, user_text_color.lower())
    except AttributeError:
        print("Invalid color. Using default color.")
        user_input_color = "white"

    # Kullanıcı metni renkli yazdır
    print(colored(banner_art, user_input_color))

    prompt = f"┌──(intikam21-cyber@root[{colored(current_directory, 'cyan')}])\n  └─$ "
    user_text = input(prompt)

    # Eğer kullanıcı komutu, bir harf eksik veya fazlaysa çalıştırma
    if re.search(r'^ls$', user_text):
        os.system(f"echo {user_text} | figlet | lolcat")

if __name__ == "__main__":
    print_banner()