# Используем официальный slim-образ с явным указанием версии
FROM python:3.12-slim-bookworm

# Устанавливаем системные зависимости
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Настраиваем рабочую директорию
WORKDIR /app

# Копируем зависимости отдельно для кэширования
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY src/ ./src/

# Запускаем приложение
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0"]