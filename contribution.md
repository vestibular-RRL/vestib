# 🛠️ Contributing to Vestib
**Thank you for your interest in contributing to Vestib, a CLI tool built to support vestibular research workflows. We welcome your additions!**
## 📦 Getting Started
**1. Clone the Repository**
```bash
git clone https://github.com/vestibular-RRL/vestib.git
```
**2. Set Up Your Conda Environment**

Ensure you have Conda installed. Then run:
```bash
conda env create -f environment.yml
conda activate vestib
```
This will install all necessary dependencies.

## 💡 Adding a New CLI Command
Vestib CLI commands are modular and stored inside the commands/ directory.

### ✅ Step-by-step: 

**1.Create a new file in the commands/ folder for your CLI command.**

Example:

```arduino
commands/
  my_new_feature.py  ← your new command here
```
**2. Define your command using click in the new file.**

Example:
```python
import click

@click.command()
def my_new_feature():
    """Short description of the feature."""
    click.echo("This is my new feature!")
```
**3. Register your command in vestib/cli.py:**
Import your command and add it to the CLI group:
```python
from commands.my_new_feature import my_new_feature

cli.add_command(my_new_feature)
```
Now your new command can be run using:
```bash
vestib my-new-feature
```
## ✅ Checklist Before Opening a Pull Request
**Your new file is inside the commands/ folder.**

 **You registered the command in vestib/cli.py.**

 **Code is formatted and linted properly.**

 **You’ve tested your feature locally in the Conda environment.**

 **You’ve written clear, descriptive docstrings and click help messages.**