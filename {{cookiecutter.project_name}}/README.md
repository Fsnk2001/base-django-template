# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Database Migrations](#database-migrations)
- [Deployment](#deployment)
- [Switching Between Environments](#switching-between-environments)

## Features

- Fill this part based on your project.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.10+** installed on your machine.
- **Virtualenv** or another method for managing virtual environments.
- **Docker** and **Docker Compose**.

## Installation

### 1. Clone the Repository

```bash
git clone {{your_repo_url}}
cd {{cookiecutter.project_name}}
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

- For development:
    ```bash
    pip install -r requirements.txt
    ```

- For production:
    ```bash
    pip install -r requirements-production.txt
    ```

## Environment Variables

Create a `.env` file in the project root directory and add the required environment.
You can copy the `.env.example` file:

```bash
cp .env.example .env
```

To generate a unique `SECRET_KEY` and set it in your `.env` file, use the provided script.

```bash
python generate_secret_key.py
```

This script will:

- Copy the `.env.example` file to `.env` if `.env` does not already exist.
- Generate a unique `SECRET_KEY` and add it to the `.env` file, ensuring you have a secure key for your application.

## Database Migrations

Apply the migrations to set up your database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Deployment

To deploy the project using Docker Compose, run this:

- For development:
    ```bash
    docker compose up --build -d
    ```

- For production:
    ```bash
    docker compose -f docker-compose-production.yml up --build -d
    ```

## Switching Between Environments

To switch between development and production settings, modify the environment variable `DJANGO_SETTINGS_MODULE` when
running the application.

- For development:
    ```bash
    export DJANGO_SETTINGS_MODULE={{cookiecutter.project_slug}}.settings.local
    ```

- For production:
    ```bash
    export DJANGO_SETTINGS_MODULE={{cookiecutter.project_slug}}.settings.production
    ```
