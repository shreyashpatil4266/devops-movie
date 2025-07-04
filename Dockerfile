# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy everything into the container
COPY . .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Flask
EXPOSE 8000

# Run the app
CMD ["python", "app.py"]
