FROM python:3.11

WORKDIR /app

COPY /requirements.txt .
RUN pip install --no-cache-dir -r /requirements.txt

COPY src ./src

ENV PYTHONPATH=/app

ENTRYPOINT ["python", "-m", "src.main"]
