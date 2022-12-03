# create iptables dir
sudo mkdir /etc/iptables 

# create rules files for ipv4 and ipv6
sudo touch /etc/iptables/rulse.v4 && chmod 777 /etc/iptables/rulse.v4 
sudo touch /etc/iptables/rulse.v6 && chmod 777 /etc/iptables/rulse.v6

# install iptables persitent for saves
sudo apt install iptables-persistent

# enable netfilter persistent
sudo systemctl enable netfilter-persistent.service

# enable iptables services
sudo systemctl enable iptables
sudo systemctl enable ip6tables

# enable on boot
sudo chkconfig netfilter-persistent.service on
sudo chkconfig iptables on
sudo chkconfig ip6tables on

# config iptables
sudo iptables -P INPUT ACCEPT && sudo iptables -P FORWARD ACCEPT && sudo iptables -P OUTPUT ACCEPT && sudo iptables -F