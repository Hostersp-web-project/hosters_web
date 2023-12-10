FROM python:3.12.0-alpine
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["gunicorn", "-b", "0.0.0.0:80", "hosters_web.wsgi:application"]
