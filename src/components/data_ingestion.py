# Import Required Libraries
import os
import sys
from src.components import data_transformation
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass  

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

# Configuration Class
# Stores file paths for ingestion

@dataclass
class DataIngestionConfig:
    # Path to save training dataset
    train_data_path:str=os.path.join("artifacts","train.csv")
    # Path to save testing dataset
    test_data_path:str=os.path.join('artifacts',"test.csv")
    # Path to save raw dataset copy
    raw_data_path:str=os.path.join('artifacts',"raw.csv")

# Data Ingestion Class
# Handles reading & splitting data

class DataIngestion:
    def __init__(self):
        # Create configuration object
        self.ingestion_config=DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method component")
        try:
            df=pd.read_csv(r"C:\Users\prane\OneDrive\Documents\ML_code\ML_Project\notebook\data\stud.csv")
            logging.info("Read the dataset as dadafame")

# Create artifacts folder if not exists
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

# Save raw dataset copy

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info('Train test split initiated')

            train_set,test_set= train_test_split(df,test_size=0.2,random_state=42)
# Save train dataset
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
# Save test dataset
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
            

if __name__=='__main__':
    obj = DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)