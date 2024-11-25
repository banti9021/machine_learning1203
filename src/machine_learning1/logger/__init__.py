import logging
import os
from datetime import datetime

# Define log directory and file path
LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)
os.makedirs(LOG_DIR, exist_ok=True)

# Create a timestamp for the log file name
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%y-%m-%d-%H-%M-%S')}"
file_name = f"log_{CURRENT_TIME_STAMP}.log"
log_file_path = os.path.join(LOG_DIR, file_name)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    filemode="w",
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Example usage
logging.info("Logging is set up successfully.")
