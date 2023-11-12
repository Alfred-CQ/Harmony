# main.py
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.markdown import Markdown


def main():
    console = Console()

    title = Text("Harmony Project Control Panel", style="bold blue on white")
    title.stylize("underline blue", 0, 7)  # Subraya 'Harmony'

    description = Markdown("Welcome to the **Harmony Project Control Panel**!\n")

    panel = Panel(
        description, title=title, expand=False, border_style="blue", padding=(1, 2)
    )

    console.print(panel)


if __name__ == "__main__":
    main()
