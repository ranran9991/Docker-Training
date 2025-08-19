FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Ensure the data directory exists
RUN mkdir -p /app/data
CMD ["python", "app.py"]