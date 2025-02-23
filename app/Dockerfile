# Use Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the application files
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose port 5000
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
