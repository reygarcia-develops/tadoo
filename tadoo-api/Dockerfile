FROM tiangolo/uvicorn-gunicorn-fastapi:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./app .

CMD ["uvicorn", "app.main:app",  "--reload","--host", "0.0.0.0", "--port", "80"]