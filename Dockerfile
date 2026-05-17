FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Install system dependencies (openssl for certificate generation)
RUN apt-get update && apt-get install -y --no-install-recommends \
    openssl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Create SSL directory
RUN mkdir -p /etc/squid-panel/ssl && chmod 700 /etc/squid-panel/ssl

EXPOSE 8444
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8444"]
