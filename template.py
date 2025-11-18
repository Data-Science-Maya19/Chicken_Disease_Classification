import os
from pathlib import Path  # to handle path issues, it identifies which type of system paath it is windows, linux or Mac
import logging

logging.basicConfig(level=logging.INFO, format= '[%(asctime)s] : %(message)s:')  # logging info - will return ascii time and logging message

project_name = "CNN_Classifier"

list_of_files = [
    ".github/workflows/.gitkeep",  # gitkeep if any empty folder it identifies that
    f"src/{project_name}/__init__.py",  # constructor file
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"  # for experimentation purpose
]

for filepath in list_of_files:
    filepath = Path(filepath)
    # separate folder name and file names
    filedir, filename = os.path.split(filepath)

    # check if folder is not empty
    if filedir != "":
        os.makedirs(filedir, exist_ok= True)
        logging.info(f"Creating directory {filedir} for the file {filename}")
    
    # Check if the file is present and what if the filesize (like if any content exists in file)
    if (not (os.path.exists(filename)) or (os.path.getsize(filename) == 0)):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file {filepath}")
    else:
        logging.info(f"The file {filename} alraedy exists")



