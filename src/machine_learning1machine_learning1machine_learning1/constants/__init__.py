import os,sys
from datetime import datetime

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"
CURRENT_TIME_STAMP=get_current_time_stamp()
ROOT_DIR_KEY=os.getcwd()
DATA_DIR_KEY="data2.csv"


ARTIFACT_DIR_KEY="Artifact"

DATA_INGESTION_KEY="data_ingestion"
DATA_INGESTION_RAW_DATA_KEY="raw_data_dir"
DATA_INGESTION_INGESTED_DATA_DIR_KEY="ingested_dir"\
RAW_DATA_DIR_KEY="data2.csv"
TRAIN_DATA_DIR_KEY="train.csv"
TEST_DATA_DIR_KEY="test.csv"




#data Transformation related variable
DATA_TRANSFORMARTION_ARTIFACT="data_transformation"
DATA_PREPROCCED_DIR="proccer"
DATA_TRANSFORMARTION_PROCESSING_OBJ="processor.pkl"
DATA_TRANSFORMARTION_DIR="transformation"
TRANSFORM_TRAIN_DIR_KEY="train.csv"
TRANSFORM_TEST_DIR_KEY="test.csv"

#artifact/data_transformation

