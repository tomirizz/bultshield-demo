FROM python:3.12.14-slim-bookworm
WORKDIR /app
COPY app.py /app/app.py
USER 10001:10001
HEALTHCHECK --interval=30s --timeout=5s CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080', timeout=3)"
CMD ["python", "app.py"]
