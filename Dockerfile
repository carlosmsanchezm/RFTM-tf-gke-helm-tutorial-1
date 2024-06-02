FROM python:3.8-slim

RUN apt-get update && apt-get install -y redis-tools

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "server.py"]