FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

# installing dependencies
ADD ./requirements.txt ./requirements.txt
RUN pip3 install -r /requirements.txt

RUN mkdir /app
WORKDIR /app

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
