FROM python:3.8.6

RUN apt-get update -y ; apt-get install vim -y
RUN pip install --upgrade pip
RUN pip install pytest

RUN mkdir /local

COPY . /local
WORKDIR /local

RUN pip install -r requirements.txt --use-deprecated=legacy-resolver

CMD /bin/bash