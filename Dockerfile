FROM python:3.8

EXPOSE 8000

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code

COPY requirements.txt  /code/

RUN pip install -r requirements.txt
COPY . /code

CMD python manage.py migrate && gunicorn ipt_techno_site.wsgi -b 0.0.0.0:8000
