import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import logging
from src.exception import CustomException


@dataclass
class DataIngestionConfig:
    train_data_path: str
    test_data_path: str
    raw_data_path: str


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig(
            train_data_path="artifacts/data/train.csv",
            test_data_path="artifacts/data/test.csv",
            raw_data_path="artifacts/data/raw.csv"
        )

    def initiate_data_ingestion(self):
        """
        Reads the dataset, splits it into train and test sets, and saves them to disk.
        """
        try:
            logging.info("Starting data ingestion process.")
            
            # Load the dataset
            df = pd.read_csv(r"C:\Users\realme\Desktop\End-to-end-Machine-Learning-Project-with-MLflow-main\End-to-end-Machine-Learning-Project-with-MLflow-main\research\data2.csv")
            logging.info("Dataset loaded successfully.")

            # Save the raw data
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.data_ingestion_config.raw_data_path, index=False)
            logging.info(f"Raw data saved at {self.data_ingestion_config.raw_data_path}.")

            # Split the data into train and test sets
            train_set, test_set = train_test_split(df, test_size=0.20, random_state=42)
            logging.info("Data split into train and test sets.")

            # Save the train and test sets
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path), exist_ok=True)
            train_set.to_csv(self.data_ingestion_config.train_data_path, index=False)
            logging.info(f"Train data saved at {self.data_ingestion_config.train_data_path}.")

            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path), exist_ok=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path, index=False)
            logging.info(f"Test data saved at {self.data_ingestion_config.test_data_path}.")

            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        obj = DataIngestion()
        train_data_path, test_data_path = obj.initiate_data_ingestion()
        logging.info(f"Data ingestion completed. Train data path: {train_data_path}, Test data path: {test_data_path}")
    except Exception as e:
        logging.error(f"Data ingestion failed: {str(e)}")
















