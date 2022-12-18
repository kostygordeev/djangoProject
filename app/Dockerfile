FROM python:3.9
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY app app
ADD .env /env_file/.env
WORKDIR /app
RUN python ./manage.py migrate
RUN python manage.py collectstatic