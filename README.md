![Alt text](https://github.com/giacomodeconti/giacomodeconti/blob/main/screen1.jpg "Optional Title")
![Alt text](https://github.com/giacomodeconti/giacomodeconti/blob/main/screen.jpg "Optional Title")

# Dolphin Firewall

A Firewall for linux

# Works on:

Debian

Ubuntu

## Features

- Create policy
- Delete policy
- Show all rules
- Enable/Disable firewall


## Installation

Run install.sh file or run every single command inside of it.

After installation run main.pyc to execute the firewall.

```bash
# create iptables dir
sudo apt update -y && sudo apt upgrade -y
sudo mkdir /etc/iptables 

# install iptables persitent for saves
sudo apt install iptables-persistent

# create rules files for ipv4 and ipv6
sudo touch /etc/iptables/rulse.v4 && sudo chmod 666 /etc/iptables/rulse.v4 
sudo touch /etc/iptables/rulse.v6 && sudo chmod 666 /etc/iptables/rulse.v6

# enable netfilter persistent
sudo systemctl enable netfilter-persistent.service

# enable iptables services
sudo systemctl enable iptables
sudo systemctl enable ip6tables

# config iptables
sudo iptables -P INPUT ACCEPT && sudo iptables -P FORWARD ACCEPT && sudo iptables -P OUTPUT ACCEPT && sudo iptables -F

#install rich library python
sudo apt install python3-pip -y
pip install rich

#download dolphin firewall repo
sudo mkdir /etc/dolphinfirewall
sudo git clone https://github.com/giacomodeconti/DolphinFirewall-LinuxFirewall /etc/dolphinfirewall
alias dfw="python3 /etc/dolphinfirewall/main.py"
echo "alias \dfw\='python3 /etc/dolphinfirewall/main.py'" >> ~/.bash_aliases
source ~/.bash_aliases
echo "alias \dfw\='python3 /etc/dolphinfirewall/main.py'" >> ~/.bashrc
source ~/.bashrc
cd /etc/doplhinfirewall && sudo chmod - R 766 ./
```








## Authors

- [@giacomo](https://github.com/giacomodeconti)
- [@armando](https://github.com/ArmandoBattaglino)


## Feedback

If you have any feedback email us:

Giacomo: giacomodeconti.gdc@gmail.com

Armando: battaglino.dev@gmail.com


## License

Copyright 2022, Giacomo De Conti & Armando Battaglino, All rights reserved.
