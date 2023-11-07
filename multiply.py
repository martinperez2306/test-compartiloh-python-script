# script.py

import logging
import datetime

# Configure the logging settings
logging.basicConfig(
    filename='output.log',
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


