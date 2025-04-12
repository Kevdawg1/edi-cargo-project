# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY edi-cargo-backend/requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY edi-cargo-backend .

# Expose port
EXPOSE 8000

# Run the app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
