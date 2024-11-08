pip3 install requests

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

pkg install neofetch

python3 intbash.py