FROM python:3.6.8-stretch

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]