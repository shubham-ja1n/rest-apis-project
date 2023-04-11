# CONTRIBUTING

## How to run the Dockerfile locally

```
docker run -dp 5000:5000 -w /app -v "${PWD}:/app" IMAGE_NAME sh -c "flask run --host 0.0.0.0"
```

# Old Docker File

```
FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask","run","--host","0.0.0.0"]
```