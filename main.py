from rich.console import Console
from pathlib import Path
from db.manager import Manager
from receptionist import Receptionist
# from analyst import Analyst

import sys


def main(console: Console, receptionist: Receptionist, manager: Manager):
    while True:
        choice = receptionist.get_choice()
        match choice:
            case "Add":
                transaction = receptionist.deal_with_add()
                manager.add_transaction(*transaction)
                pass
            case "Remove":
                # transaction_id = receptionist.deal_with_remove()
                # manager.remove_transaction()
                pass
            case "Report":
                # receptionist.deal_with_report()
                # analyst.report() # Based on the receptionist result, log/report the transactions in a table/graph
                pass
            case "Exit":
                break


if __name__ == "__main__":
    console = Console()
    receptionist = Receptionist()
    bankPath = Path('db') / 'bank.parquet'
    console.rule("[bold italic yellow]Kapital", style="[yellow]")
    manager = Manager(bankPath, console)

    try:
        main(console, receptionist, manager)
    except KeyboardInterrupt:
        console.print("[bold italic red]\n\nGoodbye![/bold italic red]")
        sys.exit(0)

    
