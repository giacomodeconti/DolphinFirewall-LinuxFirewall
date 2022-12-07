def CreatePolicy():
    from rich.console import Console
    from rich.table import Table
    import os

    console = Console()

    rule=input("InBound or OutBound (I/O):\n")

    console.print("For IP, Port and Protocl input to select all, type --> all", style="red on white")

    PolicyName = input("Policy name:\n")
    IPs = input("IP source or all:\n")
    IPd = input("IP destination or all:\n")
    port = input("Port or all:\n")
    protocol = input("Protocol:\n")
    traffic = input("ACCEPT/DROP:\n")

    table = Table(title="Dolphin Firewall")

    table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    table.add_column("IPs", style="magenta")
    table.add_column("IPd", style="magenta")
    table.add_column("Port", style="magenta")
    table.add_column("Protocol", style="magenta")
    table.add_column("Rule", style="magenta")

    table.add_row(PolicyName, IPs, IPd, port, protocol, traffic)

    if IPd == 'all':
        IPd = "0/0"

    if IPs == 'all':
        IPs = "0/0"

    if port == 'all':
        port = "1:65535"

    # TO DO:
    # SI PUò MIGLIORARE LA SCRITTURA DEL FILE PERCHé NON è NECESSARIO ECHO
    # INVECE CHE ECHO UTILIZZARE --->
    # SI RIDURREBBE IN QUESTO MODO AD UNA SOLA SCRITTURA DI FILE IMPOSTANDO IL FILE COME VARIABILE, DIMEZZANDO COSì IL CODICE SEGUENTE


    if rule == "I":
    #icmp requests
        if protocol=='icmp':
            os.system(f"sudo iptables -I INPUT -j {traffic} -s {IPs} -d {IPd} -p {protocol} --icmp-type echo-request")
            os.system("sudo /sbin/iptables-save >> /etc/iptables/rules.v4")

        elif protocol == 'all':
            os.system(f"sudo iptables -I INPUT -s {IPs} -d {IPd} -p tcp --dport {port} -j {traffic}")
            os.system("sudo /sbin/iptables-save >> /etc/iptables/rules.v4")
            os.system(f"sudo iptables -I INPUT -s {IPs} -d {IPd} -p udp --dport {port} -j {traffic}")
            os.system("sudo /sbin/iptables-save >> /etc/iptables/rules.v4")
        else:
            os.system(f"sudo iptables -I INPUT -s {IPs} -d {IPd} -p {protocol} --dport {port} -j {traffic}")
            os.system("sudo /sbin/iptables-save >> /etc/iptables/rules.v4")

        os.system(f"echo {PolicyName} {IPs} {IPd} {port} {protocol} {traffic} >> InBound.txt")

    elif rule == "O":
        if protocol == 'icmp':
            os.system(f"sudo iptables -I OUTPUT -j {traffic} -s {IPs} -d {IPd} -p {protocol} --icmp-type echo-reply")
            os.system("sudo /sbin/iptables-save >> /etc/iptables/rules.v4")
        elif protocol == 'all':
            os.system(f"sudo iptables -I OUTPUT -s {IPs} -d {IPd} -p tcp --dport {port} -j {traffic}")
            os.system("sudo /sbin/iptables-save >> /etc/iptables/rules.v4")
            os.system(f"sudo iptables -I OUTPUT -s {IPs} -d {IPd} -p udp --dport {port} -j {traffic}")
            os.system("sudo /sbin/iptables-save >> /etc/iptables/rules.v4")
        else:
            os.system(f"sudo iptables -I OUTPUT -s {IPs} -d {IPd} -p {protocol} --dport {port} -j {traffic}")
            os.system("sudo /sbin/iptables-save >> /etc/iptables/rules.v4")

        os.system(f"echo {PolicyName} {IPs} {IPd} {port} {protocol} {traffic} >> OutBound.txt")

    console.print(table)

