# main.py
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.markdown import Markdown
from rich.prompt import Prompt

# Import ETL functions
from etl.extraction import run_wikipedia_spider
from etl.transform import json_to_docs
from etl.load import load_documents

def main():
    console = Console()

    title = Text("Harmony Project Control Panel", style="bold blue on white")
    description = Markdown("""
Welcome to the **Harmony Project Control Panel**!
Please select an option to proceed with the operations.
""")

    panel = Panel(description, title=title, expand=False, border_style="blue", padding=(1, 2))
    console.print(panel)

    options = {
        "1": ("Initiate Scraping", run_wikipedia_spider),
        "2": ("Generate Documents", json_to_docs),
        "3": ("Load Documents to Database", load_documents, "documents"),
    }

    while True:
        for key in options:
            console.print(f"[yellow]{key}[/yellow]: {options[key][0]}")
        response = Prompt.ask("[bold]Enter the option number[/bold]", default="1")

        if response in options:
            console.print(f"[green]You have selected: {options[response][0]}[/green]")
            action = options[response]
            if len(action) == 2:
                action[1]()
            else:
                action[1](*action[2:])
        else:
            console.print("[red]Invalid option, please try again.[/red]")

        continue_prompt = Prompt.ask("[bold]Would you like to perform another action? (y/n)[/bold]", default="y")
        if continue_prompt.lower() != "y":
            break

    console.print("[bold cyan]Thank you for using the Harmony Project Control Panel. Goodbye![/bold cyan]")

if __name__ == "__main__":
    main()
