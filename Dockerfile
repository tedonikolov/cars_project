FROM python:3.12
WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]