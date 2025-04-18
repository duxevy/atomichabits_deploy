# Используем официальный slim-образ Python 3.12
FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \ 
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

# Копируем файл зависимостей в контейнер
COPY requirements.txt ./

# Устанавливаем зависимости проекта
RUN pip install -r requirements.txt 

# Копируем исходный код приложения в контейнер
COPY . .