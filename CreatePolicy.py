def CreatePolicy():
    from rich.console import Console
    from rich.table import Table
    import os
    rule=input("InBound or OutBound (I/O):\n")
    PolicyName=input("Policy name:\n")
    IPs=input("IP:\n")
    port=input("Port:\n")
    protocol=input("Protocol:\n")
    traffic=input("ALLOW/DROP:\n")
    
    console = Console()
    table = Table(title="Dolphin Firewall")

    table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    table.add_column("IP", style="magenta")
    table.add_column("Port", style="magenta")
    table.add_column("Protocol", style="magenta")
    table.add_column("Rule", style="magenta")

    table.add_row(PolicyName, IPs, port, protocol, traffic)
    if rule=="I":
        os.system(f"echo {PolicyName} {IPs} {port} {protocol} {traffic} >> InBound.txt")
        #add iptables command here
        os.system(f"sudo iptables -I INPUT -s {IPs} -j {traffic}")
    elif rule=="O":
        os.system(f"echo {PolicyName} {IPs} {port} {protocol} {traffic} >> OutBound.txt")
        #add iptables command here
        os.system(f"sudo iptables -I OUTPUT -s {IPs} -j {traffic}")

    console.print(table)