FROM python:3.12-slim

WORKDIR /app

COPY . .

ENV PYTHONPATH=/app

COPY requirements.txt ../requirements.txt
RUN pip install -r ../requirements.txt

CMD ["uvicorn", "main:application", "--host", "0.0.0.0", "--port", "8000"]
