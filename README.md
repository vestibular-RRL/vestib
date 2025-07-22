# 🌀 Vestib CLI (Folder Sync + Video Sort Automation)

A streamlined command-line tool built to assist vestibular research workflows. **Vestib** automates folder synchronization between external drives and intelligently renames video files based on eye-tracking data (1-eye or 2-eye).

---

## 🧠 Features

- 📁 **Folder Sync (`sync`)**  
  Automatically sync directories — ideal for keeping two hard drives up to date.

- 🎥 **Video Sorter (`sort_vid`)**  
  Renames and organizes videos depending on whether they contain 1-eye or 2-eye footage.

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