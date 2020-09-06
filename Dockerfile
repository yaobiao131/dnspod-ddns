FROM python:3-alpine

MAINTAINER strahe <u@strahe.com>

WORKDIR /app

ADD . /app

RUN "pip install -r requirement.txt"

ENTRYPOINT ["python", "ddns.py"]
