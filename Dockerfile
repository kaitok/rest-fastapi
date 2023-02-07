FROM python:3.9-alpine

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

WORKDIR /app

# pip install
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt


RUN apk add --no-cache postgresql-libs \
  && apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev \
  && apk --purge del .build-deps

COPY ./api .