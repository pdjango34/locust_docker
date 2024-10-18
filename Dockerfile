    # Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /locust
# Copy the current directory contents into the container at /app
COPY . /locust
# Copy the requirements file
# COPY requirements.txt /locust/requirements.txt

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Locust script
# COPY locustfile.py /locust/locustfile.py

# Make entry_point.sh executable
RUN chmod +x entry_point.sh

# Define environment variable
ENV PYTHONUNBUFFERED 1

# Expose the port Locust runs on
EXPOSE 8089

# Command to run Locust
CMD ["locust"]

# Run entry_point.sh when the container launches
ENTRYPOINT ["./entry_point.sh"]
