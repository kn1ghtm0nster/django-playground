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

- **NOTE:** You may need to use `py` instead of `python` in your terminal. Just depends on the shell you're using (i.e., `Powershell` or the `CMD` line terminal).

- **NOTE II:** **If** you encounter issues with dependencies, ensure **your `Python` version is correct and your `virtual environment` is activated.**

## Seeding Data

This project provides several custom Django management commands (i.e. commands you can run in the terminal locally) to generate fake data for testing and learning purposes.

**NOTE:** If you ran the `migration` commands when pulling the code down to your local, there will be existing data available. Running these commands **will add** new records unless you use the `--delete` flag.

**NOTE II:** If you're using `WSL`, follow the `MacOS / Linux` commands.

Available commands

- **Create fake people:**

  ```bash
  # MacOS / Linux
  python3 manage.py create_fake_people --count 15

  # Windows (default terminal - not recommended)
  py manage.py create_fake_people --count 15
  ```

  - Will create 15 fake `Person` objects. Use `--delete` to clear existing people before adding new ones.

  - You can use the `--count` flag without specifying a number; the default is 10.

- **Create fake authors:**

  ```bash
  # MacOS / Linux
  python3 manage.py create_fake_authors --count 10

  # Windows (default terminal - not recommended)
  py python manage.py create_fake_authors --count 10
  ```

  - Will create 10 fake `Author` objects. Supports the `--delete` flag.

  - You can use the `--count` flag without specifying a number; the default is 10.

- **Create fake blog posts:**

  ```bash
  # MacOS / Linux
  python3 manage.py create_fake_blogposts --count 20

  # Windows (default terminal - not recommended)
  py manage.py create_fake_blogposts --count 20
  ```

  - Will create 20 fake `BlogPost` objects, each assigned to a random author. Supports the `--delete` flag.

  - You can use the `--count` flag without specifying a number; the default is 10.

- **Create fake tags:**

  ```bash
  # MacOS / Linux
  python3 manage.py create_fake_tags --count 10

  # Windows (default terminal - not recommended)
  py manage.py create_fake_tags --count 10
  ```

  - Will create 10 fake `Tag` objects and associates them with random blog posts. Supports the `--delete` flag.

  - You can use the `--count` flag without specifying a number; the default is 10.

## Project Structure

## Models & Relationships

This project uses several Django models to demonstrate core `ORM` concepts and relationships. Below is a summary of each model and how they relate to one another. For full details on Django models and relationships, **please consult the [official Django documentation](https://docs.djangoproject.com/en/5.2/topics/db/models/).**

- `Person`

  - Represents a simple user with fields for first name, last name, age, email, and creation date.

  - No direct relationships to other models in this playground. Mainly a dummy model for understanding specific methods in the Django `ORM`.

- `Author`

  - Represents a blog author, with fields for name, bio, website, email, and creation date.

  - Does NOT inherit from the `Person` class--these are separate concepts for demonstration purposes.

- `BlogPost`

  - Represents a blog post with a title, content, and timestamps.

  - **ForeignKey to `Author`:** Each blog post is written by one author (e.g., `author = models.ForeignKey(Author, ...)`).

- `Tag`

  - Represents a tag that can be attached to blog posts.

  - **ManyToManyField to `BlogPost`:** Each tag can be associated with multiple blog posts, and each blog post can have multiple tags (e.g., `posts = models.ManyToManyField(BlogPost,...)`)

**NOTE:**

- If you're new to the Django framework or unsure about any model field or relationship, I encourage you to **[open the Django docs](https://docs.djangoproject.com/en/5.2/)**.

- This project is for learning--experiment, break things, and use the docs as your primary reference! I do this all the time (even at work).

## Features

## API Endpoints

## Development Notes

## Contributing

## License
