import pandas as pd
import numpy as np
import seaborn as sns
from src.DimondPricePrediction.logger import logging
import os
from pathlib import Path
from sklearn.model_selection import train_test_split
from src.DimondPricePrediction.exception import customException
import sys

class DataIngestionConfig:
    raw_data_path:str = os.path.join('artifacts','raw.csv')
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info('Data ingestion started')
        try:
            df = pd.read_csv(Path(os.path.join('notebooks/data','train.csv')))
            logging.info('I have read data as df')

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Saved the raw dataset in the artifact folder')

            logging.info('Here I performed train test split')
            train_data,test_data = train_test_split(df,test_size=0.25)
            logging.info('Train test split completed')

            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)

            logging.info('Ingestion part completed')

        except Exception as e:
            logging.info('Some exception occered in data ingestion process')
            raise customException(e,sys)