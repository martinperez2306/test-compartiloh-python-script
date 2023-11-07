# multiply.py

import datetime
import os

# Function to get the absolute path of the script's directory
def get_script_directory():
    return os.path.dirname(os.path.abspath(__file__))

# Function to log a message to the output.log file
def log_message(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    
    log_file_path = os.path.join(get_script_directory(), "output.log")
    
    with open(log_file_path, "w") as log_file:
        log_file.write(log_entry)

# Example usage
log_message("Script starting...")

# Your existing code here

result = 2 * 2

log_message(f"Result: {result}")

# Additional log messages
log_message("Script finished.")
