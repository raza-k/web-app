FROM python:3

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./src /app
COPY ./data /data

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
