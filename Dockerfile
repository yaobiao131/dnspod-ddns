FROM python:3-alpine

MAINTAINER strahe <u@strahe.com>

WORKDIR /app

ADD . /app

RUN "pip install -r requirements.txt"

ENTRYPOINT ["python", "ddns.py"]
