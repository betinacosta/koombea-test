# Use the official Python base image
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Run the FastAPI application using uvicorn server
CMD ["python3", "main.py"]