def ShowRules():
    from rich.table import Table
    from rich.console import Console
    console = Console()

    table = Table(title="INBOUND RULES")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    table.add_column("Source IP", style="magenta")
    table.add_column("Destination IP", style="magenta")
    table.add_column("Port", style="magenta")
    table.add_column("Protocol", style="magenta")
    table.add_column("Rule", style="magenta")

    with open('InBound.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            rule = line.split(" ")
            try:
                table.add_row(rule[0],rule[1],rule[2],rule[3],rule[4],rule[5])
            except:
                print("WARNING: You have entered wrong input!")
    console.print(table)

    console = Console()

    table = Table(title="OUTBOUND RULES")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    table.add_column("Source IP", style="magenta")
    table.add_column("Destination IP", style="magenta")
    table.add_column("Port", style="magenta")
    table.add_column("Protocol", style="magenta")
    table.add_column("Rule", style="magenta")

    with open('OutBound.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
        for line in lines:
            rule = line.split(" ")
            try:
                table.add_row(rule[0],rule[1],rule[2],rule[3],rule[4],rule[5])
            except:
                print("WARNING: You have entered wrong input!")
    console.print(table)
    input('Press ENTER to continue\n')
    