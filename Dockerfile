FROM python:3.11.8

WORKDIR /app

COPY './requirements.txt' .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "app.py" ]