FROM python:3.8.5

RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
    curl unzip wget \
    xvfb

COPY app /opt/app

WORKDIR /opt/app

RUN pip3 install --upgrade pip && \
    pip install pipenv

RUN pipenv install --system --deploy