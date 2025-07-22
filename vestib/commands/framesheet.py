import click
import cv2
import os
import csv

@click.command(name="extract-frames")
@click.argument("video_path", type=click.Path(exists=True, dir_okay=False))
@click.option("--output", "-o", type=click.Path(dir_okay=False), help="Exact output CSV file path (overrides outdir)")
@click.option("--outdir", type=click.Path(file_okay=False), help="Optional directory to save CSV (defaults to video folder)")
def extract_frames(video_path, output, outdir):
    """Extract frame numbers from a video and save to a CSV file with 'Frame#' column."""
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        click.echo(f"❌ Failed to open video: {video_path}")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_numbers = list(range(int(total_frames)))

    base_name = os.path.splitext(os.path.basename(video_path))[0]

    # Determine output path
    if output:
        output_csv = output
    else:
        output_dir = outdir if outdir else os.path.dirname(video_path)
        os.makedirs(output_dir, exist_ok=True)
        output_csv = os.path.join(output_dir, f"{base_name}.csv")

    with open(output_csv, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Frame#"])
        for frame_num in frame_numbers:
            writer.writerow([frame_num])

    click.echo(f"✅ Saved {len(frame_numbers)} frame numbers to {output_csv}")
    cap.release()

'''
# Save in same directory as video (default)
vestib extract-frames video.mp4

# Specify exact output file path
vestib extract-frames video.mp4 --output results/video_frames.csv

# Specify output directory (filename will match video name)
vestib extract-frames video.mp4 --outdir results/
'''
