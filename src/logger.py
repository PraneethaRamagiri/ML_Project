import logging
import os
from datetime import datetime

# Create a unique log file name using current date and time

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create path for logs directory

logs_path = os.path.join(os.getcwd(),"logs")

# Create logs directory if it does not exist

os.makedirs(logs_path,exist_ok=True)


# Full path for the log file

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,     #where logs will be stored
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO


)


if __name__=="__main__":
    logging.info("Logging has started")