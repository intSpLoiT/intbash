#!/bin/bash
# Bu betik Termux başlatıldığında çalışır.

# ASCII sanatınızın yer alacağı kutuyu oluşturun.
echo "#############################################"
echo "#                                           #"
echo "#  ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⠶⠾⠿⠛⠛⠻⠿⠶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀
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
⠀⠀⣶⠾⠶⠾⠟⠋⣁⣼⣷⡀⠀⠉⠉⠉⠉⠀⢀⣼⣧⣀⠉⠛⠷⠶⠿⣶⠀
⠀⠀⠙⣷⡄⢀⣴⠿⠛⠁⠀⠙⠳⠶⠤⠴⠶⠞⠋⠀⠈⠙⠻⣶⡄⠀⣾⠟⠀
⠀⠀⠀⢸⣷⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣶⡿⠀⠀⠀
-----------------------------------------------------------

___ _   _ _____ ___ _  __    _    __  __ ____  _ _ ____
|_ _| \ | |_   _|_ _| |/ /   / \  |  \/  |___ \/ ( ) ___|
 | ||  \| | | |  | || ' /   / _ \ | |\/| | __) | |/\___ \
 | || |\  | | |  | || . \  / ___ \| |  | |/ __/| |  ___) |
|___|_| \_| |_| |___|_|\_\/_/   \_\_|  |_|_____|_| |____/
 #"
echo "#                                           #"
echo "#############################################"

# Özel input satırınızı ekleyin.
PS1='┌──(intikam21-cyber@root\[\\w\])\n└─$ '

# Kullanıcıdan bir girdi bekleyin.
read -p "$PS1" input

# Kullanıcının girdisini kontrol edin.
if [[ $input == "intconsole" ]]; then
    # İntframework dizinine geçiş yapın.
    cd İntframework

    # intconsoleV2.py dosyasını çalıştırın.
    if [[ -f "intconsoleV2.py" ]]; then
        python3 intconsoleV2.py
    else
        # Dosya mevcut değilse, GitHub deposundan indirin.
        echo "intconsoleV2.py bulunamadı. GitHub deposundan indiriliyor..."
        git clone https://github.com/Intikam21kurucu/intframework
        cd intframework
        python3 intconsoleV2.py
    fi
else
    # Diğer komutlar için genel bir işlem yapın.
    # Örneğin, kullanıcının girdiği komutu terminalde çalıştırın.
    eval $input
fi
