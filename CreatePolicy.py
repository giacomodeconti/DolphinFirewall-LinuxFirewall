def CreatePolicy():
    from rich.console import Console
    from rich.table import Table
    import os

    console = Console()
    print('Setting up Firewall...\nGice sudo passwd if necessary')
    os.system("sudo iptables -P INPUT ACCEPT && sudo iptables -P FORWARD ACCEPT && sudo iptables -P OUTPUT ACCEPT && sudo iptables -F")

    rule=input("InBound or OutBound (I/O):\n")

    console.print("For IP and Port input to select all, type --> all", style="red on white")

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

    if rule == "I":
        os.system(f"echo {PolicyName} {IPs} {IPd} {port} {protocol} {traffic} >> InBound.txt")
    
    #IL COMANDO RIMANE COSTANTE
    #print(f"sudo iptables -I INPUT -s {IPs} -d {IPd} -p {protocol} --dport {port} -j {traffic}")
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


    console.print(table)
    '''
    # INPUT ROLES
    if rule=="I":
        os.system(f"echo {PolicyName} {IPs} {port} {protocol} {traffic} >> InBound.txt")
        
        if IPs=='all' and port!='all' and protocol!='all':
            #add port and protocol command 
            print("IPs=='all' and port!='all' and protocol!='all'")
            os.system(f"sudo iptables -I INPUT -p {protocol} --destination-port {port} -j {traffic}")

        elif IPs!='all' and port=='all' and protocol!='all':  
            #add IP and protocol command
            print("IPs!='all' and port=='all' and protocol!='all'")
            os.system(f"sudo iptables -I INPUT -s {IPs} -p {protocol} -j {traffic}")

        elif IPs!='all' and port!='all' and protocol=='all': 
            #add IP and port command
            print("IPs!='all' and port!='all' and protocol=='all'")
            os.system(f"sudo iptables -I INPUT -s {IPs} -p tcp --destination-port {port} -j {traffic}")
            os.system(f"sudo iptables -I INPUT -s {IPs} -p udp --destination-port {port} -j {traffic}")

        elif IPs=='all' and port=='all' and protocol!='all':
            #add protocol command
            print("IPs=='all' and port=='all' and protocol!='all'")
            os.system(f"sudo iptables -I INPUT -p {protocol} -j {traffic}")

        elif IPs!='all' and port=='all' and protocol=='all':
            #add IP command
            print("IPs!='all' and port=='all' and protocol=='all'")
            os.system(f"sudo iptables -I INPUT -s {IPs} -j {traffic}")

        elif IPs=='all' and port!='all' and protocol=='all':
            #add port command
            print("IPs=='all' and port!='all' and protocol=='all'")
            os.system(f"sudo iptables -I INPUT -p tcp --destination-port {port} -j {traffic}")
            os.system(f"sudo iptables -I INPUT -p udp --destination-port {port} -j {traffic}")

        elif IPs=='all' and port=='all' and protocol=='all':
            #all parameters
            print("IPs=='all' and port=='all' and protocol=='all'")
            os.system(f"sudo iptables -I INPUT -j {traffic}")

        elif IPs!='all' and port!='all' and protocol!='all':
            #one by one
            print("IPs!='all' and port!='all' and protocol!='all'")
            os.system(f"sudo iptables -I INPUT -s {IPs} -p {protocol} --destination-port {port} -j {traffic}")
            
    # OUTPUT RULES
    elif rule=="O":
        os.system(f"echo {PolicyName} {IPs} {port} {protocol} {traffic} >> OutBound.txt")

        if IPs=='all' and port!='all' and protocol!='all':
            #add port and protocol command 
            print("IPs=='all' and port!='all' and protocol!='all'")
            os.system(f"sudo iptables -I INPUT -p {protocol} --destination-port {port} -j {traffic}")

        elif IPs!='all' and port=='all' and protocol!='all':  
            #add IP and protocol command
            print("IPs!='all' and port=='all' and protocol!='all'")
            os.system(f"sudo iptables -I INPUT -s {IPs} -p {protocol} -j {traffic}")

        elif IPs!='all' and port!='all' and protocol=='all': 
            #add IP and port command
            print("IPs!='all' and port!='all' and protocol=='all'")
            os.system(f"sudo iptables -I INPUT -s {IPs} -p tcp --destination-port {port} -j {traffic}")
            os.system(f"sudo iptables -I INPUT -s {IPs} -p udp --destination-port {port} -j {traffic}")

        elif IPs=='all' and port=='all' and protocol!='all':
            #add protocol command
            print("IPs=='all' and port=='all' and protocol!='all'")
            os.system(f"sudo iptables -I INPUT -p {protocol} -j {traffic}")

        elif IPs!='all' and port=='all' and protocol=='all':
            #add IP command
            print("IPs!='all' and port=='all' and protocol=='all'")
            os.system(f"sudo iptables -I INPUT -s {IPs} -j {traffic}")

        elif IPs=='all' and port!='all' and protocol=='all':
            #add port command
            print("IPs=='all' and port!='all' and protocol=='all'")
            os.system(f"sudo iptables -I INPUT -p tcp --destination-port {port} -j {traffic}")
            os.system(f"sudo iptables -I INPUT -p udp --destination-port {port} -j {traffic}")

        elif IPs=='all' and port=='all' and protocol=='all':
            #all parameters
            print("IPs=='all' and port=='all' and protocol=='all'")
            os.system(f"sudo iptables -I INPUT -j {traffic}")

        elif IPs!='all' and port!='all' and protocol!='all':
            #one by one
            print("IPs!='all' and port!='all' and protocol!='all'")
            os.system(f"sudo iptables -I INPUT -s {IPs} -p {protocol} --destination-port {port} -j {traffic}")

    console.print(table)
'''


    