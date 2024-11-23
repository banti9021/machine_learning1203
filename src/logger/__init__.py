import logging
import os,sys
from datetime import datetime
LOG_DIR="logs"
LOG_DIR=os.path.join(os.getcwd(),LOG_DIR)
os.makedirs(LOG_DIR,exist_ok=True)
CURRENT_TIME_STAMP=f"{datetime.now().strftime('%y-%m-%d-%H-^m-%s')}"
file_name=f"log_{CURRENT_TIME_STAMP}.log"
lof_file_path=os.path.join(LOG_DIR,file_name)
logging.basicConfig(filename=lof_file_path,
                    filemode="w",
                    format='[%(asctime)s] %(name)s - %(levelname)s -%(message)s',
                    level=logging.INFO)