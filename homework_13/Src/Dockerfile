FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && \
    python -c "from csv_utils import create_csv; create_csv()"


EXPOSE 8000

ENV FLASK_APP=main.py

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "main:app"]
