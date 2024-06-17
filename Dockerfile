FROM python:3.11.5
WORKDIR /app
COPY  requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5454
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5454

CMD ["gunicorn", "-b", "0.0.0.0:5454", "main:app"]
