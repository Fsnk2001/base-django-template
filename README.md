# Cookiecutter Base Django Template

A Cookiecutter template for quickly creating Django projects with best practices and
minimal setup. This template is designed to help you kickstart a Django project with
a clean and organized structure.

## Features

- **Django and Python version**: Pre-configured with Django 4.2 and Python 3.12.
- **Structured Project Layout**: Organized directory structure for easy maintenance and scalability.
- **Docker Support**: Includes `Dockerfile` and `docker-compose` for easy development and deployment.
- **Custom User Model**: Includes a custom user model implementation for flexibility.
- **Environment Configuration**: Ready-to-use `.env` file setup for environment-specific settings.

## Usage

Let's pretend you want to create a Django project called "MyProject". Rather than using `django-admin startproject`
and then editing the results to include your name, email, and various configuration issues that always get forgotten
until the worst possible moment, get cookiecutter to do all the work.

First, get Cookiecutter.

```
pip install cookiecutter
```

Now run it against this repo:

```
cookiecutter https://github.com/Fsnk2001/base-django-template.git
```

You'll be prompted for some values. Provide them, then a Django project will be created for you.
