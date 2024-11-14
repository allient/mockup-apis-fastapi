# Dockerfile

# Use an official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.8.4

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION"

# Set the working directory
WORKDIR /app

# Copy the project files
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

# Copy the application files
COPY app ./app

# Expose the port
EXPOSE 8000

# Run the FastAPI app with Uvicorn
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
