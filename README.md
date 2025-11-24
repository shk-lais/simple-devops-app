# Simple DevOps App - CI/CD Demo

Tiny Flask app demonstrating:
- Docker containerization
- GitHub Actions CI: build image, run container, run tests
- Simple metrics endpoint for observability

Run locally:
- python app.py

Docker:
- docker build -t simple-devops-app .
- docker run -p 5000:5000 simple-devops-app

CI:
- See .github/workflows/ci.yml
