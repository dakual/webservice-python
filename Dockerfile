FROM python:3.8-slim-buster

RUN mkdir /app

WORKDIR /app/

ADD . /app/

ENV FLASK_ENV=production
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

RUN pip install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run"]