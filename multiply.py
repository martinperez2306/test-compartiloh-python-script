import os
import logging

# Get the absolute path to the current directory
current_dir = os.path.abspath(os.path.dirname(__file__))

# Specify the log file name and create the absolute path
log_file_path = os.path.join(current_dir, 'app.log')

logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

logging.info("Hello World!")
