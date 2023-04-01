FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt ./requirements.txt
COPY main.py ./main.py


# COPY ./app.py ./
RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python3", "./main.py" ]