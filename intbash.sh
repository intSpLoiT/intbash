#!/bin/bash

# Install requests module for Python
pip3 install requests

# Make the scripts executable and move them to $PREFIX/bin
chmod +x intconsole
mv intconsole $PREFIX/bin/intconsole
chmod +x help
mv help $PREFIX/bin/help
chmod +x oip
mv oip $PREFIX/bin/oip
chmod +x intmap
mv intmap $PREFIX/bin/intmap
chmod +x intweb
mv intweb $PREFIX/bin/intweb
chmod +x intbrute
mv intbrute $PREFIX/bin/intbrute
chmod +x intdc
mv intdc $PREFIX/bin/intdc
chmod +x intdiscord
mv intdiscord $PREFIX/bin/intdiscord
chmod +x intpygen
mv intpygen $PREFIX/bin/intpygen
chmod +x 

# Install neofetch
pkg install neofetch

# Prompt the user to install IntFramework (though not actually installing it here)
read -p "Do you want to install IntFramework? [y/n]: " answer
if [[ "$answer" == "y" || "$answer" == "Y" ]]; then
    # Update and upgrade the package list
    pkg update && pkg upgrade -y
    
    # Install necessary packages
    pkg install python3
    pkg install git
    
    # Install requests module again in case it's needed
    pip3 install requests
    
    # Clone the IntFramework repository (optional, not required if you don't want to install the full framework)
    git clone https://github.com/Intikam21kurucu/intframework
    cd intframework
    
    # Make intbash setup script executable
    chmod +x intbash.sh
    
    # Run the intbash setup
    ./intbash.sh
    
    # Start the intbash framework
    python3 intbash.py
else
    echo "IntFramework installation skipped."
cd ~
fi