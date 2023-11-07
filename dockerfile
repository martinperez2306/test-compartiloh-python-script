# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the entire contents of the current directory into the container
COPY . .

# Install dependencies (if you have a requirements.txt file)
# RUN pip install -r requirements.txt

# Set the entry point for the container
CMD ["python", "script.py"]
