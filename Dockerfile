FROM python:3-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project code
COPY . /app/

# Expose port (if needed for Django)
EXPOSE 8000

# Default command (this will be overridden in docker-compose for different services)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
