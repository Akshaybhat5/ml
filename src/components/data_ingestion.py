# Data Ingestion

import pandas as pd
import os
import sys
from src.exception import CustomException
from src.logger import logging

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionInfo:
    train_data_path: str = os.path.join('artifact', 'train.csv')
    test_data_path:str = os.path.join('artifact', 'test.csv')
    raw_data_path:str = os.path.join('artifact', 'data.csv')
    
    
class DataIngestion:
    def __init__(self):
        self.data_ingestion = DataIngestionInfo()
        
        
    def initiate_data_ingestion(self):
        logging.info("Data ingestion initiated")
        
        try:
            #read the data
            df = pd.read_csv('/home/akshay/Desktop/mle/notebook/data/stud.csv')
            logging.info('The data has been read correclty')
            os.makedirs(os.path.dirname(self.data_ingestion.train_data_path), exist_ok=True)
            df.to_csv(self.data_ingestion.raw_data_path, index=False, header=True)
            
            logging.info('Train Test Split Initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.data_ingestion.train_data_path, index = False, header = True)
            test_set.to_csv(self.data_ingestion.test_data_path, index = False, header = True)
            logging.info("The data ingestion is complete!")
            
        except Exception as error:
            raise CustomException(error, sys)
        
        
        return (
            self.data_ingestion.train_data_path,
            self.data_ingestion.test_data_path
        )
        
        
if __name__=="__main__":
    ingestion = DataIngestion()
    ingestion.initiate_data_ingestion()
    
    