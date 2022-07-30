from python:3.10.1-slim

WORKDIR /app

RUN apt-get update
COPY . /app
RUN pip install -r requirements.txt

expose 8888

CMD ["python", "/app/start_service.py"]