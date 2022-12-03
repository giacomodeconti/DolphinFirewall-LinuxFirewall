def CreatePolicy():
    from rich.console import Console
    from rich.table import Table
    import os

    console = Console()
    #print('Setting up Firewall...\nGice sudo passwd if necessary')
    #os.system("sudo iptables -P INPUT ACCEPT && sudo iptables -P FORWARD ACCEPT && sudo iptables -P OUTPUT ACCEPT && sudo iptables -F")

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

    # SI PUò MIGLIORARE LA SCRITTURA DEL FILE PERCHé NON è NECESSARIO ECHO
    # INVECE CHE ECHO UTILIZZARE ---> 
    # SI RIDURREBBE IN QUESTO MODO AD UNA SOLA SCRITTURA DI FILE IMPOSTANDO IL FILE COME VARIABILE, DIMEZZANDO COSì IL CODICE SEGUENTE
    if rule == "I":
        os.system(f"echo {PolicyName} {IPs} {IPd} {port} {protocol} {traffic} >> InBound.txt")

    #icmp requests
        if protocol=='icmp':
            os.system(f"sudo iptables -I INPUT -j {traffic} -s {IPs} -d {IPd} -p {protocol} --icmp-type echo-request")

            #DA ELIMINARE
            """
            icmp=input('\n1) Block InBound icmp requests\n2) Block OutBound icmp requests\n')
            if icmp == '1':
                os.system(f"sudo iptables -I INPUT -j {traffic} -s {IPs} -d {IPd} -p {protocol} --icmp-type echo-request")
                #os.system(f"sudo iptables -I INPUT -j DROP -p icmp --icmp-type echo-request")
            if icmp == '2':
                os.system(f"sudo iptables -I OUTPUT -j {traffic} -s {IPs} -d {IPd} -p {protocol} --icmp-type echo-reply")
            """

        elif protocol == 'all':
            os.system(f"sudo iptables -I INPUT -s {IPs} -d {IPd} -p tcp --dport {port} -j {traffic}")
            os.system(f"sudo iptables -I INPUT -s {IPs} -d {IPd} -p udp --dport {port} -j {traffic}")
        else:
            os.system(f"sudo iptables -I INPUT -s {IPs} -d {IPd} -p {protocol} --dport {port} -j {traffic}")
    
    #SI PUò MIGLIORARE LA SCRITTURA DEL FILE PERCHé NON è NECESSARIO ECHO
    elif rule == "O":
        os.system(f"echo {PolicyName} {IPs} {IPd} {port} {protocol} {traffic} >> OutBound.txt")

    # IL COMANDO RIMANE COSTANTE
        if protocol == 'icmp':
            os.system(f"sudo iptables -I OUTPUT -j {traffic} -s {IPs} -d {IPd} -p {protocol} --icmp-type echo-reply")
            
            #DA ELIMINARE
            """
            icmp=input('\n1) Block InBound icmp requests\n2) Block OutBound icmp requests\n')
            if icmp == '1':
                os.system(f"sudo iptables -I INPUT -j {traffic} -s {IPs} -d {IPd} -p {protocol} --icmp-type echo-request")
                #os.system(f"sudo iptables -I INPUT -j DROP -p icmp --icmp-type echo-request")
            if icmp == '2':
                os.system(f"sudo iptables -I OUTPUT -j {traffic} -s {IPs} -d {IPd} -p {protocol} --icmp-type echo-reply")
            """

        elif protocol == 'all':
            os.system(f"sudo iptables -I INPUT -s {IPs} -d {IPd} -p tcp --dport {port} -j {traffic}")
            os.system(f"sudo iptables -I INPUT -s {IPs} -d {IPd} -p udp --dport {port} -j {traffic}")
        else:
            os.system(f"sudo iptables -I INPUT -s {IPs} -d {IPd} -p {protocol} --dport {port} -j {traffic}")

        #DA ELIMINARE
        """
        if protocol != 'all':
            os.system(f"sudo iptables -I OUTPUT -d {IPs} -d {IPd} -p {protocol} --dport {port} -j {traffic}")
        elif protocol == 'all':
            os.system(f"sudo iptables -I OUTPUT -d {IPs} -d {IPd} -p tcp --dport {port} -j {traffic}")
            os.system(f"sudo iptables -I OUTPUT -d {IPs} -d {IPd} -p udp --dport {port} -j {traffic}")
        """

    console.print(table)

