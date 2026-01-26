import os
from box.exceptions import BoxValueError  # to handle box exceptions
import yaml
from CNN_Classifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from pathlib import Path
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns

    Args:
        path_to_yaml (Path): Path like input

    Raises:
        Value Error if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type object
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

    
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """Create list of directories

    Args:
        path_to_directories (list[Path]): List of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created Deafault to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves json data to a file

    Args:
        path (Path): Path to the json file
        data (dict): data to be saved
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    logger.info(f"Json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads json data from a file

    Args:
        Configbox: data as class attributes instead of dictionary """
    with open(path, 'r') as json_file:
        data = json.load(json_file)

    logger.info(f"Json file loaded successfully from: {path}")
    return ConfigBox(data)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves binary data to a file

    Args:
        data (Any): data to be saved
        path (Path): Path to the binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads binary data from a file

    Args:
        path (Path): Path to the binary file
    """
    data = joblib.load(filename=path)
    logger.info(f"Binary file loaded successfully from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """Get size of a file in KB

    Args:
        path (Path): Path to the file

    Returns:
        str: size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    logger.info(f"File size for path: {path} is {size_in_kb} KB")
    return f"{size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
        return my_string