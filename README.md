
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

After installation main.pyc to execute the firewall.

```bash
# create iptables dir
sudo apt update -y && sudo apt upgrade -y
sudo mkdir /etc/iptables 

# create rules files for ipv4 and ipv6
sudo touch /etc/iptables/rulse.v4 && sudo chmod 666 /etc/iptables/rulse.v4 
sudo touch /etc/iptables/rulse.v6 && sudo chmod 666 /etc/iptables/rulse.v6

# install iptables persitent for saves
sudo apt install iptables-persistent

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
sudo git clone https://github.com/giacomodeconti/DolphinFirewall/dfw /etc/dolphinfirewall
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

MIT License

Copyright (c) 2022 Giacomo De Conti & Armando Battaglino

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software with restriction, including with limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

