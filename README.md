# FastAPI CI/CD Demo

![CI Pipeline](https://github.com/sh3r44z/fastapi-cicd/actions/workflows/ci.yml/badge.svg)

A containerised Python REST API with a fully automated CI pipeline.
On every push to main: tests run, Docker image builds, and the image
is pushed to AWS ECR — automatically.

## Stack

| Tool | Purpose |
|---|---|
| FastAPI | REST API framework |
| Docker | Multi-stage containerisation |
| pytest | Automated testing |
| GitHub Actions | CI pipeline |
| AWS ECR | Container image registry |
| IAM | Least-privilege AWS access |

## Pipeline

push to main
→ lint + pytest
→ docker build
→ push to ECR (tagged with commit SHA)


## Run locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Run with Docker

```bash
docker build -t fastapi-cicd:latest .
docker run -p 8000:8000 fastapi-cicd:latest
```

## Run tests

```bash
pytest tests/ -v
```

## API Endpoints

| Endpoint | Method | Response |
|---|---|---|
| `/` | GET | App status |
| `/health` | GET | Health check |
| `/info` | GET | App info |
| `/docs` | GET | Interactive API docs |
