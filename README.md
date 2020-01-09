# Codename: Thor

A small application used to query the cnx-db using ORM based models

## Setup

Run the services:

    docker-compose up

Initialize the database:

    make initdb

Create a virtualenv:

    python -m venv .venv

Activate virtualenv:

    source .venv/bin/activate

Install dependencies

    pip install -r requirements.txt

Run edit and run app.py to run a queries and return results. Happy querying!

    python app.py

