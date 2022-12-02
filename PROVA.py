import os

rule=input("InBound or OutBound (I/O):\n")

PolicyName = input("Policy name:\n")
IPs = input("IP source or all:\n")
IPd = input("IP destination or all:\n")
port = input("Port or all:\n")
protocol = input("Protocol:\n")
traffic = input("ACCEPT/DROP:\n")

if IPd == 'all':
  IPd = "0/0"

if IPs == 'all':
  IPs = "0/0"

if port == 'all':
  port = "1:65535"

if rule == "I":
  os.system(f"echo {PolicyName} {IPs} {IPd} {port} {protocol} {traffic} >> InBound.txt")
  
  #IL COMANDO RIMANE COSTANTE
  print(f"sudo iptables -I INPUT -s {IPs} -d {IPd} -p {protocol} --dport {port} -j {traffic}")
  if protocol != 'all':
    os.system(f"sudo iptables -I INPUT -s {IPs} -d {IPd} -p {protocol} --dport {port} -j {traffic}")
  elif protocol == 'all':
    os.system(f"sudo iptables -I INPUT -s {IPs} -d {IPd} -p tcp --dport {port} -j {traffic}")
    os.system(f"sudo iptables -I INPUT -s {IPs} -d {IPd} -p udp --dport {port} -j {traffic}")

elif rule == "O":
  os.system(f"echo {PolicyName} {IPs} {IPd} {port} {protocol} {traffic} >> OutBound.txt")

  # IL COMANDO RIMANE COSTANTE
  if protocol != 'all':
    os.system(f"sudo iptables -I OUTPUT -d {IPs} -d {IPd} -p {protocol} --dport {port} -j {traffic}")
  elif protocol == 'all':
    os.system(f"sudo iptables -I OUTPUT -d {IPs} -d {IPd} -p tcp --dport {port} -j {traffic}")
    os.system(f"sudo iptables -I OUTPUT -d {IPs} -d {IPd} -p udp --dport {port} -j {traffic}")



