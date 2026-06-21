# CI/CD Pipeline Project

This project is part of the IBM DevOps and Software Engineering course (Course 12) final project. It demonstrates a complete CI/CD pipeline setup for a simple Flask web application using both **GitHub Actions** and **Tekton** pipelines on **OpenShift**.

## Project Overview

The project contains a minimal Flask application that returns `SERVICE RUNNING` on port `8000`. The CI/CD pipeline automates linting, testing, building, and deploying the application.

## Project Structure

```
.
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
├── tests/
│   └── test_app.py            # Unit tests for the Flask app
├── .github/
│   └── workflows/
│       └── workflow.yml        # GitHub Actions CI/CD workflow
└── .tekton/
    └── tasks.yml              # Tekton pipeline tasks
```

## CI/CD Pipeline

### GitHub Actions

The GitHub Actions workflow (`.github/workflows/workflow.yml`) performs the following steps:

1. **Checkout** the repository code
2. **Setup Python** environment
3. **Lint** the code using `flake8`
4. **Test** the application using `nose`
5. **Build** the application container image

### Tekton on OpenShift

The Tekton tasks file (`.tekton/tasks.yml`) defines the following tasks:

- **cleanup** - Remove old files from previous pipeline runs
- **test** - Run nose unit tests
- **git-clone** - Clone the source repository
- **flake8** - Lint the Python source code
- **buildah** - Build a container image using Buildah
- **deploy** - Deploy the application to OpenShift

## Application

The Flask application (`app.py`) listens on port `8000` and returns the string `SERVICE RUNNING` at the root endpoint. This confirms the service is healthy and reachable.

## Running the Application Locally

```bash
pip install -r requirements.txt
python app.py
```

The app will be available at `http://localhost:8000`.

## Running Tests

```bash
nosetests
```

## License

This project is created for educational purposes as part of the IBM DevOps course.
