from setuptools import setup, find_packages

setup(
    name="vestib",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "click==8.2.1",
        "colorama==0.4.6",
        "markdown-it-py==3.0.0",
        "mdurl==0.1.2",
        "numpy==2.2.6",
        "opencv-python==4.12.0.88",
        "pygments==2.19.2",
        "rich==14.0.0",
        "typing-extensions==4.14.1"
    ],
    entry_points={
        "console_scripts": [
            "vestib=vestib.cli:cli"
        ]
    },
)
