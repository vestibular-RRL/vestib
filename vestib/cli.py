import click
from vestib.commands.sync import sync_command
from vestib.commands.sort_vid import sort_vid

@click.group()
def cli():
    """Vestib CLI — Tools for folder and file management."""
    pass

cli.add_command(sync_command)
cli.add_command(sort_vid)

if __name__ == "__main__":
    cli()
