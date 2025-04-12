FROM python:3.12

WORKDIR /app

RUN pip install -r requirements.txt
COPY requirements.txt .

COPY src ./src

ENTRYPOINT [ "python", "-m", "src.main" ]
