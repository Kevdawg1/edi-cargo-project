# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy source code
COPY . /app

# Install dependencies
RUN apt-get update && pip install --no-cache-dir -r requirements.txt


# Expose the port FastAPI will run on
EXPOSE 8000

# Start FastAPI app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
