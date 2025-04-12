FROM python:3.1

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY src ./src

ENTRYPOINT [ "python", "-m", "src.main" ]
