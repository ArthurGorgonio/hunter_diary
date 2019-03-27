FROM python:3.5-alpine

LABEL maintainer="Arthur"

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install --no-cache -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "run.py"]
