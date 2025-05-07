from rich.prompt import Prompt
from rich.console import Console

# from rich.rule import Rule
import sys

console = Console()


def get_choice():
    console.print("\n[bold]Available actions:[/bold]")
    map_choices = {
        "Add transaction": "Add",
        "View transactions": "Report",
        "Exit": "Exit",
    }
    choices = ["Add transaction", "View transactions", "Exit"]

    for i, choice in enumerate(choices, 1):
        console.print(f"[italic]{i}. {choice}[/italic]")

    while True:
        try:
            choice = Prompt.ask(
                "What would you like to do? (number or action)",
                # choices=choices,
                default="Add transaction",
                case_sensitive=False,
            )
            if choice.isdigit():
                return map_choices[choices[int(choice) - 1]]
            else:
                return map_choices(choice)
        except (ValueError, IndexError):
            console.print("[red]Invalid selection. Please try again.[/red]")


def main():
    while True:
        choice = get_choice()
        if choice == "Add":
            # tracker.add_transaction()
            pass
        elif choice == "Report":
            # tracker.report()
            pass
        else:
            break


if __name__ == "__main__":
    console.rule("[bold italic yellow]Kapital", style="[yellow]")
    try:
        main()
    except KeyboardInterrupt:
        console.print("[bold italic red]\n[!] Exiting. Goodbye![/bold italic red]")
        sys.exit(0)
