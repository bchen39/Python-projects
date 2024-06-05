# Use the official Python image as the base image
FROM python:3.11.3

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port your Flask app will run on
EXPOSE 5000

# Define the command to start your Flask app
CMD ["python3", "tor_checker.py"]