FROM --platform=linux/amd64 python:3.10-slim as build

WORKDIR /app

RUN pip install pandas scikit-learn numpy

COPY pyFolder /app/