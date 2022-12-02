def CreatePolicy():
    from rich.console import Console
    from rich.table import Table
    import os

    console = Console()

    rule=input("InBound or OutBound (I/O):\n")

    console.print("For IP and Port input to select all, type --> all", style="red on white")

    PolicyName=input("Policy name:\n")
    IPs=input("IP:\n")
    port=input("Port:\n")
    protocol=input("Protocol:\n")
    traffic=input("ACCEPT/DROP:\n")
    
    table = Table(title="Dolphin Firewall")

    table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    table.add_column("IP", style="magenta")
    table.add_column("Port", style="magenta")
    table.add_column("Protocol", style="magenta")
    table.add_column("Rule", style="magenta")

    table.add_row(PolicyName, IPs, port, protocol, traffic)
    if rule=="I":
        os.system(f"echo {PolicyName} {IPs} {port} {protocol} {traffic} >> InBound.txt")
        #add iptables command her
        if IPs=='all':
            #add port and protocol command 
            os.system(f"sudo iptables -I INPUT -p {protocol} --destination-port {port} -j {traffic}")
        elif port=='all':  
            #add IP and protocol command
            os.system(f"sudo iptables -I INPUT -s {IPs} -p {protocol} -j {traffic}")
        elif protocol=='all':
            #add IP and port command
            os.system(f"sudo iptables -I INPUT -s {IPs} --destination-port {port} -j {traffic}")
        elif IPs and port=='all':
            #add protocol command
            os.system(f"sudo iptables -I INPUT -p {protocol} -j {traffic}")
        elif protocol and port=='all':
            #add IP command
            os.system(f"sudo iptables -I INPUT -s {IPs} -j {traffic}")
        elif IPs and protocol=='all':
            #add port command
            os.system(f"sudo iptables -I INPUT --destination-port {port} -j {traffic}")
        elif IPs and port and protocol=='all':
            #all parameters
            os.system(f"sudo iptables -I INPUT -j {traffic}")
        elif IPs and port and protocol!='all':
            #one by one
            os.system(f"sudo iptables -I INPUT -s {IPs} -p {protocol} --destination-port {port} -j {traffic}")
            
    # OUTPUT RULE
    elif rule=="O":
        os.system(f"echo {PolicyName} {IPs} {port} {protocol} {traffic} >> OutBound.txt")
    
        os.system(f"sudo iptables -I OUTPUT -s {IPs} -j {traffic}")

    console.print(table)



    