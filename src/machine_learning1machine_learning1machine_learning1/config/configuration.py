import os
from datetime import datetime

# Assuming these constants are defined in `src.machine_learning1.constants`
from src.machine_learning1.constants import (
    ROOT_DIR_KEY,
    DATA_DIR_KEY,
    ARTIFACT_DIR_KEY,
    DATA_INGESTION_KEY,
    DATA_INGESTION_RAW_DATA_KEY,
    DATA_INGESTION_INGESTED_DATA_DIR_KEY,
    TRAIN_DATA_DIR_KEY,
    TEST_DATA_DIR_KEY
)

# Define ROOT_DIR based on ROOT_DIR_KEY
ROOT_DIR = ROOT_DIR_KEY  # Replace with actual root directory path if needed

# Define the current timestamp for file versioning
CURRENT_TIME_STAMP = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Define dataset paths
DATASET_PATH = os.path.join(ROOT_DIR, DATA_DIR_KEY)

RAW_FILE_PATH = os.path.join(
    ROOT_DIR,
    ARTIFACT_DIR_KEY,
    DATA_INGESTION_KEY,
    CURRENT_TIME_STAMP,
    DATA_INGESTION_RAW_DATA_KEY
)

TRAIN_FILE_PATH = os.path.join(
    RAW_FILE_PATH,
    DATA_INGESTION_INGESTED_DATA_DIR_KEY,
    TRAIN_DATA_DIR_KEY
)

TEST_FILE_PATH = os.path.join(
    RAW_FILE_PATH,
    DATA_INGESTION_INGESTED_DATA_DIR_KEY,
    TEST_DATA_DIR_KEY
)
