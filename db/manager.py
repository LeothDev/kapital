import uuid
import polars as pl
from pathlib import Path
from rich.console import Console


class Manager:
    def __init__(self, parquet_path: Path, console: Console):
        self.parquet_path = parquet_path
        self.console = console

        if parquet_path.exists():
            # self.df = pl.read_parquet_schema(parquet_path)
            self.df = pl.read_parquet(parquet_path)
        else:
            console.print(
                f"The file [bold italic yellow]{parquet_path}[/bold italic yellow] does not exist. Creating..."
            )
            try:
                self.initialize_parquet()
                console.print("\n[bold green]Success![/bold green]")
            except Exception as e:
                console.print(f"[bold red]Error while initializing the parquet: {e}[/bold red]")

    def initialize_parquet(self):
        self.console.print(f"Initializing [bold italic yellow]{self.parquet_path}[/bold italic yellow]...")
        columns = {
            "ID": uuid.UUID,
            "Date": pl.datatypes.Datetime(time_unit="ms", time_zone="Europe/Rome"),
            "Amount": pl.datatypes.Float32,
            # "Currency": pl.datatypes.Enum
            "Currency": pl.datatypes.String | None,
            "Recipient" : pl.datatypes.String | None,
            "Category" : pl.datatypes.String | None,
            "Method": pl.datatypes.String | None,
            "Card Number": pl.datatypes.String | None,
        }

        self.df = pl.DataFrame(schema=columns)
        self.update_parquet()

    def add_transaction(self, date: pl.datatypes.Datetime, amount: pl.datatypes.Float32, currency: pl.datatypes.String | None, recipient: pl.datatypes.String | None, category: pl.datatypes.String | None, method: pl.datatypes.String | None, cardN: pl.datatypes.String | None):
        id = uuid.uuid4()

        transaction_df = pl.DataFrame({
                                          "ID": [id],
                                          "Date": [date],
                                          "Amount": [amount],
                                          "Currency": [currency],
                                          "Recipient": [recipient],
                                          "Category": [category],
                                          "Method": [method],
                                          "cardN": [cardN]
                                      })

        self.df.vstack(transaction_df, in_place=True)
        self.update_parquet()
        

    # Consider deleting in bulk
    def delete_transaction(self):
        pass

    def report_transactions(self):
        pass

    def filter_transactions(self):
        pass

    def update_parquet(self, method = None): # Does it make sense to use the method?
        self.df.write_parquet(self.parquet_path)
