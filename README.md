# 🌀 Vestib CLI (Folder Sync + Video Sort Automation)

A streamlined command-line tool built to assist vestibular research workflows. **Vestib** automates folder synchronization between external drives and intelligently renames video files based on eye-tracking data (1-eye or 2-eye).

---

## 🧠 Features

- 📁 **Folder Sync (`sync`)**  
  Automatically sync directories — ideal for keeping two hard drives up to date.

- 🎥 **Video Sorter (`sort_vid`)**  
  Renames and organizes videos depending on whether they contain 1-eye or 2-eye footage.
- 📄 **List Files (`list_file`)**  
  Generate a `.txt` file listing all files in the current directory.  
  Use `--ext` to filter by file extension and `-o` to specify the output file.

- 🧾 **Extract Frame (`extract_frame`)**  
  Create a `.csv` file listing frame numbers.  
  Use `--output` for the CSV file path and `--outdir` to define where frames are saved.
---

## 📦 Dependencies

Make sure you have **Python 3.7+** and **conda** installed.

---

## 🚀 Installation

🔁 1. **Clone the repository**  
```bash
git clone https://github.com/vestibular-RRL/vestib.git
cd vestib
```

🛠️ 2. **Create and activate the virtual environment**
```bash
conda env create -f environment.yml
conda activate vestib-env
```

⬇️ 3. **Install the project (editable mode)**
```bash
pip install -e .
```
## 💡 Usage
🔄 Sync two folders

```bash
vestib sync --source /path/to/source --target /path/to/target
```
🎞️ Sort videos by eye type

```bash
vestib sort_vid --input /path/to/videos
```
📄 List files in the current directory (optional extension filter)

```bash
vestib list_file --ext .mp4 -o output.txt
```
🧾 Extract frame numbers into a CSV
```yami
vestib extract_frame --output frames.csv --outdir /path/to/save/frames
```