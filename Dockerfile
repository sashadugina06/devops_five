FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src app/src

WORKDIR /app

ENV PYTHONPATH=/app/src

ENTRYPOINT [ "python", "-m", "src.main" ]
