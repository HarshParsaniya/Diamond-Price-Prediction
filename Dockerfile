FROM python:3.12-slim-bullseye
WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && apt-get install -y curl
 && pip install --no-cache-dir -r requirements.txt \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
 
RUN pip freeze

EXPOSE 5000

CMD ["python3","application.py"]
