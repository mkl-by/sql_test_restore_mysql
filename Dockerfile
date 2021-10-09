FROM python:3.6
RUN mkdir /src
WORKDIR src
COPY ./project/requirements.txt /scripts/
RUN pip3 install -r /scripts/requirements.txt
