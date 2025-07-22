import click
from vestib.commands.sync import sync_command
from vestib.commands.sort_vid import sort_vid
from vestib.commands.framesheet import extract_frames
from vestib.commands.list_files import list_files  

@click.group()
def cli():
    """Vestib CLI — Tools for folder and file management."""
    pass

cli.add_command(sync_command)
cli.add_command(sort_vid)
cli.add_command(extract_frames)
cli.add_command(list_files)  

if __name__ == "__main__":
    cli()
