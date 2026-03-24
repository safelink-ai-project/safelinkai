FROM python:3.12-slim

WORKDIR /app

COPY . .


RUN pip install -r requirements.txt && playwright install --with-deps
