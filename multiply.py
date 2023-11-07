# multiply.py

import logging
import datetime
import os

# Function to get the absolute path of the script's directory
def get_script_directory():
    return os.path.dirname(os.path.abspath(__file__))

# Configure the logging settings
log_file_path = os.path.join(get_script_directory(), 'output.log')

# Check if the path is a directory before configuring logging
if os.path.isdir(log_file_path):
    raise ValueError(f"The provided log file path '{log_file_path}' is a directory.")

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
)

# Function to log a message using the logging library
def log_message(message):
    logging.info(message)

# Example usage
log_message("Script starting...")

# Your existing code here

result = 2 * 2

log_message(f"Result: {result}")

# Additional log messages
log_message("Script finished.")
