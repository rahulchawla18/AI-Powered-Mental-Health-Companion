# backend/Dockerfile

FROM python:3.12

# Set work directory
WORKDIR /app

# Copy project files
COPY . .

RUN apt-get update && \
    apt-get install -y portaudio19-dev python3-pyaudio

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Run the API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
