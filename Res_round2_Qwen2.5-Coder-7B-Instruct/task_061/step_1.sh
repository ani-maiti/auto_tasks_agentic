echo "Checking for the latest Debian stable release version..."
wget -qO- https://www.debian.org/distrib/netinst | grep -oP 'Debian \K\d+\.\d+' | head -n 1