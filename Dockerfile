FROM python:3.11.4-slim

WORKDIR /app
ADD . /app

RUN apt-get update && apt-get -y install libpq-dev gcc
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]