import os
import urllib.request as request # to download file from URL
import zipfile   # to unzip the downloaded file
from CNN_Classifier import logger
from CNN_Classifier.utils.common import get_size # to get the size of file
from CNN_Classifier.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            os.makedirs(os.path.dirname(self.config.local_data_file), exist_ok=True)
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: {headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """file_path: str
        Extracts zip file into data dictionary"""
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"File extracted at : {unzip_path}")