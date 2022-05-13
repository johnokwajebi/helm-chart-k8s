FROM python:3.9-slim

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    nginx \
    python3-dev \
    build-essential \ 
    default-libmysqlclient-dev \
    python3-tk

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt  --src /usr/local/src

COPY . .

EXPOSE 7001
CMD [ "python", "main.py" ]
