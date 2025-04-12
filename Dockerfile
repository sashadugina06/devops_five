FROM python:3.1

WORKDIR /app

RUN pip install -r requirements.txt
COPY requirements.txt .

COPY src ./src

ENTRYPOINT [ "python", "-m", "src.main" ]
