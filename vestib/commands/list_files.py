import os
import click

@click.command(name="list-files")
@click.option("--ext", help="Optional file extension filter (e.g., .mp4, .csv)", default=None)
@click.option("--output", "-o", default="file_list.txt", help="Output file name")
def list_files(ext, output):
    """List all files in the current directory and save them to a text file."""

    files = [
        f for f in os.listdir()
        if os.path.isfile(f) and (ext is None or f.lower().endswith(ext.lower()))
    ]

    with open(output, "w") as f_out:
        for filename in files:
            f_out.write(f"{filename}\n")

    click.echo(f"✅ Saved list of {len(files)} file(s) to {output}")

"""
# List all files in current directory
vestib list-files

# List only .mp4 files
vestib list-files --ext .mp4

# Save to a custom file
vestib list-files -o my_video_list.txt
"""
