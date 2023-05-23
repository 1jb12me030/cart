FROM python:3-skim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
WORKDIR  /app
COPY  requirements.txt /app/

RUN python install -r requirements.txt 
COPY . /app/


EXPOSE 8080

CMD python manage.py runserver 