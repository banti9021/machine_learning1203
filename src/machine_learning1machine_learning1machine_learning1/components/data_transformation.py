import os
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV, ShuffleSplit
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from dataclasses import dataclass
#from src.utils import save_obj
from src.constants import *
from src.logger import logging
from src.exception import CustomException
from src.config.configuration import PREPROCESING_OBJ_FILE, TRANSFORM_TRAIN_FILE_PATH, TRANSFORM_TEST_FILE_PATH, FEATURE_ENGG_OBJ_FILE_PATH


@dataclass
class DataTransformationConfig:
    processed_obj_file_path: str = PREPROCESING_OBJ_FILE
    transform_train_path: str = TRANSFORM_TRAIN_FILE_PATH
    transform_test_path: str = TRANSFORM_TEST_FILE_PATH
    feature_engg_obj_path: str = FEATURE_ENGG_OBJ_FILE_PATH


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def transform_data(self, df: pd.DataFrame):
        """
        Transform the given dataframe by applying custom feature engineering.
        """
        try:
            if 'ID' in df.columns:
                df.drop(['ID'], axis=1, inplace=True)
                logging.info("Dropped 'ID' column.")

            required_columns = ['Profession', 'Income', 'Credit_card_number', 'Expiry', 'Security_code', 'Fraud']
            missing_columns = set(required_columns) - set(df.columns)
            if missing_columns:
                raise ValueError(f"Missing required columns: {missing_columns}")

            # Call a feature engineering function if needed
            # self.distance_numpy(df, *required_columns)

            logging.info("Data transformation completed.")
            return df
        except Exception as e:
            raise CustomException(f"Error during data transformation: {e}", sys)

    def get_data_transformation_obj(self):
        """
        Create preprocessing pipelines for numerical and categorical data.
        """
        try:
            categorical_columns = ['Expiry', 'Profession']
            numerical_columns = ['Income', 'Credit_card_number', 'Security_code', 'Fraud']

            # Numerical pipeline
            numerical_pipeline = Pipeline([
                ('imputer', SimpleImputer(strategy='constant', fill_value=0)),
                ('scaler', StandardScaler(with_mean=False))
            ])

            # Categorical pipeline
            categorical_pipeline = Pipeline([
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('onehot', OneHotEncoder(handle_unknown='ignore'))
            ])

            # Combine pipelines
            preprocessor = ColumnTransformer([
                ('numerical_pipeline', numerical_pipeline, numerical_columns),
                ('categorical_pipeline', categorical_pipeline, categorical_columns)
            ])

            logging.info("Data transformation pipeline created.")
            return preprocessor
        except Exception as e:
            raise CustomException(f"Error in creating data transformation object: {e}", sys)

    def initiate_data_transformation(self, train_path: str, test_path: str):
        """
        Perform data transformation on train and test datasets.
        """
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Starting feature engineering.")
            transformed_train_df = self.transform_data(train_df)
            transformed_test_df = self.transform_data(test_df)

            # Save transformed data
            transformed_train_df.to_csv("train_data.csv", index=False)
            transformed_test_df.to_csv("test_data.csv", index=False)

            preprocessor = self.get_data_transformation_obj()

            target_column_name = "Time_taken (min)"
            X_train = transformed_train_df.drop(columns=[target_column_name])
            y_train = transformed_train_df[target_column_name]

            X_test = transformed_test_df.drop(columns=[target_column_name])
            y_test = transformed_test_df[target_column_name]

            # Apply preprocessing
            X_train = preprocessor.fit_transform(X_train)
            X_test = preprocessor.transform(X_test)

            # Combine features and target
            train_arr = np.c_[X_train, np.array(y_train)]
            test_arr = np.c_[X_test, np.array(y_test)]

            # Save processed data
            os.makedirs(os.path.dirname(self.data_transformation_config.transform_train_path), exist_ok=True)
            pd.DataFrame(train_arr).to_csv(self.data_transformation_config.transform_train_path, index=False, header=True)

            os.makedirs(os.path.dirname(self.data_transformation_config.transform_test_path), exist_ok=True)
            pd.DataFrame(test_arr).to_csv(self.data_transformation_config.transform_test_path, index=False, header=True)

            # Save preprocessing object
            save_obj(self.data_transformation_config.processed_obj_file_path, preprocessor)

            logging.info("Data transformation process completed successfully.")
            return train_arr, test_arr, self.data_transformation_config.processed_obj_file_path
        except Exception as e:
            raise CustomException(f"Error during data transformation initiation: {e}", sys)
