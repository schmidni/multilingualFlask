FROM python:3.8.5-alpine3.12

LABEL maintainer "@fabdelgado <mail@fabdelgado.com>"

RUN apk add --no-cache gcc musl-dev linux-headers

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PORT 80
ENV FLASK_APP main.py

ENV FLASK_RUN_HOST 0.0.0.0

#prod
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 microblog:app

