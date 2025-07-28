import os
import cv2
import click

VIDEO_EXTS = ['.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv']

def get_video_files(folder):
    return [f for f in os.listdir(folder) if os.path.splitext(f)[1].lower() in VIDEO_EXTS]

@click.command(name="sort_vid")
@click.argument("folder", type=click.Path(exists=True, file_okay=False))
def sort_vid(folder):
    """Sort video files in a folder by previewing and labeling them."""

    video_files = get_video_files(folder)
    
    for video_file in video_files:
        the_last_char = video_file[-1] 
        if the_last_char .isdigit() and (the_last_char  == '1' or the_last_char  == '2'):
                print("Last character is '1' or '2'. Skipping video opening.")
                continue
        else:
            print(f"File: {video_file} | Last character is '{the_last_char}'. Proceeding to open video...")

        video_path = os.path.join(folder, video_file)
        cap = cv2.VideoCapture(video_path)
    
        
        if not cap.isOpened():
            print(f"Failed to open {video_file}")
            continue

        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        middle_frame = total_frames // 2
        cap.set(cv2.CAP_PROP_POS_FRAMES, middle_frame)

        ret, frame = cap.read()
        if not ret:
            print(f"Failed to read frame from {video_file}")
            cap.release()
            continue

        cv2.imshow('Preview', frame)
        print(f"\nNow showing: {video_file}")
        print("Press 1 or 2 to label the video, or ESC to skip.")

        key = None
        while key not in [49, 50, 27]:  # ASCII for '1', '2', ESC
            key = cv2.waitKey(0)

        cv2.destroyAllWindows()
        cap.release()

        if key == 27:
            print("Skipped.\n")
            continue

        label = chr(key)
        name, ext = os.path.splitext(video_file)
        new_name = f"{name}_{label}{ext}"
        os.rename(video_path, os.path.join(folder, new_name))
        print(f"Renamed to: {new_name}\n")


