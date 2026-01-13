# Mini Python Shopping Web App for DevOps Practice

A simple Flask based shopping application designed for practicing DevOps tools and pipelines.

## Features
- View Products
- Add to Cart
- View Cart (Persistent via SQLite)

## Tech Stack
- **Backend:** Python 3.11, Flask
- **Database:** SQLite
- **Containerization:** Docker, Docker Compose
- **CI/CD:** Jenkins
- **Quality:** SonarQube

## Project Structure
```
shopping-app/
├── app/
│   ├── app.py           # Flask Routes
│   ├── models.py        # Database Init & Models
│   ├── templates/       # HTML Templates
│   └── requirements.txt # Dependencies
├── tests/               # Pytest Tests
├── Dockerfile           # Docker Image Build
├── docker-compose.yml   # Multi-container Setup
├── Jenkinsfile          # CI/CD Pipeline
└── sonar-project.properties # SonarQube Config
```

## How to Run locally

1. **Install Dependencies**
   ```bash
   pip install -r app/requirements.txt
   ```

2. **Run App**
   ```bash
   python app/app.py
   ```
   Access at `http://localhost:5000`

## How to Run with Docker

1. **Build**
   ```bash
   docker build -t shopping-app .
   ```

2. **Run**
   ```bash
   docker run -p 5000:5000 shopping-app
   ```

## How to Run with Docker Compose
```bash
docker-compose up --build
```

## DevOps Practice

- **Jenkins:** Use the provided `Jenkinsfile` to create a pipeline job. Ensure you have Docker and SonarQube Scanner configured in your Jenkins environment.
- **SonarQube:** Use `sonar-project.properties` for analysis configuration. Start a local SonarQube server and run the scanner.

## Testing
Run tests using pytest:
```bash
pytest tests/
```
