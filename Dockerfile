FROM python:latest
WORKDIR /app
COPY . /app
USER root
CMD ["python", "app.py"]
