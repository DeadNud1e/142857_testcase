FROM python:3.8.0-alpine

WORKDIR /app

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt


CMD python app.py