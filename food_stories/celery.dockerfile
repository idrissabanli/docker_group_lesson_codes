FROM python:3.7

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
ADD . .

CMD [ "celery", "-A", "food_stories", "worker", "--beat", "--scheduler", "django", "--loglevel=info" ]
