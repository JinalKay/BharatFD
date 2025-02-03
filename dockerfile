# Use an official base image (e.g., Python, Node.js, etc.)
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on
EXPOSE 5000

# Define the command to run your application
CMD ["python", "app.py"]