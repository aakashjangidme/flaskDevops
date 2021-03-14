FROM python:alpine
# MAINTAINER Aakash ajangid25@gmail.com
WORKDIR /app

COPY . /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt