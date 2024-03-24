# Використовуємо базовий образ Python
FROM python:3.11-slim-buster

# Встановлюємо залежності з requirements.txt
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Додаємо файли проекту в контейнер
COPY . /app

# Встановлюємо робочу директорію
WORKDIR /app

# Команда для запуску серверу
CMD ["python", "main.py"]



