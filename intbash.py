import os

def print_banner():
    current_directory = os.getcwd()
    prompt = f"┌──(intikam21-cyber@root[{current_directory}]└─$ "
    user_text = input(prompt)
    os.system(f"echo {user_text} | figlet | lolcat")

if __name__ == "__main__":
    print_banner()