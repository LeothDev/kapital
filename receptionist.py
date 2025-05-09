from rich.prompt import Prompt
from rich.prompt import Confirm
from rich.console import Console
from datetime import datetime

class Receptionist():
    def __init__(self, console: Console):
        self.console = console

    
    def get_choice(self):
        self.console.print("\n[bold]Available actions:[/bold]")
        map_choices = {
            "Add transaction": "Add",
            "View transactions": "Report",
            "Remove transaction": "Remove",
            "Exit": "Exit",
        }
        choices = ["Add transaction", "Remove transaction", "View transactions", "Exit"]

        for i, choice in enumerate(choices, 1):
            self.console.print(f"[italic cyan]{i}. {choice}[/italic cyan]")

        while True:
            try:
                choice = Prompt.ask(
                    "What would you like to do? (number or action)",
                    # choices=choices,
                    default="Add transaction",
                    case_sensitive=False,
                )
                if choice.isdigit():
                    index = int(choice) - 1
                    return map_choices[choices[index]]
                else:
                    return map_choices[choice]
            except (ValueError, IndexError, KeyError):
                self.console.print(
                    "[red]Invalid selection. Please enter a valid action or number.[/red]"
                )

    def deal_with_add(self):
        self.console.rule("[bold italic red]\nOperating in the Bank", style="[red]")

        date = Prompt.ask(
            "[bright_cyan italic]Insert the date of the transaction [DD/MM/YYYY H/m]: ",
            default = "",
        )
        amount = Prompt.ask(
            "Insert [bright_cyan italic]amount of transaction: ",
            default = "0"
        )

        currency = Prompt.ask(
            "Insert the [bright_cyan italic]currency: ",
            default = "€"
        )

        recipient = Prompt.ask(
            "Insert the [bright_cyan italic]recipient: ",
            default = ""
        )

        category = Prompt.ask(
            "Insert [bright_cyan italic]category: ",
            default = "General Expenses"
        )

        method = Prompt.ask(
            "Insert method [bright_cyan italic]of payment: ",
            default = "Card"
        )

        if method == "Card":
            cardN = Prompt.ask(
                "[bright_cyan italic]Last 4 digits of your card: ",
                default = ""
            )
        

        # Consider printing a summary and complete the is_ok control
        is_ok = Confirm.ask(
            "Are the information correct?\n"
        )
        if is_ok: 
            pass

        
        return [date, amount, currency, recipient, category, method, cardN]

    def deal_with_view(self):
        pass
