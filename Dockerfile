# Use a base Python image
FROM python:3.11.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the contents of the application into the container
COPY . .

# Expose the port on which the application runs
EXPOSE 8000

# Default command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
