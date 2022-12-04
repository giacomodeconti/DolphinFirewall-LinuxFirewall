def status():
    import time
    import os
    from rich.console import Console
    from rich.table import Table
    n=1
    while n==1:
        console = Console()
        table = Table(title="Dolphin Firewall")

        table.add_column("Key", justify="right", style="cyan", no_wrap=True)
        table.add_column("Title", style="magenta")

        table.add_row("1", "Enable Firewall")
        table.add_row("2", "Disable Firewall")
        table.add_row("3", "BACK", style="red")

        console.print(table)

        console = Console()

        table = Table(title="Firewall Status")
        table.add_column("Firewall", justify="right", style="cyan", no_wrap=True)
        table.add_column("Status", style="magenta")
        
        table.add_row("Firewall State", ":heavy_check_mark:" )
        table.add_row("Firewall State", ":cross_mark:" )


        console.print(table)

        respond=input('')
        if respond == '1':
            print('Working ...')
            os.system("sudo systemctl enable netfilter-persistent.service")
            os.system("sudo systemctl enable iptables")
            os.system("sudo systemctl enable ip6tables")
            time.sleep(2)
            console.print('--!! ENABLED !!--', style="green")
        elif respond == '2':
            print('Working ...')
            os.system("sudo systemctl disable netfilter-persistent.service")
            os.system("sudo systemctl disable iptables")
            os.system("sudo systemctl disable ip6tables")
            time.sleep(2)
            console.print('--!! DISABLED !!--', style="red")
        elif respond == '3':
            n = n+1
            print("")
        else:
            console.print('\n--!!WRONG NUMBER!!--\n', style="red on yellow")
            time.sleep(2)
        