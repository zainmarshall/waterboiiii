FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -U sciolyid

COPY water_quality_bot.py /app/water_quality_bot.py
COPY water_quality_data /app/water_quality_data

CMD ["python", "-u", "water_quality_bot.py"]
