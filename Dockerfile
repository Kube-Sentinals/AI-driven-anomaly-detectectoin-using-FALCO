# Use a basic Python image
FROM python:3.8-slim

# Set up the working directory
WORKDIR /app

# Copy the application files
COPY app.py .

# Install required dependencies
RUN pip install flask

# Expose port 80 for the Flask app
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
