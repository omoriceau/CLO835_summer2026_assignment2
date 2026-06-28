# Requirement: the image must run your app and serve on port 8080.
FROM python:3.14-rc-slim

WORKDIR /app
COPY apps/python/app.py .
EXPOSE 8080
CMD ["python3", "app.py"]
