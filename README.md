# Django Interactive Playground (Back-End)

The `Django Interactive Playground` back-end provides a safe, sandboxed environment for new developers to experiment with Django's core features--models, querysets, and relationships--using realistic **FAKE** data.

This backend is designed to power an interactive front-end (**LINK TBD**) and exposes API endpoints for learning and demonstrating purposes.

**WARNING :** This project is intended for **EDUCATIONAL PURPOSES ONLY** and is **NOT** meant for production deployments.

## Table of Contents

- [Setup & Installation](#setup--installation)

- [Seeding Data](#seeding-data)

- [Project Structure](#project-structure)

- [Models & Relationships](#models--relationships)

- [Features](#features)

- [API Endpoints](#api-endpoints)

- [Development Notes](#development-notes)

- [Contributing](#contributing)

- [License](#license)

## Setup & Installation

Prerequisites

- **Python 3.9+** (recommended: use [pyenv](https://github.com/pyenv/pyenv) or [python.org](https://www.python.org/downloads/))

- **pip** (Python package manager)

- **virtualenv** (recommended for isolated environments)

- **git** (source control)

Follow the guides below based on your operating system.

**MacOS / Linux**

```bash
# 1. Clone the repository
git clone https://github.com/kn1ghtm0nster/django-playground.git
cd django-playground

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy the example .env file and set your SECRET_KEY
cp .env.example .env
# Edit .env to set your SECRET_KEY and DEBUG as needed

# 5. Run migrations
python3 manage.py makemigrations
python3 manage.py migrate

# 6. (Optional) Seed the database with fake data
python3 manage.py create_fake_people --count 15
python3 manage.py create_fake_authors --count 10
python3 manage.py create_fake_blogposts --count 20
python3 manage.py create_fake_tags --count 10

# 7. Start the development server
python3 manage.py runserver
```

**Windows ([WSL](https://learn.microsoft.com/en-us/windows/wsl/install) HIGHLY Recommended)**

- **If** already using `WSL`, follow the **MacOS / Linux** instructions above in your WSL terminal.

**If** using **NATIVE WINDOWS (NOT recommended)**

```bash
# 1. Clone the repository
git clone https://github.com/kn1ghtm0nster/django-playground.git
cd django-playground

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy the example .env file and set your SECRET_KEY
copy .env.example .env
# Edit .env to set your SECRET_KEY and DEBUG as needed

# 5. Run migrations
python manage.py makemigrations
python manage.py migrate

# 6. (Optional) Seed the database with fake data
python manage.py create_fake_people --count 15
python manage.py create_fake_authors --count 10
python manage.py create_fake_blogposts --count 20
python manage.py create_fake_tags --count 10

# 7. Start the development server
python manage.py runserver
```

- **NOTE:** You may need to use `py` instead of `python` in your terminal. Just depends on the shell you're using (i.e. `Powershell` or the `CMD` line terminal).

- **NOTE II:** **If** you encounter issues with dependencies, ensure **your `Python` version is correct and your `virtual environment` is activated.**

## Seeding Data

## Project Structure

## Models & Relationships

## Features

## API Endpoints

## Development Notes

## Contributing

## License
