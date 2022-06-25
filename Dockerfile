FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

# installing dependencies
ADD ./requirements.txt ./requirements.txt
RUN pip3 install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN adduser -D user
USER user
