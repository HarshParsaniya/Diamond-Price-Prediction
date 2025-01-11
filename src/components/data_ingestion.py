import os
import sys

from dataclasses import dataclass

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from src.logger import logging
from src.exception import CustomException

# Intitialize the Data Ingetion Configuration
@dataclass
class DataIngestionconfig:
    raw_data_path = os.path.join('artifacts', 'raw.csv')
    train_data_path = os.path.join('artifacts', 'train.csv')
    test_data_path = os.path.join('artifacts', 'test.csv')


# create a class for Data Ingestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion process started')
        try:
            df = pd.read_csv(os.path.join('notebook/data','gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            logging.info('Raw data path created')
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info('Raw data saved as csv')

            logging.info('Train Test Split')
            train_set, test_set = train_test_split(df, test_size=0.3, random_state=42)
            logging.info('Train Test Split completed')

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            logging.info('Train data saved as csv')
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info('Test data saved as csv')
            logging.info('Data Ingestion process completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise CustomException(e,sys)