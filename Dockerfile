FROM python:3.12-slim-bullseye
WORKDIR /app
COPY . /app

RUN apt-get update 

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3","application.py"]
