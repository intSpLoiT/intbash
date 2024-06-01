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
    
    current_directory = colored(os.getcwd(), 'cyan', attrs=['bold'])
    prompt = f"┌──(intikam21-cyber@root[{current_directory}]"
    prompt += """
└─$ """
    
    print(colored(banner_art, 'magenta'))
    
    # Kullanıcının metin rengini sadece bir kez ayarla
    global user_text_color_set
    if not user_text_color_set:
        user_text_color = input("Enter the color for user input (e.g., red, green, blue): ")
        user_text_color_set = True

    user_input = input(prompt)
    
    # Eğer kullanıcının girdiği kelime benzer bir komut adıysa, o komutu çalıştırma
    if not re.match(r'^\s*$', user_input):
        print(f"Executing: {user_input}")
        os.system(user_input)
        
        # Kullanıcının girdiği metin rengiyle yazdırma
        print(colored(user_input, user_text_color))
        
    else:
        print("No input provided. Please enter a command.")
    
if __name__ == "__main__":
    while True:
        print_banner()