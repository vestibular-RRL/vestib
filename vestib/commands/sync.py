import os
import shutil
import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def list_files(folder):
    return set(os.listdir(folder))

@click.command(name="sync")
@click.argument("folder1", type=click.Path(exists=True, file_okay=False))
@click.argument("folder2", type=click.Path(exists=True, file_okay=False))
@click.option("--combine", is_flag=True, help="Combine both folders by copying missing files into each other.")
def sync_command(folder1, folder2, combine):
    """Compare two folders and optionally combine them to have the same content."""

    files1 = list_files(folder1)
    files2 = list_files(folder2)

    common_files = files1 & files2
    missing_in_1 = sorted(files2 - files1)
    missing_in_2 = sorted(files1 - files2)

    # Display summary panel
    summary = f"""
[bold green]✅ Common files:[/] {len(common_files)}
[bold yellow]📁 Missing in '{folder1}':[/] {len(missing_in_1)}
[bold yellow]📁 Missing in '{folder2}':[/] {len(missing_in_2)}
    """.strip()
    console.print(Panel(summary, title="📊 Folder Comparison Summary", expand=False))

    # Show missing file names in a table (if any)
    if missing_in_1 or missing_in_2:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Missing in", style="cyan", width=35)
        table.add_column("File Name", style="white")

        for f in missing_in_1:
            table.add_row(folder1, f)
        for f in missing_in_2:
            table.add_row(folder2, f)

        console.print(table)

    # Combine logic
    if combine:
        for filename in missing_in_1:
            src = os.path.join(folder2, filename)
            dst = os.path.join(folder1, filename)
            shutil.copy2(src, dst)
            console.print(f"[green]📥 Copied[/] {filename} → [bold]{folder1}[/]")

        for filename in missing_in_2:
            src = os.path.join(folder1, filename)
            dst = os.path.join(folder2, filename)
            shutil.copy2(src, dst)
            console.print(f"[green]📥 Copied[/] {filename} → [bold]{folder2}[/]")

        console.print(Panel("[bold green]✅ Folders have been combined successfully![/]", expand=False))
