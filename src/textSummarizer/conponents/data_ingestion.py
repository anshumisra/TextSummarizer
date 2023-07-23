import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from pathlib import Path
from textSummarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  

        
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

    # def extract_zip_file(self):  
    #     f = open(self.config.unzip_dir, 'r')  
    #     data = f.read()  
    #     pos = data.find('\x50\x4b\x05\x06') # End of central directory signature  
    #     if (pos > 0):  
    #         self._log("Trancating file at location " + str(pos + 22)+ ".")  
    #         f.seek(pos + 22)   # size of 'ZIP end of central directory record' 
    #         f.truncate()  
    #         f.close()  
    #     else:
    #          logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}") 