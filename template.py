"""
This script automates the creation of the folder structure and template files 
for the project, ensuring that the necessary directories and files are in place 
for development.

It generates the following:
- folder_structure/
- template.py
- config/ directory with config files
"""

import os
from pathlib import Path
import logging

# logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'trendline'
list_of_files = [
    f"src/{project_name}/__init__.py",
    
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/logging/logs",
    
    "config/config.yaml",
    "params.yaml",
    "setup.py",
    "main.py",
    "requirements.txt",
    "schema.yaml",
    "params.yaml"
]

# files & folders logic

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")