FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r req.txt

EXPOSE 8000
EXPOSE 8501

CMD uvicorn api.app:app --host 0.0.0.0 --port 8000