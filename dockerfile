# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary

# Expose port FastAPI will run on
EXPOSE 8000

# Command to run FastAPI app
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
