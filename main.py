# main.py
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.markdown import Markdown
from rich.prompt import Prompt

# Import ETL functions
from etl.extraction import run_wikipedia_spider
from etl.transform import json_to_docs
from etl.load import load_documents, load_words


import subprocess


def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else result.stderr


def main():
    console = Console()

    title = Text("Harmony Project Control Panel", style="bold blue on white")
    description = Markdown(
        """
Welcome to the **Harmony Project Control Panel**!
Please select an option to proceed with the operations.
"""
    )

    panel = Panel(
        description, title=title, expand=False, border_style="blue", padding=(1, 2)
    )
    console.print(panel)

    options = {
        "1": ("Initiate Scraping", run_wikipedia_spider),
        "2": ("Generate Documents", json_to_docs),
        "3": ("Load Documents to Database", load_documents, "documents"),
        "4": (
            "Load Documents to HDFS",
            run_command,
            "hdfs dfs -mkdir -p /harmony/documents/ && \
             hdfs dfs -copyFromLocal /home/hadoop/harmony/documents/* /harmony/documents/ && \
             hdfs dfs -ls /harmony/documents",
        ),
        "5": (
            "Send JSON Inv-Idx Request to Hadoop",
            run_command,
            "hadoop-streaming -D mapred.reduce.tasks=1 \
             -file /home/hadoop/Harmony/samples/inverted_index/mapper.py    -mapper /home/hadoop/Harmony/samples/inverted_index/mapper.py \
             -file /home/hadoop/Harmony/samples/inverted_index/reducer.py   -reducer /home/hadoop/Harmony/samples/inverted_index/reducer.py \
             -input /harmony/documents/ -output /harmony/output",
        ),
        "6": (
            "Get JSON Inv-Idx from HDFS",
            run_command,
            "hdfs dfs -get /harmony/output/part-00000 /home/hadoop/harmony/data && \
             mv /home/hadoop/harmony/data/part-00000 /home/hadoop/harmony/data/index_mapping.json",
        ),
        "7": ("Load Inverted Index", load_words, "data/index_mapping.json"),
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

        continue_prompt = Prompt.ask(
            "[bold]Would you like to perform another action? (y/n)[/bold]", default="y"
        )
        if continue_prompt.lower() != "y":
            break

    console.print(
        "[bold cyan]Thank you for using the Harmony Project Control Panel. Goodbye![/bold cyan]"
    )


if __name__ == "__main__":
    main()
