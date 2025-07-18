import click
from vestib.commands.sync import sync_command

@click.group()
def cli():
    """Vestib CLI — Tools for folder and file management."""
    pass

cli.add_command(sync_command)

if __name__ == "__main__":
    cli()
