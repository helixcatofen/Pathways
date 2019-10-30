FROM ubuntu:18.04

MAINTAINER Xavier Weiss 2246306w@student.gla.ac.uk

RUN apt-get update && \
    apt-get install -y python-pip python-dev

COPY .requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]