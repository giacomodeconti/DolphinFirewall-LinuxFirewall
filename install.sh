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
echo "alias \dfw\='python3 /etc/dolphinfirewall/dfw/main.py'" >> ~/.bash_aliases
source ~/.bash_aliases
echo "alias \dfw\='python3 /etc/dolphinfirewall/dfw/main.py'" >> ~/.bashrc
source ~/.bashrc
alias dfw="python3 /etc/dolphinfirewall/dfw/main.py"
cd /etc/doplhinfirewall && sudo chmod - R 766 ./
cd
echo
echo
echo Installation succesful, type dfw to open firewall
echo
echo or run python3 /etc/dolphinfirewall/dfw/main.py
echo
