FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Args
ARG TELEGRAM_BOT_TOKEN

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app

ENV TELEGRAM_BOT_TOKEN=$TELEGRAM_BOT_TOKEN

CMD ["python", "bot.py"]
