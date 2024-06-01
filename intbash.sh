#!/bin/bash

# Gerekli paketleri yükle
pkg update
pkg install -y figlet
pkg install -y ruby
pkg install -y git
gem install lolcat

# ~/.termux/ dizinini oluştur
mkdir -p ~/.termux

# Termux başlangıç scriptini oluştur
cat <<EOT > ~/.termux/termux-startup.sh
#!/bin/bash
python ~/intbash/intbash.py
EOT

# Termux başlangıç scriptini çalıştırılabilir yap
chmod +x ~/.termux/termux-startup.sh

# Termux başlangıç komutunu ayarla
if ! grep -Fxq "source ~/.termux/termux-startup.sh" ~/.bashrc
then
    echo "source ~/.termux/termux-startup.sh" >> ~/.bashrc
fi