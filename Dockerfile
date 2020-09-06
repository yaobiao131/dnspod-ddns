FROM python:3.8-alpine

MAINTAINER zecbd <u@strahe.com>

WORKDIR /app

ADD . /app

RUN apk add gcc linux-headers libc-dev musl-dev libffi-dev openssl-dev

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "ddns.py"]
