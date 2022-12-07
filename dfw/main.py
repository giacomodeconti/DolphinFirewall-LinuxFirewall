from rich.console import Console
from rich.table import Table
import time
from status import status
from CreatePolicy import CreatePolicy
from seekRule import seekRule
from show import ShowRules
from delPolicy import delPolicy

console = Console()

console.print("""
                ,-._
              _.-'  '--.
            .'      _  -`\_
            / .----.`_.'----'
            ;/     `
    dfw   /_;

        ._      ._      ._
    _.-._)`\_.-._)`\_.-._)`\_.-._
    
    Created by 
    - Giacomo De Conti  giacomodeconti.gdc@gmail.com
    - Armando Battaglino  battaglino.dev@gmail.com

    # For source code or more info contact us!

    """, style="blue")
while 1==1:
    table = Table(title="Dolphin Firewall")

    table.add_column("Key", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")

    table.add_row("1", "Create Policy")
    table.add_row("2", "Delete Policy")
    table.add_row("3", "Show Rules")
    table.add_row("4", "Show Status")
    table.add_row("5", "EXIT", style="red")

    console.print(table)

    respond=input()
    if respond == '1':
        CreatePolicy()
    elif respond == '2':
        delPolicy()
    elif respond == '3':
        ShowRules()
    elif respond == '4':
        status()
    elif respond == '5':
        console.print('\n--!! EXIT !!--\n', style="red on yellow")
        time.sleep(1)
        break
    else:
         console.print('\n--!!WRONG NUMBER!!--\n', style="red on yellow")
         time.sleep(2)

