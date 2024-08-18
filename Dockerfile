# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy project files
COPY OMEGA /app
COPY temp /app/temp

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    pkg-config \
    libmariadb-dev \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


# Copy requirements.txt file
COPY requirements.txt /app/requirements.txt

# Install Python packages
RUN pip install --no-cache-dir -r /app/requirements.txt


# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable [whenever there is an error, it is been send to the terminal]
ENV PYTHONUNBUFFERED 1

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
